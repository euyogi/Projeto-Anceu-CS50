#pragma once

#include <string>

namespace Neyo {
	// Dado uma string para armazenar e um caminho com nome do pdf, extrai texto na string (sem espaços ou quebras de linha).
	void pdfToTxt(std::string& txt_container, const wchar_t* pdf_pn);
}