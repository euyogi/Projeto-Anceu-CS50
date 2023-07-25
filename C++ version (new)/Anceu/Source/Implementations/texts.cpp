#include "texts.h"

// Ativar compatibilidade com unicode.
#define U8(_S) (const char*)u8##_S

const char* Texts::NW_TIP_MARKER_INITIAL = "Ver texto inicial";
const char* Texts::NW_TIP_MARKER_INFO = U8("Ver informa��es sobre o programa");

const char* Texts::SMALLER_TEXT_BOX_INITIAL = U8("Pesquise ou selecione um curso para come�ar");
const char* Texts::SMALLER_TEXT_BOX_INFO = U8("Informa��es sobre o programa");
const char* Texts::SMALLER_TEXT_BOX_NO_COURSE_SELECTED = U8("Erro: nenhum curso foi selecionado");
const char* Texts::SMALLER_TEXT_BOX_DOWNLOADING = "Baixando pdfs, aguarde...";
const char* Texts::SMALLER_TEXT_BOX_DOWNLOAD_FAILED = "Erro: falha ao baixar os pdfs, tente novamente";
const char* Texts::SMALLER_TEXT_BOX_RESULTS = "Resumo das notas abaixo";
const char* Texts::SMALLER_TEXT_BOX_DETAILS = U8("Inscri��es, notas e posi��es detalhadas abaixo");
const char* Texts::SMALLER_TEXT_BOX_EXTRACT_FAILED = "Erro: falha ao extrair os dados dos pdfs, tente novamente";

const char* Texts::BUTTON_SEARCH = "Pesquisar";

const char* Texts::BIGGER_TEXT_BOX_INITIAL = U8("Ol�, este programa mostra as notas dos candidatos aprovados na UnB pelo acesso Enem.\n\n")
	"Para come�ar, voc� pode escolher o curso desejado na lista de cursos dispon�veis acima e clicar em pesquisar para checar as notas m�ximas"
	"(1� lugar), m�nimas (nota de corte/�ltimo lugar) e tamb�m a m�dia das notas, de acordo com cada cota que a universidade disponibiliza.\n\n"
	"Voc� pode escolher o ano que deseja checar e tamb�m a chamada, al�m de ser poss�vel ver todas as notas, com o n�mero de inscri��o e"
	"respectivas posi��es do candidato no bot�o \"Ver Detalhes\"\n\n"
	"Caso queira dar zoom no texto voc� pode utilizar Ctrl + Scroll (rodinha do mouse/gesto de pin�a no touchpad), com a setinha emcima desse"
	"texto aqui, al�m disso voc� pode abrir links e copiar os resultados pesquisados com clique direito do mouse/touchpad ou Ctrl + C para copiar\n\n"
	"Informa��es sobre o programa no 'i' no canto superior esquerdo.";
const char* Texts::BIGGER_TEXT_BOX_INFO = U8("Este programa n�o tem nenhuma afilia��o com a Universidade de Bras�lia. Os dados utilizados est�o")
	"dispon�veis para o p�blico no seguinte url: https://www.cebraspe.org.br/ [1]\n\n"
	"Criador : Yogi Nam de Souza Barbosa\n"
	"Github: https://github.com/euyogi/ [2]\n\n"
	"Este programa � meu projeto final do curso: CS50 - Introduction to Computer Science of Harvard University\n"
	"Dispon�vel no seguinte url: https://pll.harvard.edu/course/cs50-introduction-computer-science/ [3]\n\n"
	"Feito em C++ com ImGui :)\n\n"
	"Caso tenha encontrado algum comportamento incorreto e queira colaborar reportando esse erro - (Necess�rio criar conta github)\n"
	"Reporte no seguinte url: https://github.com/euyogi/Projeto-CS50/issues/new/ [4]\n\n"
	"[Clique com o bot�o direito do mouse/touchpad para abrir qualquer um dos links]";

const char* Texts::BUTTON_COPY = "Copiar";
const char* Texts::BUTTON_OPEN1 = "Abrir [1]";
const char* Texts::BUTTON_OPEN2 = "Abrir [2]";
const char* Texts::BUTTON_OPEN3 = "Abrir [3]";
const char* Texts::BUTTON_OPEN4 = "Abrir [4]";

const char* Texts::SW_TIP_MARKER = U8("Escolha o ano e a chamada que voc�\n  quer checar as notas de corte");
const char* Texts::SE_BUTTON_DETAILS = "Ver Detalhes";
const char* Texts::SE_BUTTON_RESULTS = "Ver Resumo";
const char* Texts::BUTTON_EXIT = "Sair";

const char* Texts::LABEL_CONVERTER = "Converter Notas";
const char* Texts::NE1_TIP_MARKER = U8("A UnB possui diferentes pesos\npara cada �rea, de acordo com\n o grupo do curso, calcule a\n sua nota com os pesos aqui");
const char* Texts::LABEL_GROUP = "Grupo do Curso";
const char* Texts::NE2_TIP_MARKER = U8("N�o sabe o grupo do seu curso?\nO grupo est� na frente de cada\n\tcurso na lista ao lado");

const char* Texts::RADIO1 = "Grupo I";
const char* Texts::RADIO2 = "Grupo II";

const char* Texts::LABEL_GRADES = "Insira as Notas";
const char* Texts::LABEL_LITERATURE = "Linguagens";
const char* Texts::LABEL_HUMANITIES = "Humanas";
const char* Texts::LABEL_NATURE = "Natureza";
const char* Texts::LABEL_MATH = U8("Matem�tica");
const char* Texts::LABEL_ESSAY = U8("Reda��o");

const char* Texts::BUTTON_CONVERT = "Converter";

const char* Texts::COURSES[101] = {
	U8("[I] Administra��o (Bacharelado)"),
	U8("[II] Agronomia (Bacharelado)"),
	U8("[I] Arquitetura e Urbanismo (Bacharelado)"),
	U8("[I] Artes C�nicas - Interpreta��o Teatral (Bacharelado)"),
	U8("[I] Artes Visuais (Bacharelado)"),
	U8("[I] Artes Visuais (Licenciatura)"),
	U8("[I] Biblioteconomia (Bacharelado)"),
	U8("[II] Biotecnologia (Bacharelado)"),
	U8("[II] Ci�ncia da Computa��o (Bacharelado)"),
	U8("[I] Ci�ncia Pol�tica (Bacharelado)"),
	U8("[II] Ci�ncias Biol�gicas (Bacharelado)"),
	U8("[I] Ci�ncias Cont�beis (Bacharelado)"),
	U8("[I] Ci�ncias Econ�micas (Bacharelado)"),
	U8("[I] Ci�ncias Sociais � Antropologia/Sociologia (Bacharelado/Licenciatura)"),
	U8("[I] Comunica��o Social � Audiovisual (Bacharelado)"),
	U8("[I] Comunica��o Social � Publicidade e Propaganda (Bacharelado)"),
	U8("[I] Design � Programa��o Visual/Projeto do Produto (Bacharelado)"),
	U8("[I] Direito (Bacharelado)"),
	U8("[II] Educa��o F�sica (Bacharelado)"),
	U8("[II] Educa��o F�sica (Licenciatura)"),
	U8("[II] Enfermagem (Bacharelado)"),
	U8("[II] Engenharia Ambiental (Bacharelado)"),
	U8("[II] Engenharia Civil (Bacharelado)"),
	U8("[II] Engenharia de Computa��o (Bacharelado)"),
	U8("[II] Engenharia de Redes de Comunica��o (Bacharelado)"),
	U8("[II] Engenharia El�trica (Bacharelado)"),
	U8("[II] Engenharia Florestal (Bacharelado)"),
	U8("[II] Engenharia Mec�nica (Bacharelado)"),
	U8("[II] Engenharia Mecatr�nica � Controle e Automa��o (Bacharelado)"),
	U8("[II] Engenharia Qu�mica (Bacharelado)"),
	U8("[II] Estat�stica (Bacharelado)"),
	U8("[II] Farm�cia (Bacharelado)"),
	U8("[I] Filosofia (Bacharelado/Licenciatura)"),
	U8("[II] F�sica (Bacharelado)"),
	U8("[II] Geof�sica (Bacharelado)"),
	U8("[I] Geografia (Bacharelado/Licenciatura)"),
	U8("[II] Geologia (Bacharelado)"),
	U8("[I] Hist�ria (Bacharelado/Licenciatura)"),
	U8("[I] Jornalismo (Bacharelado)"),
	U8("[I] Letras � Portugu�s do Brasil como Segunda L�ngua (Licenciatura)"),
	U8("[I] Letras � Tradu��o � Franc�s (Bacharelado)"),
	U8("[I] Letras � Tradu��o � Ingl�s (Bacharelado)"),
	U8("[I] Licenciatura em Artes C�nicas"),
	U8("[I] L�ngua Estrangeira Aplicada � Multilinguismo e Sociedade da Informa��o (Bacharelado)"),
	U8("[I] L�ngua Francesa e Respectiva Literatura (Bacharelado/Licenciatura)"),
	U8("[I] L�ngua Inglesa e Respectiva Literatura (Bacharelado/Licenciatura)"),
	U8("[I] L�ngua Portuguesa e Respectiva Literatura (Bacharelado/Licenciatura)"),
	U8("[II] Matem�tica (Bacharelado/Licenciatura)"),
	U8("[II] Medicina (Bacharelado)"),
	U8("[II] Medicina Veterin�ria (Bacharelado)"),
	U8("[I] Museologia (Bacharelado)"),
	U8("[I] M�sica (Bacharelado)"),
	U8("[I] M�sica (Licenciatura)"),
	U8("[II] Nutri��o (Bacharelado)"),
	U8("[II] Odontologia (Bacharelado)"),
	U8("[I] Pedagogia (Licenciatura)"),
	U8("[II] Psicologia (Bacharelado/Licenciatura/Psic�logo)"),
	U8("[II] Qu�mica (Bacharelado)"),
	U8("[II] Qu�mica Tecnol�gica (Bacharelado)"),
	U8("[I] Rela��es Internacionais (Bacharelado)"),
	U8("[I] Servi�o Social (Bacharelado)"),
	U8("[I] Turismo (Bacharelado)"),
	U8("[I] Administra��o (Bacharelado) (Noturno)"),
	U8("[I] Arquitetura e Urbanismo (Bacharelado) (Noturno)"),
	U8("[I] Arquivologia (Bacharelado) (Noturno)"),
	U8("[I] Artes Visuais (Licenciatura) (Noturno)"),
	U8("[I] Ci�ncias Ambientais (Bacharelado) (Noturno)"),
	U8("[I] Ci�ncias Cont�beis (Bacharelado) (Noturno)"),
	U8("[II] Computa��o (Licenciatura) (Noturno)"),
	U8("[I] Comunica��o Organizacional (Bacharelado) (Noturno)"),
	U8("[I] Direito (Bacharelado) (Noturno)"),
	U8("[II] Engenharia de Produ��o (Bacharelado) (Noturno)"),
	U8("[II] Farm�cia (Bacharelado) (Noturno)"),
	U8("[I] Filosofia (Licenciatura) (Noturno)"),
	U8("[I] Gest�o de Agroneg�cio (Bacharelado) (Noturno)"),
	U8("[I] Gest�o de Pol�ticas P�blicas (Bacharelado) (Noturno)"),
	U8("[I] Hist�ria (Licenciatura) (Noturno)"),
	U8("[I] Letras � Tradu��o Espanhol (Bacharelado) (Noturno)"),
	U8("[II] Licenciatura em Ci�ncias Biol�gicas (Noturno)"),
	U8("[II] Licenciatura em F�sica (Noturno)"),
	U8("[II] Licenciatura em Matem�tica (Noturno)"),
	U8("[I] Licenciatura em M�sica (Noturno)"),
	U8("[II] Licenciatura em Qu�mica (Noturno)"),
	U8("[I] L�ngua e Literatura Japonesa (Licenciatura) (Noturno)"),
	U8("[I] L�ngua Espanhola e Literatura Espanhola e Hispano-Americana (Licenciatura) (Noturno)"),
	U8("[I] L�ngua Portuguesa e Respectiva Literatura (Licenciatura) (Noturno)"),
	U8("[I] Pedagogia (Licenciatura) (Noturno)"),
	U8("[II] Sa�de Coletiva (Bacharelado) (Noturno)"),
	U8("[I] Servi�o Social (Bacharelado) (Noturno)"),
	U8("[I] Teoria, Cr�tica e Hist�ria da Arte (Bacharelado) (Noturno)"),
	U8("[II] Enfermagem (Bacharelado) (Ceil�ndia)"),
	U8("[II] Farm�cia (Bacharelado) (Ceil�ndia)"),
	U8("[II] Fisioterapia (Bacharelado) (Ceil�ndia)"),
	U8("[II] Fonoaudiologia (Bacharelado) (Ceil�ndia)"),
	U8("[II] Sa�de Coletiva (Bacharelado) (Ceil�ndia)"),
	U8("[II] Terapia Ocupacional (Bacharelado) (Ceil�ndia)"),
	U8("[II] Engenharias � Aeroespacial/Automotiva/Eletr�nica/Energia/Software (Bacharelados) (Gama)"),
	U8("[I] Ci�ncias Naturais (Licenciatura) (Planaltina)"),
	U8("[I] Gest�o do Agroneg�cio (Bacharelado) (Planaltina)"),
	U8("[I] Ci�ncias Naturais (Licenciatura) (Noturno) (Planaltina)"),
	U8("[I] Gest�o Ambiental (Bacharelado) (Noturno) (Planaltina)")
};