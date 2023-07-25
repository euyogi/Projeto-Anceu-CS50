// Informações nas últimas linhas.

#include <fstream>
#include <filesystem>

#include "neyo.h"
#include "zlib.h"

#define NOT_FOUND (size_t)(-1)

void	processStream(std::string&, size_t&, char*, size_t);
bool	seen2(const char*, const char*);
bool	seen3(const char*, const char*);
size_t	findSubstr(const char*, size_t, const char*, size_t, size_t = 0);

// Dado uma string para armazenar e um caminho com nome do pdf, extrai texto na string (sem espaços ou quebras de linha).
void Neyo::pdfToTxt(std::string& txt_container, const wchar_t* pdf_pn) {
	// Abre pdf e guarda seu tamanho.
	std::ifstream file(pdf_pn, std::ios::binary);
	size_t file_size = std::filesystem::file_size(std::filesystem::path(pdf_pn));

	// Lê o pdf no buffer.
	char* pdf_buffer = new char[file_size];
	memset(pdf_buffer, NULL, file_size);
	file.read(pdf_buffer, file_size);
	file.close();

	// Reserva memória para armazenar o texto do pdf.
	txt_container.clear();
	txt_container.resize(file_size / 2);

	// Itera o buffer procurando por streams para processá-las.
	size_t txt_container_ridx = 0;
	size_t offset = 0; // Desvio para marcar o quanto já iteramos no buffer.
	while (true) {
		size_t stream_start = findSubstr("stream", 6, pdf_buffer, file_size, offset);

		if (stream_start == NOT_FOUND)
			break;

		size_t stream_end = findSubstr("endstream", 9, pdf_buffer, file_size, stream_start);

		// Pula alguns caracteres no começo e no fim da stream para conseguirmos descomprimi-la.
		stream_start += 6;

		if (pdf_buffer[stream_start] == '\r' and pdf_buffer[stream_start + 1] == '\n')
			stream_start += 2;
		else if (pdf_buffer[stream_start] == '\n')
			++stream_start;

		if (pdf_buffer[stream_end - 2] == '\r' and pdf_buffer[stream_end - 1] == '\n')
			stream_end -= 2;
		else if (pdf_buffer[stream_end - 1] == '\n')
			--stream_end;

		// Assume que a stream descomprimida será até 20x maior que a comprimida.
		size_t stream_buffer_capacity = (stream_end - stream_start) * 20;
		char* stream_buffer = new char[stream_buffer_capacity];

		// Usa zlib para descomprimir:
		z_stream zstrm; memset(&zstrm, NULL, sizeof(zstrm));

		zstrm.avail_in = static_cast<uInt>(stream_end - stream_start + 1);
		zstrm.avail_out = static_cast<uInt>(stream_buffer_capacity);
		zstrm.next_in = reinterpret_cast<Bytef*>(pdf_buffer + stream_start);
		zstrm.next_out = reinterpret_cast<Bytef*>(stream_buffer);
		
		int rsti = inflateInit(&zstrm);
		if (rsti == Z_OK) {
			int rst2 = inflate(&zstrm, Z_FINISH);
			if (rst2 >= 0)
				processStream(txt_container, txt_container_ridx, stream_buffer, zstrm.total_out);
		}

		delete[] stream_buffer;
		offset = stream_end + 6;
	}

	delete[] pdf_buffer;
	return;
}

// Extrai apenas o texto da stream no container.
void processStream(std::string& txt_container, size_t& txt_container_ridx, char* stream, size_t stream_size) {
	bool in_footer = false; // Estamos dentro do rodapé (entre "/Footer" e "EMC").
	bool in_txt_object = false; // Estamos dentro do objeto de texto (entre os tokens BT e ET).
	bool next_literal = false; // Próximo carácter faz parte do texto (e.g. '\\' para uma '\' ou '\(' para um '(').
	bool in_brackets = false; // Estamos dentro de parênteses (texto fica dentro deles).
	char last_4_chars[4]{}; // Armazena os últimos 4 carácteres vistos.

	for (size_t i = 0; i < stream_size; ++i) {
		char c = stream[i]; // Mais eficiente que por const& e por stream[i]

		if (in_txt_object) {
			if (not in_brackets and seen2("ET", last_4_chars)) // Objeto de texto termina em ET.
				in_txt_object = false;
			else if (c == '(' and not (in_brackets and next_literal)) // Texto está dentro de parênteses.
				in_brackets = true;
			else if (c == ')' and in_brackets and not next_literal)
				in_brackets = false;
			else if (in_brackets) {
				if (c == '\\' and not next_literal)
					next_literal = true;
				else {
					next_literal = false;
					if ((c >= '!') and (c <= '~')) { // Caracteres normais.
						txt_container[txt_container_ridx] = c;
						++txt_container_ridx;
					}
				}
			}
		}
		else if (not in_footer) {
			if (seen2("BT", last_4_chars)) // Objeto de texto começa em "BT".
				in_txt_object = true;
			else if (seen3("/Fo", last_4_chars)) // Rodapé começa em "/Footer", "/Fo" funciona.
				in_footer = true;
		}
		else if (seen3("EMC", last_4_chars)) // Rodapé termina em "EMC".
			in_footer = false;

		// Remove o primeiro caráctere, move o resto à esquerda e guarda um novo caráctere.
		for (int j = 0; j < 3; ++j)
			last_4_chars[j] = last_4_chars[j + 1];
		last_4_chars[3] = c;
	}
}

// Checa se um token de dois carácteres apareceu (e.g. BT ou ET).
inline bool seen2(const char* token, const char* str) {
	if (str[1] == token[0] and str[2] == token[1] and (str[3] == ' ' || str[3] == '\r' || str[3] == '\n') and (str[0] == ' ' || str[0] == '\r' || str[0] == '\n'))
		return true;

	return false;
}

// Checa se um token de três carácteres apareceu (e.g. /Fo ou EMC).
inline bool seen3(const char* token, const char* str) {
	if (str[0] == token[0] and str[1] == token[1] and str[2] == token[2])
		return true;

	if (str[1] == token[1] and str[2] == token[2] and str[3] == token[3])
		return true;

	return false;
}

// Procura substring (terminada em null) em string, dado o tamanho de string.
inline size_t findSubstr(const char* substr, size_t substr_len, const char* str, size_t str_len, size_t offset) {
	while (offset + substr_len <= str_len) {
		bool found = true;
		for (size_t j = 0; j < substr_len; ++j) {
			if (str[offset + j] != substr[j]) {
				found = false;
				break;
			}
		}

		if (found)
			return offset;

		++offset;
	}

	return NOT_FOUND;
}

// Optei por armazenar o texto extraído em uma string para não precisar usar delete[]
// no código principal sem usar new antes.

// Optei por não utilizar strings exceto para o texto extraído pois já tenho o tamanho dos buffers (não preciso de
// buffer.size()) e já tenho a função findSubstr() (não preciso de buffer.find()) além de um mínimo ganho em
// performance (quase negligente, exceto em last_4_chars em processStream(), esse não deve ser uma string por
// razões de performance, apesar de uma array funcionar sem tanta perda de performance).