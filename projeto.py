''' 
< BUG Resolução estranha na tela do notebook? >

Esse é o meu projeto final para o curso CS50 - é um aplicativo feito em python,
que checa as notas dos candidatos que participaram do Enem e se inscreveram na
Universidade Nacional de Brasília - UNB, mostrando por fim um resumo para cada
curso da instituição, com as maiores notas, as menores notas (nota de corte), e
a média em cada cota disponível.

É possível calcular também a sua própria nota, já que a universidade possui um
sistema de pesos para as notas de cada área.

Necessário instalar customtkinter, numpy, Pmw, pygame e requests com pip install
caso ainda não tenha-os instalados.

Além do click_sound.wav e do pdftotext.exe disponíveis no meu github, junto com o
arquivo desse código.
'''

# O código tá na ordem: (Bibliotecas / Variáveis / UI / Funções)


''' Bibliotecas e módulos necessários para o programa. '''

# Para a UI
import customtkinter as ctk  

 # Similar ao range(), mas mais rápido.
from numpy import arange 

 # Para ordenar uma lista de sublistas com base em um valor em uma dessas sublistas.
from operator import itemgetter 

 # Para remover os PDFs.
from os import remove 

  # Para mostrar os balões quando o cursor está emcima dos "?".
from Pmw import Balloon

 # Para reproduzir sons de clique.
from pygame import mixer 

 # Similar a .find() ou .replace(), mas com padrões mais complexos de substrings.
from re import findall, search, sub 

 # Para baixar os PDFs.
from requests import get, exceptions 

 # Para calcular média dos valores em uma lista.
from statistics import mean 

# Para converter os PDFs.
import subprocess  

# Executa algumas partes do programa em outro thread, evitando da UI travar.
from threading import Thread  

 # Para, ao fechar a UI dar tempo de reproduzir o som de clique.
from time import sleep, time


''' Variáveis para armazenar dados necessários para as funções. '''

# Links dos PDFs que contém dados dos candidatos; NOTAS possui as notas de todos os candidatos; APROVADOS as inscrições dos aprovados.
URL_DAS_NOTAS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_6_ACESSOENEM_22_RES_FINAL_BIOP_SCEP_E_NO_PROCESSO.PDF'
URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ACESSOENEM_22_ED_9_RES_FINAL_RA_1_CHAMADA.PDF'

# Nomes dos arquivos; Pode ser qualquer nome pois só existem enquanto o programa está rodando.
NOME_PDF = 'dados.pdf'
NOME_PDF2 = 'dados_2.pdf'

# Lista com cada cota em sua versão resumida.
SIMBOLO_COTAS = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10']

# Lista com cada cota em sua versão normal.
NOMES_DAS_COTAS = [
    'Sistema Universal',
    'Cotas para Negros',
    'PPI   ≤   1,5    ',
    'PPI   ≤ 1,5 D    ',
    'Ñ PPI ≤   1,5    ',
    'Ñ PPI ≤ 1,5 D    ',
    'PPI   ≥   1,5    ',
    'PPI   ≥ 1,5 D    ',
    'Ñ PPI ≥   1,5    ',
    'Ñ PPI ≥ 1,5 D    ']

# As inscrições tem 8 dígitos e começam com '100'; Útil para achar o início dos dados de cada candidato.
INICIO_INSCRICAO = '100'

# Lista com cada curso; Para ter os nomes dos cursos na menu_cursos a partir do início do programa.
NOMES_DOS_CURSOS = sorted([
    'ADMINISTRAÇÃO', 'AGRONOMIA', 'ARQUITETURA E URBANISMO', 'ARTES CÊNICAS - INTERPRETAÇÃO TEATRAL', 'ARTES VISUAIS', 'ARTES VISUAIS (LICENCIATURA)',
    'BIBLIOTECONOMIA', 'BIOTECNOLOGIA', 'CIÊNCIA DA COMPUTAÇÃO', 'CIÊNCIA POLÍTICA', 'CIÊNCIAS BIOLÓGICAS', 'CIÊNCIAS CONTÁBEIS', 'CIÊNCIAS ECONÔMICAS',
    'ANTROPOLOGIA/SOCIOLOGIA (BACHARELADO/LICENCIATURA)', 'AUDIOVISUAL', 'PUBLICIDADE E PROPAGANDA', 'DESIGN', 'DIREITO', 'EDUCAÇÃO FÍSICA',
    'EDUCAÇÃO FÍSICA (LICENCIATURA)', 'ENGENHARIA AMBIENTAL', 'ENGENHARIA CIVIL', 'ENGENHARIA DE COMPUTAÇÃO', 'ENGENHARIA DE REDES DE COMUNICAÇÃO',
    'ENGENHARIA ELÉTRICA', 'ENGENHARIA FLORESTAL', 'ENGENHARIA MECÂNICA', 'ENGENHARIA MECATRÔNICA', 'ENGENHARIA QUÍMICA', 'ESTATÍSTICA', 'FARMÁCIA',
    'FILOSOFIA (BACHARELADO/LICENCIATURA)', 'FÍSICA', 'GEOFÍSICA', 'GEOGRAFIA (BACHARELADO/LICENCIATURA)', 'GEOLOGIA', 'HISTÓRIA (BACHARELADO/LICENCIATURA)',
    'JORNALISMO', 'LETRAS – PORTUGUÊS DO BRASIL COMO SEGUNDA LÍNGUA (LICENCIATURA)', 'LETRAS – TRADUÇÂO – FRANCÊS', 'LETRAS – TRADUÇÃO – INGLÊS',
    'LICENCIATURA EM ARTES CÊNICAS', 'LÍNGUA ESTRANGEIRA APLICADA', 'LÍNGUA FRANCESA E RESPECTIVA LITERATURA (BACHARELADO/LICENCIATURA)',
    'LÍNGUA INGLESA E RESPECTIVA LITERATURA (BACHARELADO/LICENCIATURA)', 'MATEMÁTICA (BACHARELADO/LICENCIATURA)', 'MEDICINA', 'MUSEOLOGIA', 'MÚSICA',
    'MÚSICA (LICENCIATURA)', 'NUTRIÇÃO', 'ODONTOLOGIA', 'PEDAGOGIA (LICENCIATURA)', 'PSICOLOGIA (BACHARELADO/LICENCIATURA/PSICÓLOGO)', 'QUÍMICA',
    'QUÍMICA TECNOLÓGICA', 'SERVIÇO SOCIAL', 'TURISMO', 'ADMINISTRAÇÃO (NOTURNO)', 'ARQUITETURA E URBANISMO (NOTURNO)', 'ARQUIVOLOGIA (NOTURNO)',
    'ARTES VISUAIS (LICENCIATURA) (NOTURNO)', 'CIÊNCIAS AMBIENTAIS (NOTURNO)', 'CIÊNCIAS CONTÁBEIS (NOTURNO)', 'COMPUTAÇÃO (LICENCIATURA) (NOTURNO)',
    'COMUNICAÇÃO ORGANIZACIONAL (NOTURNO)', 'DIREITO (NOTURNO)', 'ENGENHARIA DE PRODUÇÃO (NOTURNO)', 'FARMÁCIA (NOTURNO)', 'FILOSOFIA (LICENCIATURA) (NOTURNO)',
    'GESTÃO DE AGRONEGÓCIO (NOTURNO)', 'GESTÃO DE POLÍTICAS PÚBLICAS (NOTURNO)', 'HISTÓRIA (LICENCIATURA) (NOTURNO)', 'LETRAS – TRADUÇÃO ESPANHOL (NOTURNO)',
    'LICENCIATURA EM CIÊNCIAS BIOLÓGICAS (NOTURNO)', 'LICENCIATURA EM FÍSICA (NOTURNO)', 'LICENCIATURA EM MATEMÁTICA (NOTURNO)', 'LICENCIATURA EM MÚSICA (NOTURNO)',
    'LICENCIATURA EM QUÍMICA (NOTURNO)', 'LÍNGUA E LITERATURA JAPONESA (LICENCIATURA) (NOTURNO)', 'LÍNGUA ESPANHOLA E LITERATURA ESPANHOLA E HISPANO–AMERICANA (LICENCIATURA) (NOTURNO)',
    'LÍNGUA PORTUGUESA E RESPECTIVA LITERATURA (LICENCIATURA) (NOTURNO)', 'PEDAGOGIA (LICENCIATURA) (NOTURNO)', 'SAÚDE COLETIVA (NOTURNO)', 'SERVIÇO SOCIAL (NOTURNO)',
    'TEORIA, CRÍTICA E HISTÓRIA DA ARTE (NOTURNO)', 'ENFERMAGEM (CEILÂNDIA)', 'FARMÁCIA (CEILÂNDIA)', 'FISIOTERAPIA (CEILÂNDIA)', 'FONOAUDIOLOGIA (CEILÂNDIA)',
    'SAÚDE COLETIVA (CEILÂNDIA)', 'TERAPIA OCUPACIONAL (CEILÂNDIA)', 'ENGENHARIAS – AEROESPACIAL/AUTOMOTIVA/ELETRÔNICA/ENERGIA/SOFTWARE (GAMA)',
    'CIÊNCIAS NATURAIS (LICENCIATURA) (PLANALTINA)', 'GESTÃO DO AGRONEGÓCIO (PLANALTINA)', 'CIÊNCIAS NATURAIS (LICENCIATURA) (PLANALTINA) (NOTURNO)',
    'GESTÃO AMBIENTAL (PLANALTINA) (NOTURNO)', 'MEDICINA (BACHARELADO) – SUB JUDICE'])

# Cores para textos e botões.
AZUL = '#4169E1'
CINZA = '#C0C0C0'
CINZA_ESCURO = '#9E9E9E'
CINZA_VERMELHADO = '#393333'
CINZA_ESCURO_VERMELHADO = '#2C2121'
VERDE = '#83F28F'
VERMELHO_CLARO = '#D9381E'
VERMELHO = '#A5361F'
VERMELHO_ESCURO = '#521B0F'
ROXO = '#502B29'
ROXO_ESCURO = '#2C1B1A'
ROXO_MAIS_ESCURO = '#271717'

# Nesse dicionário é armazenado 10 listas com as notas de cada candidato que se candidatou por cada uma das 10 cotas.
cotas_notas = {s: list() for s in SIMBOLO_COTAS}

# Para guardar o nome do curso , ano e chamada que foi pesquisada;
# Evita um bug em que poderia mostrar o nome do curso, o ano, ou a chamada nos resultados, mesmo sem ter pesquisado.
curso = ano = chamada = str()

# Todos os dados dos candidatos do curso escolhido vão ser armazenados nessa string, mas depois ela vai ser dividida em listas com sublistas.
dados = str()

# Lista com as inscrições de todos os candidatos que foram aprovados na universidade.
inscricoes_aprovados = list()

# Declara os elementos da UI que são utilizados por outras funções.
window = ctk.CTk()

frame_esquerdo = ctk.CTkFrame(master = window)

menu_filtros = ctk.CTkOptionMenu(master = frame_esquerdo)
menu_cursos = ctk.CTkComboBox(master = frame_esquerdo)
rotulo_status = ctk.CTkLabel(master = frame_esquerdo)
barra_progresso = ctk.CTkProgressBar(master = frame_esquerdo)
rotulo_resultado = ctk.CTkTextbox(master = frame_esquerdo)
opcoes_anos = ctk.CTkSegmentedButton(master = frame_esquerdo)
menu_chamadas = ctk.CTkOptionMenu(master = frame_esquerdo)
botao_detalhes = ctk.CTkButton(master = frame_esquerdo)

frame_direito = ctk.CTkFrame(master = window)

grupo_var = ctk.IntVar(value = 1)
nota_1 = ctk.CTkEntry(master = frame_direito)
nota_2 = ctk.CTkEntry(master = frame_direito)
nota_3 = ctk.CTkEntry(master = frame_direito)
nota_4 = ctk.CTkEntry(master = frame_direito)
nota_5 = ctk.CTkEntry(master = frame_direito)
nota_6 = ctk.CTkLabel(master = frame_direito)


def UI() -> None:
    # Declara como global os elementos da UI que precisam ser alterados, pois são utilizados por outras funções.
    global menu_filtros, menu_cursos, rotulo_status, barra_progresso, rotulo_resultado, opcoes_anos
    global menu_chamadas, botao_detalhes, grupo_var, nota_1, nota_2, nota_3, nota_4, nota_5, nota_6

    # A UI está sempre no modo escuro, pois assim a borda da janela não fica branca.
    ctk.set_appearance_mode('Dark')

    # Para deixar a UI em um tamanho que achei bom.
    ctk.set_widget_scaling(0.8)

    # Declara a janela principal, insere o título e sua resolução que é travada.
    window = ctk.CTk(fg_color = ROXO_ESCURO)
    window.title('Notas - Acesso ENEM UNB')
    window.geometry('1010x580')
    window.resizable(False, False)

    # Constantes para fonte , altura dos widgets e raio da borda.
    FONTE = ctk.CTkFont(family = 'Cascadia Code', size = 20)
    FONTE_MENOR = ctk.CTkFont(family = 'Cascadia Code', size = 18)
    ALTURA = 50
    RAIO = 8

    frame_esquerdo = ctk.CTkFrame(master = window, corner_radius = 12, fg_color = CINZA_ESCURO_VERMELHADO)
    frame_esquerdo.pack(side = 'left', pady = (0, 30), padx = (30, 15))

    botao_i = ctk.CTkButton(master = frame_esquerdo, width = 27, height = 15,
                            font = ('',15,'bold'), text_color = CINZA_ESCURO,
                            fg_color = 'transparent', border_color = CINZA_VERMELHADO,
                            border_width = 2, hover_color = ROXO, text = 'i',
                            command = lambda: [som_clique(), ver_info()])
    botao_i.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'nw')
    balao(botao_i, 'Ver informações sobre o\n'
                   'programa')

    menu_filtros = ctk.CTkOptionMenu(master = frame_esquerdo,
                                     dynamic_resizing = False,
                                     font = FONTE,
                                     dropdown_font = FONTE,
                                     fg_color = ROXO,
                                     button_color = ROXO_ESCURO,
                                     button_hover_color = ROXO_MAIS_ESCURO,
                                      dropdown_fg_color = ROXO_ESCURO,
                                     dropdown_hover_color = ROXO_MAIS_ESCURO,
                                     corner_radius = RAIO,
                                     height = ALTURA,
                                     text_color = CINZA,
                                     values = ['TODOS', 'BACHARELADOS', 'LICENCIATURAS', 'NOTURNOS', 'CEILÂNDIA', 'GAMA', 'PLANALTINA'],
                                     command = mudar_opcoes_menu_cursos)
    menu_filtros.grid(row = 0, column = 0, pady = (30, 0), padx = (65, 0), sticky = 'w')
    menu_filtros.set('TODOS')

    menu_cursos = ctk.CTkComboBox(master = frame_esquerdo,
                                  font = FONTE,
                                  dropdown_font = FONTE,
                                  border_color = ROXO,
                                  fg_color = ROXO,
                                  button_color = ROXO_ESCURO,
                                  button_hover_color = ROXO_MAIS_ESCURO,
                                  dropdown_fg_color = ROXO_ESCURO,
                                  dropdown_hover_color = ROXO_MAIS_ESCURO,
                                  corner_radius = RAIO,
                                  height = ALTURA,
                                  width = 400,
                                  text_color = CINZA,
                                  values = NOMES_DOS_CURSOS,
                                  command = som_clique)
    menu_cursos.grid(row = 0, column = 0, columnspan = 3, pady = (30, 0), padx = (220), sticky = 'we')
    menu_cursos.set('Cursos')

    botao_pesquisar = ctk.CTkButton(master = frame_esquerdo,
                                    font = FONTE,
                                    height = ALTURA,
                                    fg_color = ROXO,
                                    hover_color = ROXO_ESCURO,
                                    corner_radius = RAIO,
                                    text = 'Pesquisar',
                                    text_color = CINZA,
                                    command = lambda: [som_clique(), Thread(target = iniciar_pesquisa).start()])
    botao_pesquisar.grid(row = 0, column = 2, pady = (30, 0), padx = (0, 65), sticky = 'e')

    rotulo_status = ctk.CTkLabel(master = frame_esquerdo, corner_radius = RAIO, fg_color = CINZA_VERMELHADO,
                                 font = FONTE, height = ALTURA, anchor = 'w')
    rotulo_status.grid(row = 1, column = 0, columnspan = 3, pady = (25, 0), padx = 50, sticky = 'nsew')
    mudar_status('Status: Insira ou selecione um curso para começar')

    barra_progresso = ctk.CTkProgressBar(master = frame_esquerdo, fg_color = CINZA_VERMELHADO, progress_color = ROXO,
                                         height = 10, mode = 'determinate')
    barra_progresso.grid(row = 2, column = 0, columnspan = 3, pady = (15, 0), padx = 200, sticky = 'nsew')
    barra_progresso.set(1)

    rotulo_resultado = ctk.CTkTextbox(master = frame_esquerdo, fg_color = CINZA_VERMELHADO, text_color = CINZA,
                                      font = FONTE, corner_radius = RAIO, height = 400, state = 'disabled')
    rotulo_resultado.grid(row = 3, column = 0, columnspan = 3, pady = (15, 25), padx = 32, sticky='nsew')

    opcoes_anos = ctk.CTkSegmentedButton(master = frame_esquerdo,
                                         font = FONTE,
                                         height = ALTURA,
                                         width = 350,
                                         fg_color = CINZA_VERMELHADO,
                                         selected_color = ROXO,
                                         selected_hover_color =ROXO_ESCURO,
                                         corner_radius = RAIO,
                                         values = [' 2022 ', ' 2021 ', '2020_2', '2020_1'],
                                         dynamic_resizing = False,
                                         text_color = CINZA,
                                         command = mudar_ano_e_chamada)
    opcoes_anos.grid(row = 4, column = 0, pady = (0, 30), padx = (50, 0))
    opcoes_anos.set(' 2022 ')

    info_opcoes_anos = ctk.CTkButton(master = frame_esquerdo, width = 27, height = 15,
                                     font = ('',15,'bold'),
                                     fg_color = 'transparent', border_color = CINZA_VERMELHADO,
                                     border_width = 2, hover_color = ROXO, text = '?',
                                     state = 'disabled')
    info_opcoes_anos.grid(row = 4, column = 0, padx = 10, pady = (0, 29), sticky = 'w')

    balao(info_opcoes_anos, 'Você pode mudar a data das edições do\n'
                            'Acesso ENEM e a chamada que quer checar,\n'
                            'porém:\n\n'

                            'A formatação dos documentos mudaram\n'
                            'com o passar dos anos e, também,\n'
                            'os nomes de alguns cursos, então,\n'
                            'podem ocorrer problemas ao mudar o\n'
                            'ano que quer checar')

    menu_chamadas = ctk.CTkOptionMenu(master = frame_esquerdo,
                                      dynamic_resizing = False,
                                      font = FONTE,
                                      dropdown_font = FONTE,
                                      fg_color = ROXO,
                                      button_color = ROXO_ESCURO,
                                      button_hover_color = ROXO_MAIS_ESCURO,
                                      dropdown_fg_color = ROXO_ESCURO,
                                      dropdown_hover_color = ROXO_MAIS_ESCURO,
                                      corner_radius = RAIO,
                                      height = ALTURA,
                                      width = 100,
                                      text_color = CINZA,
                                      values = ['1ª', '2ª', '3ª', '4ª', '5ª'],
                                      command = mudar_ano_e_chamada)
    menu_chamadas.grid(row = 4, column = 1, pady = (0, 30), padx = (15, 190), sticky = 'w')
    menu_chamadas.set('1ª')

    botao_detalhes = ctk.CTkButton(master = frame_esquerdo,
                                   font = FONTE,
                                   height = ALTURA,
                                   width = 150,
                                   fg_color = CINZA_VERMELHADO,
                                   hover_color = ROXO_ESCURO,
                                   corner_radius = RAIO,
                                   text = 'Ver Detalhes',
                                   text_color = CINZA,
                                   command = lambda: [som_clique(), ver_dados_candidatos_aprovados_na_maior_caixa()],
                                   state = 'disabled')
    botao_detalhes.grid(row = 4, column = 1, columnspan = 2, pady = (0, 30), padx = (138, 0), sticky = 'w')

    botao_sair = ctk.CTkButton(master = frame_esquerdo,
                               font = FONTE,
                               height = ALTURA,
                               fg_color = VERMELHO,
                               hover_color = VERMELHO_ESCURO,
                               corner_radius = RAIO,
                               text = 'Sair',
                               text_color = CINZA,
                               command = lambda: [som_clique(), remover_pdfs(), window.quit(), sleep(0.12), exit()])
    botao_sair.grid(row = 4, column = 2, pady = (0, 30), padx = (0, 65), sticky = 'e')

    frame_direito = ctk.CTkFrame(master = window, fg_color = CINZA_ESCURO_VERMELHADO, corner_radius = 12)
    frame_direito.pack(side = 'right', pady = (0, 30), padx = (0, 30))

    rotulo_converter_notas = ctk.CTkLabel(master = frame_direito, fg_color = CINZA_VERMELHADO, corner_radius = RAIO,
                                          font = FONTE, height = ALTURA, text = 'Converter Notas', text_color = CINZA)
    rotulo_converter_notas.grid(row = 0, column = 0, columnspan = 2, pady = (30, 0), padx = 16)

    info_rotulo_converter_notas = ctk.CTkButton(master = frame_direito, width = 27, height = 15,
                                                font = ('',15,'bold'),
                                                fg_color = 'transparent', border_color = CINZA_VERMELHADO,
                                                border_width = 2, hover_color = ROXO, text = '?',
                                                state = 'disabled')
    info_rotulo_converter_notas.grid(row = 0, column = 1, padx = 10, pady = (35, 0), sticky = 'e')
    balao(info_rotulo_converter_notas, 'A UNB possui diferentes pesos\n'
                            'para cada curso de acordo\n'
                            'com o grupo ao qual o mesmo\n'
                            'pertence')

    rotulo_grupo_do_curso = ctk.CTkLabel(master = frame_direito, text_color = CINZA, text = 'Grupo do Curso', font = FONTE)
    rotulo_grupo_do_curso.grid(row = 1, column = 0, columnspan = 2, pady = 27, padx = 32)

    info_rotulo_grupo_do_curso = ctk.CTkButton(master = frame_direito, width = 27, height = 15,
                                               font = ('',15,'bold'), text_color = CINZA_ESCURO,
                                               fg_color = 'transparent', border_color = CINZA_VERMELHADO,
                                               border_width = 2, hover_color = ROXO, text = 'i',
                                               command = lambda: [som_clique(), ver_url_grupo()])
    info_rotulo_grupo_do_curso.grid(row = 1, column = 1, padx = 10, pady = (5, 0), sticky = 'e')
    balao(info_rotulo_grupo_do_curso, 'Ver link para PDF com a\n'
                                      'tabela com cada curso e\n'
                                      'seu respectivo grupo')

    botao_grupo_1 = ctk.CTkRadioButton(master = frame_direito, fg_color = ROXO, border_color = CINZA_VERMELHADO,
                                       hover_color = 'gray', font = FONTE_MENOR, border_width_unchecked = 5, text = 'Grupo  I',
                                       text_color = CINZA,
                                       variable = grupo_var, value = 1, command = som_clique)
    botao_grupo_1.grid(row = 2, column = 0, columnspan = 2, pady = (0, 15), padx = 16)
    botao_grupo_1.select()

    botao_grupo_2 = ctk.CTkRadioButton(master = frame_direito, fg_color = ROXO, border_color = CINZA_VERMELHADO,
                                       hover_color = 'gray', font = FONTE_MENOR, border_width_unchecked = 5, text = 'Grupo II',
                                       text_color = CINZA,
                                       variable = grupo_var, value = 2, command = som_clique)
    botao_grupo_2.grid(row = 3, column = 0, columnspan = 2, pady = 0, padx = 16)

    rotulo_insira_as_notas = ctk.CTkLabel(master = frame_direito, text_color = CINZA, text = 'Insira as Notas', font = FONTE)
    rotulo_insira_as_notas.grid(row = 4, column = 0, columnspan = 2, pady = 27, padx = 32)

    rotulo_nota_linguagens = ctk.CTkLabel(master = frame_direito, text_color = CINZA, text = 'Linguagens', font = FONTE)
    rotulo_nota_linguagens.grid(row = 5, column = 0, pady = (0, 15), padx = (32, 5), sticky = 'w')

    nota_1 = ctk.CTkEntry(master = frame_direito, width = 85, fg_color = CINZA_VERMELHADO, corner_radius = RAIO,
                          font = FONTE, text_color = CINZA_ESCURO, border_width = 0, placeholder_text = '000.00')
    nota_1.grid(row = 5, column = 1, pady = (0, 15), padx = (5, 32), sticky = 'w')

    rotulo_nota_humanas = ctk.CTkLabel(master = frame_direito, text_color = CINZA, text = 'Humanas', font = FONTE)
    rotulo_nota_humanas.grid(row = 6, column = 0, pady = (0, 15), padx = (32, 5), sticky = 'w')

    nota_2 = ctk.CTkEntry(master = frame_direito, width = 85, fg_color = CINZA_VERMELHADO, corner_radius = RAIO,
                          font = FONTE, text_color = CINZA_ESCURO, border_width = 0, placeholder_text = '000.00')
    nota_2.grid(row = 6, column = 1, pady = (0, 15), padx = (5, 32), sticky = 'w')

    rotulo_nota_natureza = ctk.CTkLabel(master = frame_direito, text_color = CINZA, text = 'Natureza', font = FONTE)
    rotulo_nota_natureza.grid(row = 7, column = 0, pady = (0, 15), padx = (32, 5), sticky = 'w')

    nota_3 = ctk.CTkEntry(master = frame_direito, width = 85, fg_color = CINZA_VERMELHADO, corner_radius = RAIO,
                          font = FONTE, text_color = CINZA_ESCURO, border_width = 0, placeholder_text = '000.00')
    nota_3.grid(row = 7, column = 1, pady = (0, 15), padx = (5, 32), sticky = 'w')

    rotulo_nota_matematica = ctk.CTkLabel(master = frame_direito, text_color = CINZA, text = 'Matemática', font = FONTE)
    rotulo_nota_matematica.grid(row = 8, column = 0, pady = (0, 15), padx = (32, 5), sticky = 'w')

    nota_4 = ctk.CTkEntry(master = frame_direito, width = 85, fg_color = CINZA_VERMELHADO, corner_radius = RAIO,
                          font = FONTE, text_color = CINZA_ESCURO, border_width = 0, placeholder_text = '000.00')
    nota_4.grid(row = 8, column = 1, pady = (0, 15), padx = (5, 32), sticky = 'w')

    rotulo_nota_redacao = ctk.CTkLabel(master = frame_direito, text_color = CINZA, text = 'Redação', font = FONTE)
    rotulo_nota_redacao.grid(row = 9, column = 0, pady = 0, padx = (32, 5), sticky = 'w')

    nota_5 = ctk.CTkEntry(master = frame_direito, width = 85, fg_color = CINZA_VERMELHADO, corner_radius = RAIO,
                          font = FONTE, text_color = CINZA_ESCURO, border_width = 0, placeholder_text = '000.00')
    nota_5.grid(row = 9, column = 1, pady = 0, padx = (5, 32), sticky = 'w')

    botao_converter = ctk.CTkButton(master = frame_direito,
                                    font = FONTE,
                                    height = ALTURA,
                                    fg_color = ROXO,
                                    hover_color = ROXO_ESCURO,
                                    corner_radius = RAIO,
                                    text = 'Converter',
                                    text_color = CINZA,
                                    command = lambda: [som_clique(), converter()])
    botao_converter.grid(row = 10, column = 0, columnspan = 2, pady = 27, padx = 16)

    rotulo_nota_final = ctk.CTkLabel(master = frame_direito, text_color = CINZA, text = 'Final', font = FONTE)
    rotulo_nota_final.grid(row = 11, column = 0, pady = (11, 36), padx = (32, 5), sticky = 'w')

    nota_6 = ctk.CTkLabel(master = frame_direito, width = 85, fg_color = CINZA_VERMELHADO, corner_radius = RAIO,
                          font = FONTE, text = '000.00', text_color = CINZA_ESCURO)
    nota_6.grid(row = 11, column = 1, pady = (11, 36), padx = (5, 32), sticky = 'w')

    # Ao abrir a UI, reproduz um som de clique e mostra algumas informações no rotulo_resultado.
    window.after(0, lambda: [som_clique(), ver_informacoes_iniciais()])

    # Ao fechar a UI, remove os arquivos antes.
    window.protocol('WM_DELETE_WINDOW', lambda: [remover_pdfs(), window.quit(), exit()])

    window.mainloop()


''' Funções principais '''

# Mostra as informações iniciais no rotulo_resultado.
def ver_informacoes_iniciais() -> None:
    adicionar_na_maior_caixa('Olá, este programa mostra as notas dos candidatos aprovados na UNB pelo\n'
                             'acesso ENEM.\n\n'

                             'Para começar, você pode escolher na lista de cursos disponíveis acima\n'
                             'uma opção e clicar em pesquisar para checar as notas máximas, mínimas e\n'
                             'também a média das notas, de acordo com cada cota que a universidade\n'
                             'disponibiliza.\n\n'

                             'É possível filtrar algumas opções de curso no botão escrito "TODOS"\n\n'

                             'Você pode escolher o ano que deseja checar e também a chamada além de\n'
                             'ser possível ver todas as notas no botão "Ver Detalhes"\n\n'

                             'Informações sobre o programa no "i" no canto superior esquerdo.')


# Essa função é ativada ao por o nome do curso e apertar o botão de pesquisar;
# Serve para chamar as funções que lidam com os arquivos e se alguma der erro, impede do programa continuar, mas não o fecha;
# Se tudo correr bem, chama a função que checa as maiores e as menores notas, além da média de cada cota e mostra na tela.
def iniciar_pesquisa() -> None:
    global cotas_notas, dados, inscricoes_aprovados, curso, ano, chamada

    # Confere se o curso digitado existe na lista de cursos.
    if menu_cursos.get().strip().upper() not in NOMES_DOS_CURSOS:
        mudar_status('Status: Curso inexistente', VERMELHO_CLARO)
        return

    # Reseta essas variáveis caso estejamos pesquisando um curso após já ter pesquisado algum.
    cotas_notas = {s: list() for s in SIMBOLO_COTAS}
    dados = ''
    inscricoes_aprovados.clear()

    # Armazena o nome do curso para mostrar no rótulo_resultado quando tiver terminado a pesquisa.
    curso = menu_cursos.get().strip().title()

    # Armazena o nome do ano para mostrar no rótulo_resultado quando tiver terminado a pesquisa.
    ano = opcoes_anos.get().strip()

    # Armazena o nome da chamada para mostrar no rótulo_resultado quando tiver terminado a pesquisa.
    chamada = menu_chamadas.get()

    # Ativa a barra de progresso.
    barra_progresso.configure(mode = 'indeterminate')
    Thread(target = barra_progresso.start).start()

    # Confere se os PDFs já estão baixados, se não, baixa-os.
    baixou_os_pdf = True
    try:
        open(NOME_PDF, 'r')
        open(NOME_PDF2, 'r')
    except:
        mudar_status('Status: Baixando os documentos...', VERDE)
        
        a = Thread(target = lambda: baixar_pdf(URL_DAS_NOTAS, NOME_PDF))
        b = Thread(target = lambda: baixar_pdf(URL_DOS_APROVADOS, NOME_PDF2))
        a.start()
        b.start()
        a.join()
        b.join()

    # Tenta abrir os PDFs, se não conseguir, houve algum erro.
    try:
        open(NOME_PDF, 'r')
        open(NOME_PDF2, 'r')
    except:
        mudar_status('Status: Erro de conexão com os documentos', VERMELHO_CLARO)
        baixou_os_pdf = False

    # Extrai os dados e as inscrições dos PDFs, e checa se dados e inscricoes_aprovados foram preenchidos, se não, houve algum erro. 
    if baixou_os_pdf:
        mudar_status('Status: Lendo os documentos...', VERDE)

        # O argumento é o curso escrito ou escolhido no menu_cursos, sem espaços e maiúsculo.
        worker_1 = Thread(target = extrair_dados_do_pdf(menu_cursos.get().replace(' ', '').strip().upper()))
        worker_2 = Thread(target = extrair_inscricoes_do_pdf)
        worker_1.start()
        worker_2.start()
        worker_1.join()
        worker_2.join()

        # Calcula as notas, se conseguiu extrair os dados.
        if len(dados) > 0 and len(inscricoes_aprovados) > 0:
            mudar_status('Status: Calculando as notas...', AZUL)
            
            worker_1 = Thread(target = corrigir_dados)
            worker_2 = Thread(target = checar_aprovados)
            worker_1.start()
            worker_1.join()
            worker_2.start()
            worker_2.join()

        # Caso não tenha conseguido extrair os dados.
        else:
            mudar_status('Status: Erro ao ler os documentos...', VERMELHO_CLARO)

    # Desativa a barra de progresso.
    barra_progresso.configure(mode = 'determinate')
    barra_progresso.stop()
    barra_progresso.set(1)


# Baixa os PDFs.
def baixar_pdf(url: str, nome_do_arquivo: str) -> None:
    try:
        pdf = get(url)
    except exceptions.RequestException as e:
        return

    open(nome_do_arquivo, "wb").write(pdf.content)


# Converte o pdf em texto e salva os dados de todos os candidatos que se inscreveram no curso pesquisado.
def extrair_dados_do_pdf(curso: str) -> None:  # Possui curso como parâmetro para copiar apenas os dados dos candidatos desse curso.
                                               # Não é o mesmo curso declarado nas variáveis globais.
    global dados

    pos_n = pos_c = pos_p = 0
    noturno = ceilandia = planaltina = False

    # Como há cursos noturnos com o mesmo nome dos diurnos, vamos checar se é noturno.
    if '(NOTURNO)' in curso:
        curso = curso.replace('(NOTURNO)', '').strip()
        noturno = True

    # Como há cursos no campus de Ceilândia com o mesmo nome dos nos outros campus, vamos checar se este é no Ceilândia.
    if '(CEILÂNDIA)' in curso:
        curso = curso.replace('(CEILÂNDIA)', '').strip()
        ceilandia = True

    # Só há 1 opção de curso no campus Gama, então, vamos pesquisar apenas por 'GAMA'.
    if '(GAMA)' in curso:
        curso = 'GAMA'

    # Como há cursos no campus de Planaltina com o mesmo nome dos nos outros campus, vamos checar se este é em Planaltina.
    if '(PLANALTINA)' in curso:
        curso = curso.replace('(PLANALTINA)', '').strip()
        planaltina = True

    # Converte o pdf com o programa pdftotext.exe; https://www.shedloadofcode.com/blog/searching-for-text-in-pdfs-at-increasing-scale.
    args = ["pdftotext", '-enc', 'UTF-8', NOME_PDF, '-']

    res = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = res.stdout.decode('utf-8').replace(' ', '')

    # Procura pelo nome do campus antes do nome do curso, para começar a procurar o nome do curso apenas após o nome do campus.
    if ceilandia:
        pos_c = search(r'CEILÂN.IA', output).span()[1]  # No documento de 2022 estava escrito CEILÂNCIA, e nos outros CEILÂNDIA. 

    if planaltina:
        pos_p = output.find('PLANALTINA')

    # Procura pelo nome 'NOTURNO', após a posição do nome 'CEILÂNDIA' ou 'PLANALTINA', se existirem.
    if noturno:
        pos_n = output.find('NOTURNO', pos_c if pos_c > 0 else pos_p)

    # A posição que começaremos será a maior que tivermos achado.
    pos = max(pos_c, pos_p, pos_n)

    # Procura pelo nome do curso após a posição dos nomes do campus e de 'NOTURNO', se não houverem procura do começo.
    pos_curso = output.find(curso, pos)

    # Procura pelo início da primeira inscrição após o nome do curso.
    pos_inicio = output.find(INICIO_INSCRICAO, pos_curso)

    # Procura pelos dados do último candidato nesse curso, demarcado pela posição dele na última cota + ponto final, por ex: ,-. ou ,123.
    pos_final = search(r',[\d|-]{1,4}\..\D', output[pos_inicio:]).span()[1]

    # Remove os números das páginas e associa dados ao nosso texto, desda posição de início até a posição final.
    dados = sub('\d{1,4}\r', '', output[pos_inicio:pos_inicio + pos_final - 3])  # O -3 é necessário para que o dado do último candidato fique igual aos outros.


# Como ao extrair texto do PDF ele vem com uma formatação esquisita é necessário corrigí-lo.
def corrigir_dados() -> None:
    global dados

    dados = dados.replace('\n', '').replace('\r', '').replace('\f', '')

    # Lista em que cada elemento era uma linha; Cada elemento tem os dados de um candidato: Inscrição,Nome,Nota,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10.
    dados = dados.split('/')  

    # Confere os dados de cada candidato e os corrige se necessário.
    for c in arange(len(dados), dtype = int):
        # Por algum motivo ao converter o pdf em texto pelo pdftotext.exe, quando os dados de algum candidato chegam
        # No fim da linha com "-", esse "-" não é lido e então ficam duas vírgulas juntas ou os dados terminam com
        # Uma vírgula, então é necessário repor esse "-" que não foi lido.
        if ',,' in dados[c]:  # Em alguns testes alguns candidatos ficaram com duas vírgulas juntas, sem nada entre elas.
            dados[c] = dados[c].replace(',,', ',-,')  # Coloca um - entre elas.

        if dados[c].endswith(','):  # Em alguns testes alguns candidatos ficaram com uma vírgula no final dos dados.
            dados[c] += '-'  # Coloca um - após essa vírgula.

        # Nas edições dos anos anteriores as notas eram no formato 999,99 em vez de 999.99, assim tendo mais de 12 vírgulas.
        if dados[c].count(',') > 12:  
            pos_1 = dados[c].find(',')
            pos_2 = dados[c].find(',', pos_1 + 1)
            pos_3 = dados[c].find(',', pos_2 + 1)

            dados[c] = dados[c][:pos_3] + '.' + dados[c][pos_3 + 1:]  # Troca essa vírgula da nota por um ponto.

        dados[c] = dados[c].split(',')  # Separa os dados dos candidatos em uma sublista em que cada elemento é um dado.


# Converte o pdf em texto e salva as inscrições de todos os candidatos que foram aprovados.
def extrair_inscricoes_do_pdf() -> None:  # Os dados extraídos são apenas os números das inscrições dos aprovados.
    global inscricoes_aprovados

    # Converte o pdf com o programa pdftotext.exe; https://www.shedloadofcode.com/blog/searching-for-text-in-pdfs-at-increasing-scale.
    args = ["pdftotext", '-enc', 'UTF-8', NOME_PDF2, '-']

    res = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = res.stdout.decode('utf-8').replace(' ', '')

    # Separa cada inscrição em uma lista.
    inscricoes_aprovados = findall(r'\d{8}', output)


# Essa função checa a partir das inscrições dos aprovados, suas notas e posições em cada cota, comparando as duas listas.
def checar_aprovados() -> None:
    # Lista para guardar cada dicionário com os dados dos candidatos aprovados.
    candidatos_aprovados = list()

    for candidato in dados:
        if candidato[0] in inscricoes_aprovados:  # Candidato[0] é a inscrição do candidato.
            candidatos_aprovados.append(candidato)

            # Esse dicionário guarda o valor numérico da cota a qual o candidato foi aprovado (a cota com a menor posição), e seu nome na versão resumida.
            menor_cota = {'pos': int(candidato[3]), 'nome': 's1'}  # Já declara a maior posição, que no caso vai ser sempre a da cota "s1".

            # Encontra a cota a qual o candidato foi aprovado (a cota com a menor posição).
            for s in arange(len(SIMBOLO_COTAS), dtype = int):
                # Se o candidato se inscreveu por essa cota e sua posição é menor que a menor posição nas cotas antes registradas.
                if candidato[s + 3] != '-' and int(candidato[s + 3]) < menor_cota['pos']:
                    menor_cota['pos'] = int(candidato[s + 3])
                    menor_cota['nome'] = SIMBOLO_COTAS[s]

            # Ao encontrar a cota a qual o candidato foi aprovado, atualiza os dados dessa cota registrando a nota desse candidato.
            cotas_notas[menor_cota['nome']].append(float(candidato[2]))

    # Para mostrar todas as notas dos aprovados e suas posições em cada cota, elas são ordenadas da menor nota para a maior.
    candidatos_aprovados = sorted(candidatos_aprovados, key = itemgetter(2))

    # Optei por não adicionar nem as inscrições nem os nomes no arquivo das notas dos candidatos aprovados.
    for c in arange(len(candidatos_aprovados), dtype = int):
        del candidatos_aprovados[c][0]
        del candidatos_aprovados[c][0]
        candidatos_aprovados[c] = ','.join(candidatos_aprovados[c]) + '\n'

    # Adiciona os dados no arquivo txt.
    with open('aprovados.txt', 'w') as aprovados_arquivo:
        aprovados_arquivo.writelines(candidatos_aprovados)

    # Mostra o resumo das notas dos aprovados na maior caixa de texto.
    som_clique()
    ver_resumo_das_notas_na_maior_caixa()


# Mostra na maior caixa as notas máxima, mínima e média de cada cota, se houverem aprovados por essa cota.
def ver_resumo_das_notas_na_maior_caixa() -> None:
    mudar_status('Status: Resumo das notas dos aprovados abaixo', VERDE)

    adicionar_na_maior_caixa('delete')

    # Calcula quantos candidados foram aprovados em cada cota.
    vagas_cotas = [len(cotas_notas[s]) for s in SIMBOLO_COTAS]
    vagas_totais = sum(vagas_cotas)

    adicionar_na_maior_caixa(f'Curso: {curso} \n'
                             f'Ano: {ano} \t\t\tChamada: {chamada} \t\t\tVagas Totais: {vagas_totais} \n')

    # Caso pelo menos um candidato tenha sido aprovado nessa chamada.
    if vagas_totais > 0:
        # Mostra a nota máxima, mínima e a média de cada cota, se houverem aprovados por essa cota.
        for s in arange(len(SIMBOLO_COTAS), dtype = int):
            if s == 2:
                adicionar_na_maior_caixa('\nEscola Pública: \n')

                # Se as vagas totais forem igual a soma das vagas de escolas particulares, não há aprovados por escola pública.
                if vagas_cotas[0] + vagas_cotas[1] == vagas_totais:
                    adicionar_na_maior_caixa('Nenhum candidato aprovado por escola pública nessa chamada.')
            adicionar_na_maior_caixa(f'Vagas: {vagas_cotas[s]:02d}; {NOMES_DAS_COTAS[s]}: Máx = {max(cotas_notas[SIMBOLO_COTAS[s]]):.2f}; '
                                     f'Min = {min(cotas_notas[SIMBOLO_COTAS[s]]):.2f}; Média = {mean(cotas_notas[SIMBOLO_COTAS[s]]):.2f}'
                                    ) if len(cotas_notas[SIMBOLO_COTAS[s]]) > 0 else ''
    # Se não vagas_totais for igual a 0, ninguém foi aprovado nessa chamada.
    else:
        adicionar_na_maior_caixa('Nenhum candidato chamado nessa chamada.')

    # Ativa o botão para ver todas as notas.
    botao_detalhes.configure(fg_color = ROXO, text = 'Ver Detalhes',
                             command = lambda: [som_clique(), ver_dados_candidatos_aprovados_na_maior_caixa()],
                             state = 'normal')


# Mostra todas as notas dos aprovados e suas posições em cada cota na maior caixa de texto.
def ver_dados_candidatos_aprovados_na_maior_caixa() -> None:
    mudar_status('Status: Detalhes das notas dos aprovados abaixo', VERDE)

    adicionar_na_maior_caixa('delete')

    # Lê o arquivo com as notas dos aprovados e suas posições em cada cota.
    with open('aprovados.txt', 'r') as aprovados_arquivo:
        aprovados = aprovados_arquivo.readlines()

    # Adiciona na maior caixa as notas dos aprovados e suas posições em cada cota.
    for linha in aprovados:
        adicionar_na_maior_caixa(linha.replace('\n', ''))

    # Ativa o botão para ver apenas as notas máximas, mínimas e média de cada cota.
    botao_detalhes.configure(fg_color = ROXO, text = 'Ver Resumo',
                             command = lambda: [som_clique(), ver_resumo_das_notas_na_maior_caixa()],
                             state = 'normal')


# Remove os PDFs, caso existam.
def remover_pdfs() -> None:
    try:
        remove(NOME_PDF)
    except:
        pass

    try:
        remove(NOME_PDF2)
    except:
        pass


''' Funções secundárias '''

# Mostra uma janela com texto quando o cursor está acima do widget.
def balao(widget, texto: str) -> None:
    balao = Balloon(widget.master)
    balao.bind(widget, texto)

    # Muda a fonte, cor do texto e de fundo, e deixa o texto centralizado.
    balao.component("label").configure(font = ('Cascadia Code', 12),
                                       background = CINZA_ESCURO_VERMELHADO,
                                       foreground = CINZA, justify = 'center',
                                       bd = 10)


# Converte sua nota com base nos pesos da UNB.
def converter() -> None:
    global nota_6

    # Converte as notas para floats, aceita "," e ".".
    try:
        n_1 = float(nota_1.get().replace(',', '.'))
        n_2 = float(nota_2.get().replace(',', '.'))
        n_3 = float(nota_3.get().replace(',', '.'))
        n_4 = float(nota_4.get().replace(',', '.'))
        n_5 = float(nota_5.get().replace(',', '.'))
    except:
        return

    if grupo_var.get() == 1:
        nota = (4 * (n_1 + n_2) + 2 * (n_3 + n_4) + n_5) / 13
    elif grupo_var.get() == 2:
        nota = (2 * (n_1 + n_2) + 4 * (n_3 + n_4) + n_5) / 13

    nota_6.configure(text = f'{nota:.2f}')


# Mostra no rotulos_resultado, informações sobre o programa.
def ver_info() -> None:
    texto = ('* Este programa não tem nenhuma afiliação com a Universidade de\n'
             '* Brasília. Os dados utilizados estão disponíveis para o público no\n'
             '* seguinte url: https://www.cebraspe.org.br/\n\n'

             '* Criador: Yogi Nam de Souza Barbosa\n'
             '* Github: https://github.com/euyogi/\n'
             '* Instagram: @eu.yogi\n\n'

             '* Este programa constitui o meu projeto do curso:\n'
             '* CS50 - Introduction to Computer Science of Harvard University\n'
             '* Disponível no seguinte url: https://pll.harvard.edu/course/cs50-introduction-computer-science/\n\n'

             '* Caso tenha encontrado algum comportamento incorreto e queira\n'
             '* colaborar reportando esse erro - (Necessário criar conta github)\n'
             '* Reporte bugs/erros no seguinte url: https://github.com/euyogi/Projeto-CS50/issues/new/\n'
             '* Versão: 1.0 Beta''')

    # Mostra o texto se ele já não estiver sendo mostrado, se já estiver apaga-o.
    if texto not in rotulo_resultado.get('0.0', 'end'):
        adicionar_na_maior_caixa('delete')
        mudar_status('Status: Informações do programa abaixo')
        adicionar_na_maior_caixa(texto)
    else:
        mudar_status('Status: Insira ou selecione um curso para começar')
        adicionar_na_maior_caixa('delete')


# Mostra no rotulos_resultado, url para PDF com informações sobre os grupos.
def ver_url_grupo() -> None:
    texto = ('* PDF com mais informações sobre o Acesso Enem UNB 2022, incluindo\n'
             '* tabela que mostra cada curso e seu respectivo grupo (I ou II) PG: 14\n'
             '* No seguinte URL: https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_1_ACESSOENEM_22_ABERTURA.PDF')

    # Mostra o texto se ele já não estiver sendo mostrado, se já estiver apaga-o.
    if texto not in rotulo_resultado.get('0.0', 'end'):
        adicionar_na_maior_caixa('delete')
        mudar_status('Status: Link com PDF sobre os grupos abaixo')
        adicionar_na_maior_caixa(texto)
    else:
        mudar_status('Status: Insira ou selecione um curso para começar')
        adicionar_na_maior_caixa('delete')


# Altera as opções do menu_cursos quando um filtro é selecionado no menu_filtros.
def mudar_opcoes_menu_cursos(opcao: str) -> None:
    # Reproduz som de clique.
    som_clique()  # Não consegui iniciar essa função no lambda pois o lambda não aceita argumentos, então vai ser chamada aqui.

    filtro = opcao.removesuffix('S')
    opcoes = list()

    if opcao != 'TODOS':
        for c in arange(len(NOMES_DOS_CURSOS), dtype = int):
            if filtro != 'BACHARELADO':
                if filtro in NOMES_DOS_CURSOS[c]:
                    opcoes.append(NOMES_DOS_CURSOS[c])
            else:
                if 'LICENCIATURA' not in NOMES_DOS_CURSOS[c]:
                    opcoes.append(NOMES_DOS_CURSOS[c])

        menu_cursos.configure(values = opcoes)
    else:
        menu_cursos.configure(values = NOMES_DOS_CURSOS)

    menu_cursos.set(opcao.capitalize())


# Altera os URLs de acordo com o ano e a chamada escolhida.
def mudar_ano_e_chamada(event: str = 'Esse parâmetro é apenas para a função aceitar o argumento que o opcoes_anos e o menu_chamadas inserem') -> None:
    global URL_DAS_NOTAS, URL_DOS_APROVADOS, opcoes_anos, menu_chamadas

    som_clique()  # Não consegui iniciar essa função no lambda pois o lambda não aceita argumentos, então vai ser chamada aqui.
    remover_pdfs()

    ano = opcoes_anos.get().strip()
    chamada = menu_chamadas.get().removesuffix('ª')

    if ano == '2022':
        chamadas = ['1ª', '2ª', '3ª', '4ª', '5ª']
        menu_chamadas.configure(values = chamadas)

        # Se a chamada selecionada não existir no ano selecionado, seleciona a primeira chamada.
        if chamada + 'ª' not in chamadas:
            menu_chamadas.set('1ª')
            chamada = '1'

        URL_DAS_NOTAS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_6_ACESSOENEM_22_RES_FINAL_BIOP_SCEP_E_NO_PROCESSO.PDF'
        if chamada == '1':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ACESSOENEM_22_ED_9_RES_FINAL_RA_1_CHAMADA.PDF'
        elif chamada == '2':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_13_ACESSOENEM_22_RES_FINAL_RA_2_CHAMADA.PDF'
        elif chamada == '3':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_16_ACESSOENEM_22_RES_FINAL_RA_3_CHAMADA.PDF'
        elif chamada == '4':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_19_ACESSOENEM_22_RES_FINAL_RA_4_CHAMADA.PDF'
        elif chamada == '5':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_22_ACESSOENEM_22_RES_FINAL_RA_5_CHAMADA.PDF'

    elif ano == '2021':
        chamadas = ['1ª', '2ª', '3ª', '4ª']
        menu_chamadas.configure(values = chamadas)
        # Se a chamada selecionada não existir no ano selecionado, seleciona a primeira chamada.
        if chamada + 'ª' not in chamadas:
            menu_chamadas.set('1ª')
            chamada = '1'

        URL_DAS_NOTAS = 'https://cdn.cebraspe.org.br/vestibulares/unb_21_1_acessoenem/arquivos/ED_7_2020_ACESSOENEM_21_RELAO_FINAL_BIOPSICOSSOCIAL.PDF'
        if chamada == '1':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_21_1_acessoenem/arquivos/ED_10_2020_ACESSOENEM_21_FINAL_1A_CHAMADA.PDF'
        elif chamada == '2':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_21_1_acessoenem/arquivos/ED_14_2020_ACESSOENEM_21_FINAL_2A_CHAMADA.PDF'
        elif chamada == '3':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_21_1_acessoenem/arquivos/ED_16_2020_ACESSOENEM_21_FINAL_3A_CHAMADA.PDF'
        elif chamada == '4':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_21_1_acessoenem/arquivos/ED_19_2020_ACESSOENEM_21_1_FINAL_REGISTRO_4_CHAMADA.PDF'

    elif ano == '2020_2':
        chamadas = ['1ª', '2ª']
        menu_chamadas.configure(values = chamadas)
        # Se a chamada selecionada não existir no ano selecionado, seleciona a primeira chamada.
        if chamada + 'ª' not in chamadas:
            menu_chamadas.set('1ª')
            chamada = '1'

        URL_DAS_NOTAS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_2_acessoenem/arquivos/ED_10_2020_ACESSOENEM_20_2_FIN_AV_BIOPSICO_SCEP_E_SELEO.PDF'
        if chamada == '1':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_2_acessoenem/arquivos/ED_13_2020_ACESSOENEM_20_2_FIN_REGISTRO_1_CHAMADA.PDF'
        elif chamada == '2':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_2_acessoenem/arquivos/ED_17_2020_ACESSOENEM_20_2_FIN_REGISTRO_2_CHAMADA.PDF'

    elif ano == '2020_1':
        chamadas = ['1ª', '2ª', '3ª', '4ª', '5ª', '6ª', '7ª', '8ª', '9ª']
        menu_chamadas.configure(values = chamadas)
        # Se a chamada selecionada não existir no ano selecionado, seleciona a primeira chamada.
        if chamada + 'ª' not in chamadas:
            menu_chamadas.set('1ª')
            chamada = '1'

        URL_DAS_NOTAS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_acessoenem/arquivos/ED_5_2019_ACESSOENEM_20_FINAL_AV_BIOPSICO_PROCESSO.PDF'
        if chamada == '1':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_acessoenem/arquivos/ED_9_ACESSOENEM_FINAL_REGISTRO_HOMOLOG.PDF'
        elif chamada == '2':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_acessoenem/arquivos/ED_13_ACESSOENEM_FINAL_REGISTRO_HOMOLOG_2_CHAMADA.PDF'
        elif chamada == '3':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_acessoenem/arquivos/ED_17_ACESSOENEM_FINAL_REGISTRO_HOMOLOG_3_CHAMADA.PDF'
        elif chamada == '4':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_acessoenem/arquivos/ED_20_ACESSOENEM_FINAL_REGISTRO_HOMOLOG_4_CHAMADA.PDF'
        elif chamada == '5':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_acessoenem/arquivos/ED_22_ACESSOENEM_FINAL_REGISTRO_HOMOLOG_5_CHAMADA.PDF'
        elif chamada == '6':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_acessoenem/arquivos/ED_24_ACESSOENEM_FINAL_REGISTRO_HOMOLOG_6_CHAMADA.PDF'
        elif chamada == '7':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_acessoenem/arquivos/ED_26_ACESSOENEM_FIN_REGISTRO_HOMOLOG_7_CHAMADA.PDF'
        elif chamada == '8':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_acessoenem/arquivos/ED_29_ACESSOENEM_FIN_REGISTRO_HOMOLOG_8_CHAMADA.PDF'
        elif chamada == '9':
            URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_20_acessoenem/arquivos/ED_32_ACESSOENEM_FIN_REGISTRO_HOMOLOG_9_CHAMADA.PDF'


# Essa função muda o texto na menor caixa de texto.
def mudar_status(texto: str = '', cor: str = CINZA) -> None:
    rotulo_status.configure(text = texto, text_color = cor)


# Essa função adicionar texto na maior caixa de texto, se o argumento for 'delete', apaga o texto.
def adicionar_na_maior_caixa(texto: str = '') -> None:
    rotulo_resultado.configure(state = 'normal')
    rotulo_resultado.delete('0.0', 'end') if texto == 'delete' else rotulo_resultado.insert('end', texto + '\n')
    rotulo_resultado.configure(state = 'disabled')


# Inicializa o mixer de som.
mixer.init()

# Essa função é para ser chamado ao apertar qualquer botão e tocar o som do clique.
def som_clique(event: str = 'Esse parâmetro é apenas para a função aceitar o argumento que a menu_cursos e o menu_filtros inserem') -> None:
    mixer.music.load('click_sound.wav')
    mixer.music.play(loops = 0)


if __name__ == '__main__':
    UI()
