#include "texts.h"

// Ativar compatibilidade com unicode.
#define U8(_S) (const char*)u8##_S

const char* Texts::NW_TIP_MARKER_INITIAL = "Ver texto inicial";
const char* Texts::NW_TIP_MARKER_INFO = U8("Ver informações sobre o programa");

const char* Texts::SMALLER_TEXT_BOX_INITIAL = U8("Pesquise ou selecione um curso para começar");
const char* Texts::SMALLER_TEXT_BOX_INFO = U8("Informações sobre o programa");
const char* Texts::SMALLER_TEXT_BOX_NO_COURSE_SELECTED = U8("Erro: nenhum curso foi selecionado");
const char* Texts::SMALLER_TEXT_BOX_DOWNLOADING = "Baixando pdfs, aguarde...";
const char* Texts::SMALLER_TEXT_BOX_DOWNLOAD_FAILED = "Erro: falha ao baixar os pdfs, tente novamente";
const char* Texts::SMALLER_TEXT_BOX_RESULTS = "Resumo das notas abaixo";
const char* Texts::SMALLER_TEXT_BOX_DETAILS = U8("Inscrições, notas e posições detalhadas abaixo");
const char* Texts::SMALLER_TEXT_BOX_EXTRACT_FAILED = "Erro: falha ao extrair os dados dos pdfs, tente novamente";

const char* Texts::BUTTON_SEARCH = "Pesquisar";

const char* Texts::BIGGER_TEXT_BOX_INITIAL = U8("Olá, este programa mostra as notas dos candidatos aprovados na UnB pelo acesso Enem.\n\n")
	"Para começar, você pode escolher o curso desejado na lista de cursos disponíveis acima e clicar em pesquisar para checar as notas máximas"
	"(1º lugar), mínimas (nota de corte/último lugar) e também a média das notas, de acordo com cada cota que a universidade disponibiliza.\n\n"
	"Você pode escolher o ano que deseja checar e também a chamada, além de ser possível ver todas as notas, com o número de inscrição e"
	"respectivas posições do candidato no botão \"Ver Detalhes\"\n\n"
	"Caso queira dar zoom no texto você pode utilizar Ctrl + Scroll (rodinha do mouse/gesto de pinça no touchpad), com a setinha emcima desse"
	"texto aqui, além disso você pode abrir links e copiar os resultados pesquisados com clique direito do mouse/touchpad ou Ctrl + C para copiar\n\n"
	"Informações sobre o programa no 'i' no canto superior esquerdo.";
const char* Texts::BIGGER_TEXT_BOX_INFO = U8("Este programa não tem nenhuma afiliação com a Universidade de Brasília. Os dados utilizados estão")
	"disponíveis para o público no seguinte url: https://www.cebraspe.org.br/ [1]\n\n"
	"Criador : Yogi Nam de Souza Barbosa\n"
	"Github: https://github.com/euyogi/ [2]\n\n"
	"Este programa é meu projeto final do curso: CS50 - Introduction to Computer Science of Harvard University\n"
	"Disponível no seguinte url: https://pll.harvard.edu/course/cs50-introduction-computer-science/ [3]\n\n"
	"Feito em C++ com ImGui :)\n\n"
	"Caso tenha encontrado algum comportamento incorreto e queira colaborar reportando esse erro - (Necessário criar conta github)\n"
	"Reporte no seguinte url: https://github.com/euyogi/Projeto-CS50/issues/new/ [4]\n\n"
	"[Clique com o botão direito do mouse/touchpad para abrir qualquer um dos links]";

const char* Texts::BUTTON_COPY = "Copiar";
const char* Texts::BUTTON_OPEN1 = "Abrir [1]";
const char* Texts::BUTTON_OPEN2 = "Abrir [2]";
const char* Texts::BUTTON_OPEN3 = "Abrir [3]";
const char* Texts::BUTTON_OPEN4 = "Abrir [4]";

const char* Texts::SW_TIP_MARKER = U8("Escolha o ano e a chamada que você\n  quer checar as notas de corte");
const char* Texts::SE_BUTTON_DETAILS = "Ver Detalhes";
const char* Texts::SE_BUTTON_RESULTS = "Ver Resumo";
const char* Texts::BUTTON_EXIT = "Sair";

const char* Texts::LABEL_CONVERTER = "Converter Notas";
const char* Texts::NE1_TIP_MARKER = U8("A UnB possui diferentes pesos\npara cada área, de acordo com\n o grupo do curso, calcule a\n sua nota com os pesos aqui");
const char* Texts::LABEL_GROUP = "Grupo do Curso";
const char* Texts::NE2_TIP_MARKER = U8("Não sabe o grupo do seu curso?\nO grupo está na frente de cada\n\tcurso na lista ao lado");

const char* Texts::RADIO1 = "Grupo I";
const char* Texts::RADIO2 = "Grupo II";

const char* Texts::LABEL_GRADES = "Insira as Notas";
const char* Texts::LABEL_LITERATURE = "Linguagens";
const char* Texts::LABEL_HUMANITIES = "Humanas";
const char* Texts::LABEL_NATURE = "Natureza";
const char* Texts::LABEL_MATH = U8("Matemática");
const char* Texts::LABEL_ESSAY = U8("Redação");

const char* Texts::BUTTON_CONVERT = "Converter";

const char* Texts::COURSES[101] = {
	U8("[I] Administração (Bacharelado)"),
	U8("[II] Agronomia (Bacharelado)"),
	U8("[I] Arquitetura e Urbanismo (Bacharelado)"),
	U8("[I] Artes Cênicas - Interpretação Teatral (Bacharelado)"),
	U8("[I] Artes Visuais (Bacharelado)"),
	U8("[I] Artes Visuais (Licenciatura)"),
	U8("[I] Biblioteconomia (Bacharelado)"),
	U8("[II] Biotecnologia (Bacharelado)"),
	U8("[II] Ciência da Computação (Bacharelado)"),
	U8("[I] Ciência Política (Bacharelado)"),
	U8("[II] Ciências Biológicas (Bacharelado)"),
	U8("[I] Ciências Contábeis (Bacharelado)"),
	U8("[I] Ciências Econômicas (Bacharelado)"),
	U8("[I] Ciências Sociais – Antropologia/Sociologia (Bacharelado/Licenciatura)"),
	U8("[I] Comunicação Social – Audiovisual (Bacharelado)"),
	U8("[I] Comunicação Social – Publicidade e Propaganda (Bacharelado)"),
	U8("[I] Design – Programação Visual/Projeto do Produto (Bacharelado)"),
	U8("[I] Direito (Bacharelado)"),
	U8("[II] Educação Física (Bacharelado)"),
	U8("[II] Educação Física (Licenciatura)"),
	U8("[II] Enfermagem (Bacharelado)"),
	U8("[II] Engenharia Ambiental (Bacharelado)"),
	U8("[II] Engenharia Civil (Bacharelado)"),
	U8("[II] Engenharia de Computação (Bacharelado)"),
	U8("[II] Engenharia de Redes de Comunicação (Bacharelado)"),
	U8("[II] Engenharia Elétrica (Bacharelado)"),
	U8("[II] Engenharia Florestal (Bacharelado)"),
	U8("[II] Engenharia Mecânica (Bacharelado)"),
	U8("[II] Engenharia Mecatrônica – Controle e Automação (Bacharelado)"),
	U8("[II] Engenharia Química (Bacharelado)"),
	U8("[II] Estatística (Bacharelado)"),
	U8("[II] Farmácia (Bacharelado)"),
	U8("[I] Filosofia (Bacharelado/Licenciatura)"),
	U8("[II] Física (Bacharelado)"),
	U8("[II] Geofísica (Bacharelado)"),
	U8("[I] Geografia (Bacharelado/Licenciatura)"),
	U8("[II] Geologia (Bacharelado)"),
	U8("[I] História (Bacharelado/Licenciatura)"),
	U8("[I] Jornalismo (Bacharelado)"),
	U8("[I] Letras – Português do Brasil como Segunda Língua (Licenciatura)"),
	U8("[I] Letras – Tradução – Francês (Bacharelado)"),
	U8("[I] Letras – Tradução – Inglês (Bacharelado)"),
	U8("[I] Licenciatura em Artes Cênicas"),
	U8("[I] Língua Estrangeira Aplicada – Multilinguismo e Sociedade da Informação (Bacharelado)"),
	U8("[I] Língua Francesa e Respectiva Literatura (Bacharelado/Licenciatura)"),
	U8("[I] Língua Inglesa e Respectiva Literatura (Bacharelado/Licenciatura)"),
	U8("[I] Língua Portuguesa e Respectiva Literatura (Bacharelado/Licenciatura)"),
	U8("[II] Matemática (Bacharelado/Licenciatura)"),
	U8("[II] Medicina (Bacharelado)"),
	U8("[II] Medicina Veterinária (Bacharelado)"),
	U8("[I] Museologia (Bacharelado)"),
	U8("[I] Música (Bacharelado)"),
	U8("[I] Música (Licenciatura)"),
	U8("[II] Nutrição (Bacharelado)"),
	U8("[II] Odontologia (Bacharelado)"),
	U8("[I] Pedagogia (Licenciatura)"),
	U8("[II] Psicologia (Bacharelado/Licenciatura/Psicólogo)"),
	U8("[II] Química (Bacharelado)"),
	U8("[II] Química Tecnológica (Bacharelado)"),
	U8("[I] Relações Internacionais (Bacharelado)"),
	U8("[I] Serviço Social (Bacharelado)"),
	U8("[I] Turismo (Bacharelado)"),
	U8("[I] Administração (Bacharelado) (Noturno)"),
	U8("[I] Arquitetura e Urbanismo (Bacharelado) (Noturno)"),
	U8("[I] Arquivologia (Bacharelado) (Noturno)"),
	U8("[I] Artes Visuais (Licenciatura) (Noturno)"),
	U8("[I] Ciências Ambientais (Bacharelado) (Noturno)"),
	U8("[I] Ciências Contábeis (Bacharelado) (Noturno)"),
	U8("[II] Computação (Licenciatura) (Noturno)"),
	U8("[I] Comunicação Organizacional (Bacharelado) (Noturno)"),
	U8("[I] Direito (Bacharelado) (Noturno)"),
	U8("[II] Engenharia de Produção (Bacharelado) (Noturno)"),
	U8("[II] Farmácia (Bacharelado) (Noturno)"),
	U8("[I] Filosofia (Licenciatura) (Noturno)"),
	U8("[I] Gestão de Agronegócio (Bacharelado) (Noturno)"),
	U8("[I] Gestão de Políticas Públicas (Bacharelado) (Noturno)"),
	U8("[I] História (Licenciatura) (Noturno)"),
	U8("[I] Letras – Tradução Espanhol (Bacharelado) (Noturno)"),
	U8("[II] Licenciatura em Ciências Biológicas (Noturno)"),
	U8("[II] Licenciatura em Física (Noturno)"),
	U8("[II] Licenciatura em Matemática (Noturno)"),
	U8("[I] Licenciatura em Música (Noturno)"),
	U8("[II] Licenciatura em Química (Noturno)"),
	U8("[I] Língua e Literatura Japonesa (Licenciatura) (Noturno)"),
	U8("[I] Língua Espanhola e Literatura Espanhola e Hispano-Americana (Licenciatura) (Noturno)"),
	U8("[I] Língua Portuguesa e Respectiva Literatura (Licenciatura) (Noturno)"),
	U8("[I] Pedagogia (Licenciatura) (Noturno)"),
	U8("[II] Saúde Coletiva (Bacharelado) (Noturno)"),
	U8("[I] Serviço Social (Bacharelado) (Noturno)"),
	U8("[I] Teoria, Crítica e História da Arte (Bacharelado) (Noturno)"),
	U8("[II] Enfermagem (Bacharelado) (Ceilândia)"),
	U8("[II] Farmácia (Bacharelado) (Ceilândia)"),
	U8("[II] Fisioterapia (Bacharelado) (Ceilândia)"),
	U8("[II] Fonoaudiologia (Bacharelado) (Ceilândia)"),
	U8("[II] Saúde Coletiva (Bacharelado) (Ceilândia)"),
	U8("[II] Terapia Ocupacional (Bacharelado) (Ceilândia)"),
	U8("[II] Engenharias – Aeroespacial/Automotiva/Eletrônica/Energia/Software (Bacharelados) (Gama)"),
	U8("[I] Ciências Naturais (Licenciatura) (Planaltina)"),
	U8("[I] Gestão do Agronegócio (Bacharelado) (Planaltina)"),
	U8("[I] Ciências Naturais (Licenciatura) (Noturno) (Planaltina)"),
	U8("[I] Gestão Ambiental (Bacharelado) (Noturno) (Planaltina)")
};