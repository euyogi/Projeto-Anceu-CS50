#include "anceu.h"

#include <urlmon.h> // Lembre de incluir respectivo diretório de biblioteca;

#include <string>
#include <array>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <filesystem>
#include <future>
#include <format>

//#define DFUNCS
#include "neyo.h" // Lembre de incluir respectivo diretório de biblioteca;
#include "texts.h"
#include "utils.h"

// Urls dos pdfs que vão ser baixados (temporariamente).

const wchar_t* grades_url[] = {
	L"https://cdn.cebraspe.org.br/vestibulares/UNB_23_ACESSOENEM/arquivos/ED_8_2023_ACESSO_ENEM_RES_FINAL_BIOP_HETERO.PDF", // 2023
	L"https://cdn.cebraspe.org.br/vestibulares/UNB_22_ACESSOENEM/arquivos/ED_6_ACESSOENEM_22_RES_FINAL_BIOP_SCEP_E_NO_PROCESSO.PDF", // 2022
	L"https://cdn.cebraspe.org.br/vestibulares/UNB_21_1_ACESSOENEM/arquivos/ED_7_2020_ACESSOENEM_21_RELAO_FINAL_BIOPSICOSSOCIAL.PDF" // 2021
};

const wchar_t* approved_url[3][5] = {
	{ // 2023
		L"https://cdn.cebraspe.org.br/vestibulares/UNB_23_ACESSOENEM/arquivos/ED_9_2023_ACESSO_ENEM_CONV_RA_1_CHAMADA.PDF",
		L"https://cdn.cebraspe.org.br/vestibulares/UNB_23_ACESSOENEM/arquivos/ED_12_2023_ACESSO_ENEM_CONV_RA_2_CHAMADA.PDF"
	},
	{ // 2022
		L"https://cdn.cebraspe.org.br/vestibulares/UNB_22_ACESSOENEM/arquivos/ED_7_ACESSOENEM_22_RES_CONV_1_CHAMADA.PDF",
		L"https://cdn.cebraspe.org.br/vestibulares/UNB_22_ACESSOENEM/arquivos/ACESSOENEM_22_ED_10_CONV_RA_2_CHAMADA.PDF",
		L"https://cdn.cebraspe.org.br/vestibulares/UNB_22_ACESSOENEM/arquivos/ED_14_ACESSOENEM_22_CONV_RA_3_CHAMADA.PDF",
		L"https://cdn.cebraspe.org.br/vestibulares/UNB_22_ACESSOENEM/arquivos/ED_17_ACESSOENEM_22_CONV_RA_4_CHAMADA.PDF",
		L"https://cdn.cebraspe.org.br/vestibulares/UNB_22_ACESSOENEM/arquivos/ED_20_ACESSOENEM_22_CONV_RA_5_CHAMADA.PDF"
	},
	{ // 2021
		L"https://cdn.cebraspe.org.br/vestibulares/UNB_21_1_ACESSOENEM/arquivos/ED_8_2020_ACESSOENEM_21_CONV_1A_CHAMADA.PDF",
		L"https://cdn.cebraspe.org.br/vestibulares/UNB_21_1_ACESSOENEM/arquivos/ED_11_2020_ACESSOENEM_21_CONV_2A_CHAMADA.PDF",
		L"https://cdn.cebraspe.org.br/vestibulares/UNB_21_1_ACESSOENEM/arquivos/ED_13_2020_ACESSOENEM_21_CONV_3A_CHAMADA.PDF",
		L"https://cdn.cebraspe.org.br/vestibulares/UNB_21_1_ACESSOENEM/arquivos/ED_17_2020_ACESSOENEM_21_CONV_4A_CHAMADA.PDF",
	}
};

std::string grades_txt, approved_txt; // Textos extraídos dos pdfs serão armazenados nessas strings.
std::string Anceu::results, Anceu::details; // Resultados (serão mostrados ao usuário).
constexpr size_t REGISTRATION_LEN = 8;
constexpr int QUOTAS_QNT = 10, APPROVED_QNT = 2300; // Um pouco maior que o número exato de aprovados, mas é para evitar alocações.
int searched_year, searched_call; // Ao baixar os pdfs essas variáveis vão ser preenchidas e utilizados por extractPdfs.

// Dados de um candidato.
struct Candidate {
	Candidate(int registration) { DERR(registration < 10000000 or registration > 20000000, "Erro: inscricao [" << registration << "] invalida!")
		m_registration = registration;
	}

	void setGrade(float grade) { DERR(grade <= 0.0f or grade >= 1000.0f, "Erro: nota [" << grade << "] invalida!")
		m_grade = grade;
	}

	void addRanking(int ranking) { DERR(m_rankings_qnt >= 10, "Erro: limite de classificacoes ultrapassado!")
								   DERR(ranking < 0, "Erro: classificacao [" << ranking << "] invalido!")
		m_rankings[m_rankings_qnt] = ranking;
		++m_rankings_qnt;
	}

	int getRegistration() { return m_registration; }
	float getGrade() { return m_grade; }
	const std::array<int, QUOTAS_QNT>& getRankings() { return m_rankings; }

private:
	int m_registration, m_rankings_qnt = 0; // e.g.: 10000000.
	float m_grade = 0.0f; // e.g.: 999.99.
	std::array<int, QUOTAS_QNT> m_rankings {}; // e.g.: { 23, 4, 0, 0, 0, 1, 2, 3, 1, 3 }.
};

struct Quota {
	~Quota() {
		delete[] m_name;
	}

	void setName(const char* name) {
		size_t name_len = strlen(name);
		m_name = new char[name_len + 1];

		for (size_t i = 0; i < name_len; ++i)
			m_name[i] = name[i];

		m_name[name_len] = '\0';
	}

	void addGrade(float grade) { DERR(grade <= 0.0f or grade >= 1000.0f, "Erro: nota [" << grade << "] invalida!")
		m_grades_sum += grade;
		++m_slots;

		if (grade > m_max)
			m_max = grade;

		if (grade < m_min)
			m_min = grade;

		m_avg = m_grades_sum / m_slots;
	}

	const char* getName() { return m_name; }
	int getSlots() { return m_slots; }
	float getMax() { return m_max; }
	float getMin() { return m_min; }
	float getAvg() { return m_avg; }

private:
	char* m_name = nullptr;
	float m_grades_sum = 0.0f, m_max = 0.0f, m_min = 1000.0f, m_avg = 0.0f;
	int m_slots = 0;
};

std::string formatCourseName(const char*);
bool		downloadFile(const wchar_t*, const wchar_t*);

bool Anceu::extractGrades(const char* course) { DTIMER(__func__)
	// Extrai número das inscrições dos aprovados em todos os cursos.
	std::unordered_set<int> approved_registrations;
	approved_registrations.reserve(APPROVED_QNT);
	for (size_t i = REGISTRATION_LEN + 1; i < approved_txt.size(); ++i) {
		// Localiza uma inscrição (estão entre letra minúscula, e letra maiúscula).
		if (!(islower(approved_txt[i - REGISTRATION_LEN - 1]) and approved_txt[i - REGISTRATION_LEN] == '1' and isupper(approved_txt[i])))
			continue;

		char registration_buffer[REGISTRATION_LEN + 1];
		registration_buffer[REGISTRATION_LEN] = '\0';

		// Itera extraindo a inscrição.
		for (size_t j = 0; j < REGISTRATION_LEN; ++j)
			registration_buffer[j] = approved_txt[i - REGISTRATION_LEN + j];

		approved_registrations.insert(std::stoi(registration_buffer));
	}

	int start_idx = (course[2] == ']' ? 4 : 5); // Para ignorar o grupo do curso "[I]" ou "[II]".
	std::string course_name = formatCourseName(course + start_idx);
	size_t campus_shift_idx = 0;

	if (size_t idx = course_name.find("(PLA"); idx != std::string::npos) {
		campus_shift_idx = grades_txt.find("PLA"); // (menor string que funciona).
		course_name.replace(idx, course_name.size() - 1, "");
	}
	else if (idx = course_name.find("(GAM"); idx != std::string::npos) {
		campus_shift_idx = grades_txt.find("GAM"); // (menor string que funciona).
		course_name.replace(idx, course_name.size() - 1, "");
	}
	else if (idx = course_name.find("(CEI"); idx != std::string::npos) {
		campus_shift_idx = grades_txt.find("CEI"); // (menor string que funciona).
		course_name.replace(idx, course_name.size() - 1, "");
	}

	if (size_t idx = course_name.find("(NOTU"); idx != std::string::npos) {
		campus_shift_idx = grades_txt.find("NOTU", campus_shift_idx); // (menor string que funciona).
		course_name.replace(idx, course_name.size() - 1, "");
	}
	
	// Localiza a posição do curso escolhido.
	size_t course_idx = grades_txt.find(course_name, campus_shift_idx); DLOG("course_name = " << course_name)

	if (course_idx == std::string::npos)
		return false;

	course_idx += course_name.size() - 1;

	// Extrai dados dos candidatos aprovados no curso escolhido.
	std::vector<Candidate> approved_candidates;
	approved_candidates.reserve(APPROVED_QNT / 10);
	bool first_candidate = true; int commas_count = 0;
	while (true) { // Itera, a partir do início do curso até o fim do curso.
		// Localiza uma inscrição (estão logo após uma '/' ou ')').
		if (!(grades_txt[course_idx] == '/' or first_candidate)) {
			if (grades_txt[course_idx] == ',')
				++commas_count;
			else if (commas_count == 12 and grades_txt[course_idx] == '.') // Fim do curso.
				break;

			++course_idx;
			continue;
		}

		if (first_candidate)
			first_candidate = false;

		char registration_buffer[REGISTRATION_LEN + 1];
		registration_buffer[REGISTRATION_LEN] = '\0';

		// Itera extraindo a inscrição.
		size_t i;
		for (i = 1; i <= REGISTRATION_LEN; ++i)
			registration_buffer[i - 1] = grades_txt[course_idx + i];

		int registration_numeric_buffer = std::stoi(registration_buffer);

		// Incrementa o index para não precisar iterar o que iteramos no for loop.
		course_idx += i;
		commas_count = 0;

		// Checa se é uma inscrição de aprovado.
		if (approved_registrations.find(registration_numeric_buffer) == approved_registrations.end())
			continue;

		approved_candidates.push_back(Candidate(registration_numeric_buffer));
		std::string grade_buffer, ranking_buffer;

		while (true) { // Itera extraindo os dados.
			if (grades_txt[course_idx] == '/' or (commas_count == 12 and grades_txt[course_idx] == '.')) {
				approved_candidates.back().addRanking(ranking_buffer.front() == '-' ? 0 : std::stoi(ranking_buffer));
				--course_idx;
				break;
			}
			else if (grades_txt[course_idx] == ',') {
				if (commas_count >= 3) {
					approved_candidates.back().addRanking(ranking_buffer.front() == '-' ? 0 : std::stoi(ranking_buffer));
					ranking_buffer.clear();
				}
				++commas_count;
			}
			else if (commas_count == 2)
				grade_buffer.push_back(grades_txt[course_idx]);
			else if (commas_count >= 3)
				ranking_buffer.push_back(grades_txt[course_idx]);

			++course_idx;
		}
		approved_candidates.back().setGrade(std::stof(grade_buffer));
	}

	std::array<Quota, QUOTAS_QNT> results_arr;
	for (int i = 0; i < QUOTAS_QNT; ++i)
		results_arr[i].setName(Texts::QUOTAS_NAMES[i]);

	for (Candidate& c : approved_candidates) {
		// Checa em qual sistema o candidato foi aprovado.
		int min = c.getRankings().front();
		int min_idx = 0;

		for (int i = 1; i < QUOTAS_QNT; ++i) {
			if (c.getRankings()[i] and c.getRankings()[i] < min) {
				min = c.getRankings()[i];
				min_idx = i;
			}
		}

		results_arr[min_idx].addGrade(c.getGrade());
	}

	// Formata nossos dados para uso no GUI.
	const char* group = start_idx == 4 ? "I" : "II";

	results.reserve(1000);
	results = std::format("Curso: {}; Grupo: {};\nAno: {}; Chamada: {}", course + start_idx, group, searched_year, searched_call);
	results += "ª; Convocados/Vagas Totais: "; results += std::format("{}\n", approved_candidates.size());

	if (results_arr[0].getSlots() == 0 and results_arr[1].getSlots() == 0)
		results += "\nNenhum convocado da ampla nesta chamada";
	else
		results += "\nAmpla:\n";

	for (int i = 0; i < results_arr.size(); ++i) {
		if (i == 2) {
			if (approved_candidates.size() == results_arr[0].getSlots() + results_arr[1].getSlots())
				results += "\n\nNenhum convocado de escola pública nesta chamada";
			else
				results += "\n\nCotas de Escola Pública:\n";
		}

		if (results_arr[i].getSlots() > 0) {
			results += std::format("\nQnt: {:02d}; ", results_arr[i].getSlots()); results += results_arr[i].getName();
			results += " Máx: "; results += std::format("{:.2f}", results_arr[i].getMax());
			results += "; Méd: "; results += std::format("{:.2f}", results_arr[i].getAvg());
			results += "; Min: "; results += std::format("{:.2f}", results_arr[i].getMin());
		}
	}
	results += "\n\n[Clique com o botão direito do mouse/touchpad ou Ctrl + C para copiar]";

	details.reserve(approved_candidates.size() * 90);
	details = "Inscrição Nota      Posição\n";

	// Ordena os dados em ordem decrescente de nota.
	std::sort(approved_candidates.begin(), approved_candidates.end(), [](Candidate& a, Candidate& b) {
		return a.getGrade() > b.getGrade();
	});

	for (Candidate& c : approved_candidates) {
		details += std::format("{}, {:.2f}", c.getRegistration(), c.getGrade());
		for (int i = 0; i < QUOTAS_QNT; ++i) {
			if (i == 0)
				details += std::format(",{:4d}", c.getRankings()[i]);
			else
				details += c.getRankings()[i] == 0 ? ",  -" : std::format(",{:3d}", c.getRankings()[i]);
		}
		details += ".\n";
	}
	details += "\n[Clique com o botão direito do mouse/touchpad ou Ctrl + C para copiar]";

	return true;
}

// Caminho com destino e nome dos pdfs.
static std::filesystem::path grades_pn = std::filesystem::temp_directory_path().append("grades.pdf");
static std::filesystem::path approved_pn = std::filesystem::temp_directory_path().append("approved.pdf");

// Baixa os dois pdfs simultaneamente.
bool Anceu::downloadPdfs(int year, int call) { DTIMER(__func__)
	searched_year = year; searched_call = call;
	std::future<bool> task_1 = std::async(std::launch::async, downloadFile, grades_url[2023 - year], grades_pn.c_str());
	std::future<bool> task_2 = std::async(std::launch::async, downloadFile, approved_url[2023 - year][call - 1], approved_pn.c_str());
	bool r_1 = task_1.get(); bool r_2 = task_2.get();
	return (r_1 and r_2);
}

// Extrai texto dos dois pdfs simultaneamente.
bool Anceu::convertPdfs() { DTIMER(__func__)
	std::future<void> task_1 = std::async(std::launch::async, Neyo::pdfToTxt, std::ref(grades_txt), grades_pn.c_str());
	std::future<void> task_2 = std::async(std::launch::async, Neyo::pdfToTxt, std::ref(approved_txt), approved_pn.c_str());
	task_1.wait(); task_2.wait();
	return !(grades_txt.empty() or approved_txt.empty());
}

// Deleta os dois pdfs.
void Anceu::deletePdfs() { DTIMER(__func__)
	std::filesystem::remove(grades_pn);
	std::filesystem::remove(approved_pn);
}

// Retorna uma cópia do nome em maiúsculo, sem diacríticos e espaços.
std::string formatCourseName(const char* course_name) { DTIMER(__func__)
	size_t course_name_len = strlen(course_name);
	std::string formatted_course_name;
	formatted_course_name.reserve(course_name_len);
	for (size_t i = 0; i < course_name_len; ++i) {
		char c = course_name[i];
		if (c >= '!' and c <= '~')
			formatted_course_name.push_back(toupper(c));
	}
	return formatted_course_name;
}

// Dado um url e um caminho com destino e nome do arquivo escolhido, baixa-o nesse caminho.
bool downloadFile(const wchar_t* w_url, const wchar_t* w_path_with_name) {
	// Veja: https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775123(v=vs.85)
	HRESULT result = URLDownloadToFileW(nullptr, w_url, w_path_with_name, 0, nullptr);
	return result == S_OK;
}
