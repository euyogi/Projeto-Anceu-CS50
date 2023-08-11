#include "texts.h"

const char* Texts::NW_TIP_MARKER_INITIAL = "Ver texto inicial";
const char* Texts::NW_TIP_MARKER_INFO = "Ver informações sobre o programa";

const char* Texts::SMALLER_TEXT_BOX_INITIAL = "Pesquise ou selecione um curso para começar";
const char* Texts::SMALLER_TEXT_BOX_INFO = "Informações sobre o programa";
const char* Texts::SMALLER_TEXT_BOX_NO_COURSE_SELECTED = "Erro: nenhum curso foi selecionado";
const char* Texts::SMALLER_TEXT_BOX_DOWNLOADING = "Baixando pdfs, aguarde...";
const char* Texts::SMALLER_TEXT_BOX_DOWNLOAD_FAILED = "Erro: falha ao baixar os pdfs, tente novamente";
const char* Texts::SMALLER_TEXT_BOX_RESULTS = "Resumo das notas abaixo";
const char* Texts::SMALLER_TEXT_BOX_DETAILS = "Inscrições, notas e posições detalhadas abaixo";
const char* Texts::SMALLER_TEXT_BOX_EXTRACT_FAILED = "Erro: falha ao extrair os dados dos pdfs, tente novamente";

const char* Texts::BUTTON_SEARCH = "Pesquisar";

const char* Texts::BIGGER_TEXT_BOX_INITIAL = "Olá, este programa mostra as notas dos candidatos aprovados na UnB pelo acesso Enem.\n\n"
	"Para começar, você pode escolher o curso desejado na lista de cursos disponíveis acima e clicar em pesquisar para checar as notas máximas "
	"(1º lugar), mínimas (nota de corte/último lugar) e também a média das notas, de acordo com cada cota que a universidade disponibiliza.\n\n"
	"Você pode escolher o ano que deseja checar e também a chamada, além de ser possível ver todas as notas, com o número de inscrição e "
	"respectivas posições do candidato no botão \"Ver Detalhes\"\n\n"
	"Caso queira dar zoom no texto você pode utilizar Ctrl + Scroll (rodinha do mouse/gesto de pinça no touchpad), com a setinha emcima desse "
	"texto aqui, além disso você pode abrir links e copiar os resultados pesquisados com clique direito do mouse/touchpad ou Ctrl + C para copiar\n\n"
	"Informações sobre o programa no 'i' no canto superior esquerdo.";
const char* Texts::BIGGER_TEXT_BOX_INFO = "Este programa não tem nenhuma afiliação com a Universidade de Brasília. Os dados utilizados estão"
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
const char* Texts::SMALLER_TEXT_BOX_COPIED = "Copiado com sucesso";
const char* Texts::BUTTON_OPEN1 = "Abrir [1]";
const char* Texts::BUTTON_OPEN2 = "Abrir [2]";
const char* Texts::BUTTON_OPEN3 = "Abrir [3]";
const char* Texts::BUTTON_OPEN4 = "Abrir [4]";

const char* Texts::SW_TIP_MARKER = "Escolha o ano e a chamada que você\n  quer checar as notas de corte";
const char* Texts::SE_BUTTON_DETAILS = "Ver Detalhes";
const char* Texts::SE_BUTTON_RESULTS = "Ver Resumo";
const char* Texts::BUTTON_EXIT = "Sair";

const char* Texts::LABEL_CONVERTER = "Converter Notas";
const char* Texts::NE1_TIP_MARKER = "A UnB possui diferentes pesos\npara cada área, de acordo com\n o grupo do curso, calcule a\n sua nota com os pesos aqui";
const char* Texts::LABEL_GROUP = "Grupo do Curso";
const char* Texts::NE2_TIP_MARKER = "Não sabe o grupo do seu curso?\nO grupo está na frente de cada\n\tcurso na lista ao lado";

const char* Texts::RADIO1 = "Grupo I";
const char* Texts::RADIO2 = "Grupo II";

const char* Texts::LABEL_GRADES = "Insira as Notas";
const char* Texts::LABEL_LITERATURE = "Linguagens";
const char* Texts::LABEL_HUMANITIES = "Humanas";
const char* Texts::LABEL_NATURE = "Natureza";
const char* Texts::LABEL_MATH = "Matemática";
const char* Texts::LABEL_ESSAY = "Redação";

const char* Texts::BUTTON_CONVERT = "Converter";
const char* Texts::LABEL_FINAL = "Final";

const char* Texts::QUOTAS_NAMES[10] = {
		"Sistema Universal:", "Cotas para Negros:",
		"Rnd ≤ 1,5 PPI:\t", "Rnd ≤ 1,5 PPI PCD:", "Rnd ≤ 1,5:\t\t", "Rnd ≤ 1,5 PCD:\t",
		"Rnd > 1,5 PPI:\t", "Rnd > 1,5 PPI PCD:", "Rnd > 1,5:\t\t", "Rnd > 1,5 PCD:\t"
};

const char* Texts::COURSES[101] = {
	"[I] Administração (Bacharelado)",
	"[II] Agronomia (Bacharelado)",
	"[I] Arquitetura e Urbanismo (Bacharelado)",
	"[I] Artes Cênicas - Interpretação Teatral (Bacharelado)",
	"[I] Artes Visuais (Bacharelado)",
	"[I] Artes Visuais (Licenciatura)",
	"[I] Biblioteconomia (Bacharelado)",
	"[II] Biotecnologia (Bacharelado)",
	"[II] Ciência da Computação (Bacharelado)",
	"[I] Ciência Política (Bacharelado)",
	"[II] Ciências Biológicas (Bacharelado)",
	"[I] Ciências Contábeis (Bacharelado)",
	"[I] Ciências Econômicas (Bacharelado)",
	"[I] Ciências Sociais – Antropologia/Sociologia (Bacharelado/Licenciatura)",
	"[I] Comunicação Social – Audiovisual (Bacharelado)",
	"[I] Comunicação Social – Publicidade e Propaganda (Bacharelado)",
	"[I] Design – Programação Visual/Projeto do Produto (Bacharelado)",
	"[I] Direito (Bacharelado)",
	"[II] Educação Física (Bacharelado)",
	"[II] Educação Física (Licenciatura)",
	"[II] Enfermagem (Bacharelado)",
	"[II] Engenharia Ambiental (Bacharelado)",
	"[II] Engenharia Civil (Bacharelado)",
	"[II] Engenharia de Computação (Bacharelado)",
	"[II] Engenharia de Redes de Comunicação (Bacharelado)",
	"[II] Engenharia Elétrica (Bacharelado)",
	"[II] Engenharia Florestal (Bacharelado)",
	"[II] Engenharia Mecânica (Bacharelado)",
	"[II] Engenharia Mecatrônica – Controle e Automação (Bacharelado)",
	"[II] Engenharia Química (Bacharelado)",
	"[II] Estatística (Bacharelado)",
	"[II] Farmácia (Bacharelado)",
	"[I] Filosofia (Bacharelado/Licenciatura)",
	"[II] Física (Bacharelado)",
	"[II] Geofísica (Bacharelado)",
	"[I] Geografia (Bacharelado/Licenciatura)",
	"[II] Geologia (Bacharelado)",
	"[I] História (Bacharelado/Licenciatura)",
	"[I] Jornalismo (Bacharelado)",
	"[I] Letras – Português do Brasil como Segunda Língua (Licenciatura)",
	"[I] Letras – Tradução – Francês (Bacharelado)",
	"[I] Letras – Tradução – Inglês (Bacharelado)",
	"[I] Licenciatura em Artes Cênicas",
	"[I] Língua Estrangeira Aplicada – Multilinguismo e Sociedade da Informação (Bacharelado)",
	"[I] Língua Francesa e Respectiva Literatura (Bacharelado/Licenciatura)",
	"[I] Língua Inglesa e Respectiva Literatura (Bacharelado/Licenciatura)",
	"[I] Língua Portuguesa e Respectiva Literatura (Bacharelado/Licenciatura)",
	"[II] Matemática (Bacharelado/Licenciatura)",
	"[II] Medicina (Bacharelado)",
	"[II] Medicina Veterinária (Bacharelado)",
	"[I] Museologia (Bacharelado)",
	"[I] Música (Bacharelado)",
	"[I] Música (Licenciatura)",
	"[II] Nutrição (Bacharelado)",
	"[II] Odontologia (Bacharelado)",
	"[I] Pedagogia (Licenciatura)",
	"[II] Psicologia (Bacharelado/Licenciatura/Psicólogo)",
	"[II] Química (Bacharelado)",
	"[II] Química Tecnológica (Bacharelado)",
	"[I] Relações Internacionais (Bacharelado)",
	"[I] Serviço Social (Bacharelado)",
	"[I] Turismo (Bacharelado)",
	"[I] Administração (Bacharelado) (Noturno)",
	"[I] Arquitetura e Urbanismo (Bacharelado) (Noturno)",
	"[I] Arquivologia (Bacharelado) (Noturno)",
	"[I] Artes Visuais (Licenciatura) (Noturno)",
	"[I] Ciências Ambientais (Bacharelado) (Noturno)",
	"[I] Ciências Contábeis (Bacharelado) (Noturno)",
	"[II] Computação (Licenciatura) (Noturno)",
	"[I] Comunicação Organizacional (Bacharelado) (Noturno)",
	"[I] Direito (Bacharelado) (Noturno)",
	"[II] Engenharia de Produção (Bacharelado) (Noturno)",
	"[II] Farmácia (Bacharelado) (Noturno)",
	"[I] Filosofia (Licenciatura) (Noturno)",
	"[I] Gestão de Agronegócio (Bacharelado) (Noturno)",
	"[I] Gestão de Políticas Públicas (Bacharelado) (Noturno)",
	"[I] História (Licenciatura) (Noturno)",
	"[I] Letras – Tradução Espanhol (Bacharelado) (Noturno)",
	"[II] Licenciatura em Ciências Biológicas (Noturno)",
	"[II] Licenciatura em Física (Noturno)",
	"[II] Licenciatura em Matemática (Noturno)",
	"[I] Licenciatura em Música (Noturno)",
	"[II] Licenciatura em Química (Noturno)",
	"[I] Língua e Literatura Japonesa (Licenciatura) (Noturno)",
	"[I] Língua Espanhola e Literatura Espanhola e Hispano-Americana (Licenciatura) (Noturno)",
	"[I] Língua Portuguesa e Respectiva Literatura (Licenciatura) (Noturno)",
	"[I] Pedagogia (Licenciatura) (Noturno)",
	"[II] Saúde Coletiva (Bacharelado) (Noturno)",
	"[I] Serviço Social (Bacharelado) (Noturno)",
	"[I] Teoria, Crítica e História da Arte (Bacharelado) (Noturno)",
	"[II] Enfermagem (Bacharelado) (Ceilândia)",
	"[II] Farmácia (Bacharelado) (Ceilândia)",
	"[II] Fisioterapia (Bacharelado) (Ceilândia)",
	"[II] Fonoaudiologia (Bacharelado) (Ceilândia)",
	"[II] Saúde Coletiva (Bacharelado) (Ceilândia)",
	"[II] Terapia Ocupacional (Bacharelado) (Ceilândia)",
	"[II] Engenharias – Aeroespacial/Automotiva/Eletrônica/Energia/Software (Bacharelados) (Gama)",
	"[I] Ciências Naturais (Licenciatura) (Planaltina)",
	"[I] Gestão do Agronegócio (Bacharelado) (Planaltina)",
	"[I] Ciências Naturais (Licenciatura) (Noturno) (Planaltina)",
	"[I] Gestão Ambiental (Bacharelado) (Noturno) (Planaltina)"
};
