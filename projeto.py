''' Esse é o meu projeto final para o curso CS50 - é um aplicativo feito em python, que checa as notas dos candidatos
    que participaram do Enem e se inscreveram na Universidade Nacional de Brasília - UNB, mostrando por fim um resumo
    para cada curso da instituição, com as maiores notas, as menores notas (nota de corte), e a média em cada cota disponível.'''

''' O código tá na ordem: (Bibliotecas / Variáveis / Funções / UI) '''

''' Bibliotecas e módulos necessários para o programa. '''

import customtkinter

import os
from os import environ, remove

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from pygame import mixer

from threading import Thread

import multiprocessing as mp
import sys
from requests import get, exceptions

from PyPDF2 import PdfReader

from time import time, sleep

from dataclasses import dataclass

import subprocess
import re
from numpy import arange

from operator import itemgetter

from statistics import mean

''' Variáveis para armazenar dados necessários para as funções. '''

# Links dos PDF's que contém dados dos candidatos; NOTAS possui as notas de todos os candidatos; APROVADOS as inscrições dos aprovados.
URL_DAS_NOTAS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_6_ACESSOENEM_22_RES_FINAL_BIOP_SCEP_E_NO_PROCESSO.PDF'
URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_7_ACESSOENEM_22_RES_CONV_1_CHAMADA.PDF'

# Lista com cada cota em sua versão resumida.
SIMBOLO_COTAS = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10']

# Cada cota pode é identificado pelo programa pela sua versão resumida 's1', 's2'... Mas para o usuário é mostrado os nomes delas.
NOMES_DAS_COTAS = [
    'Sistema Universal: ',
    'Cotas para Negros: ',
    'PPI   <   1,5:     ',
    'PPI   < 1,5 D:     ',
    'Ñ PPI <   1,5:     ',
    'Ñ PPI < 1,5 D:     ',
    'PPI   >   1,5      ',
    'PPI   > 1,5 D:     ',
    'Ñ PPI >   1,5:     ',
    'Ñ PPI > 1,5 D:     '
]

# As inscrições tem 8 dígitos e começam com '100', útil para achar o início dos dados de cada candidato.
INICIO_INSCRICAO = '100'
TAMANHO_DA_INSCRICAO = 8
PAGINAS_INUTEIS = 38  # Checando o PDF das notas, vemos que até a página 39 não há notas, portanto são inúteis, 38 pois começa do 0.

# Nomes dos arquivos; Pode ser qualquer nome pois só existem enquanto o programa está rodando.
NOME_PDF = 'dados.pdf'
NOME_PDF2 = 'dados_2.pdf'
    
# Para ter os nomes dos cursos na combobox a partir do início do programa foi necessário declará-los.
NOMES_DOS_CURSOS = sorted(['ADMINISTRAÇÃO', 'AGRONOMIA', 'ARQUITETURA E URBANISMO', 'ARTES CÊNICAS - INTERPRETAÇÃO TEATRAL', 'ARTES VISUAIS', 'ARTES VISUAIS (LICENCIATURA)',
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

# Cores para output's e botões.
AZUL = '#4169E1'
AMARELO = '#FFBF3C'
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
dados = str()  # A princípio é uma string mas depois vai virar uma lista.
inscricoes_aprovados = list()

mixer.init()  # Inicializa o mixer de som.

# Declara os elementos da janela.
window = customtkinter.CTk()
frame = customtkinter.CTkFrame(master = window)
optionmenu = customtkinter.CTkOptionMenu(master = frame)
combobox = customtkinter.CTkComboBox(master = frame)
botao_pesquisar = customtkinter.CTkButton(master = frame)
status = customtkinter.CTkTextbox(master = frame)
progressbar = customtkinter.CTkProgressBar(master = frame)
resultado = customtkinter.CTkTextbox(master = frame)
botao_detalhes = customtkinter.CTkButton(master = frame)
botao_sair = customtkinter.CTkButton(master = frame)

''' Janela: '''
def main() -> None:
    # UI
    global window, frame, optionmenu, combobox, botao_pesquisar, status, progressbar, resultado, botao_detalhes, botao_sair
    customtkinter.set_appearance_mode('Dark')
    customtkinter.set_widget_scaling(0.8)  # Para deixar em um tamanho que achei melhor sem precisar alterar muita coisa.

    window = customtkinter.CTk(fg_color = ROXO_ESCURO)
    window.title('Checador de notas')
    window.geometry('770x580')
    window.resizable(False, False)

    FONTE = customtkinter.CTkFont(family = 'Cascadia Code', size = 20)
    FONTE_MENOR = customtkinter.CTkFont(family = 'Cascadia Code', size = 15)
    BUTTON_HEIGHT = 50
                
    frame = customtkinter.CTkFrame(master = window, fg_color = CINZA_ESCURO_VERMELHADO, corner_radius = 12)
    frame.pack(pady = (0, 30), padx = 30)

    optionmenu = customtkinter.CTkOptionMenu(master = frame,
                                            dynamic_resizing = False,
                                            font = FONTE,
                                            dropdown_font = FONTE,
                                            fg_color = ROXO,
                                            button_color = ROXO_ESCURO,
                                            button_hover_color = ROXO_MAIS_ESCURO,
                                            dropdown_fg_color = ROXO_ESCURO,
                                            dropdown_hover_color = ROXO_MAIS_ESCURO,
                                            height = BUTTON_HEIGHT,
                                            width = 140,
                                            values = ['TODOS', 'BACHARELADOS', 'LICENCIATURAS', 'NOTURNOS', 'CEILÂNDIA', 'GAMA', 'PLANALTINA'],
                                            command = mudar_valores_combobox)
    optionmenu.grid(row = 0, column = 0, pady = (30, 0), padx = (100, 0), sticky = 'nsew')
    optionmenu.set('TODOS')

    combobox = customtkinter.CTkComboBox(master = frame,
                                        font = FONTE,
                                        dropdown_font = FONTE,
                                        border_color = ROXO,
                                        fg_color = ROXO,
                                        button_color = ROXO_ESCURO,
                                        button_hover_color = ROXO_MAIS_ESCURO,
                                        dropdown_fg_color = ROXO_ESCURO,
                                        dropdown_hover_color = ROXO_MAIS_ESCURO,
                                        height = BUTTON_HEIGHT,
                                        values = NOMES_DOS_CURSOS,
                                        command = som_clique)
    combobox.grid(row = 0, column = 1, columnspan = 1, pady = (30, 0), padx = (15), sticky = 'nsew')
    combobox.set('Cursos')

    botao_pesquisar = customtkinter.CTkButton(master = frame,
                                            font = FONTE,
                                            height = BUTTON_HEIGHT,
                                            fg_color = ROXO,
                                            hover_color = ROXO_ESCURO,
                                            text = 'Pesquisar',
                                            command = lambda: [som_clique(), Thread(target = criar_arquivos).start()])
    botao_pesquisar.grid(row = 0, column = 2, pady = (30, 0), padx = (0, 100), sticky = 'nsew')

    status = customtkinter.CTkTextbox(master = frame, fg_color = CINZA_VERMELHADO, font = FONTE, height = BUTTON_HEIGHT)
    status.grid(row = 1, column = 0, columnspan = 3, pady = (25, 0), padx = 50, sticky = 'nsew')
    mudar_status('Status: Insira ou selecione um curso para começar')

    progressbar = customtkinter.CTkProgressBar(master = frame, fg_color = CINZA_VERMELHADO, progress_color = ROXO, height = 10, mode = 'indeterminate')
    progressbar.grid(row = 2, column = 0, columnspan = 3, pady = (15, 0), padx = 200, sticky = 'nsew')

    resultado = customtkinter.CTkTextbox(master = frame, fg_color = CINZA_VERMELHADO, font = FONTE, text_color = AMARELO, height = 400, state = 'disabled')
    resultado.grid(row = 3, column = 0, columnspan = 3, pady = (15, 25), padx = 50, sticky='nsew')

    botao_detalhes = customtkinter.CTkButton(master = frame,
                                            font = FONTE,
                                            height = BUTTON_HEIGHT,
                                            width = 200,
                                            fg_color = CINZA_VERMELHADO,
                                            hover_color = ROXO_ESCURO,
                                            text = 'Ver Detalhes',
                                            command = lambda: [som_clique(), ver_dados_candidatos_aprovados_na_maior_caixa()],
                                            state = 'disabled')
    botao_detalhes.grid(row = 4, column = 1, pady = (0, 30), padx = (0, 220))

    botao_sair = customtkinter.CTkButton(master = frame,
                                        font = FONTE,
                                        height = BUTTON_HEIGHT,
                                        width = 200,
                                        fg_color = VERMELHO,
                                        hover_color = VERMELHO_ESCURO,
                                        text = 'Sair',
                                        command = lambda: [som_clique(), remover_arquivos(), sleep(0.1), window.destroy(), exit()])
    botao_sair.grid(row = 4, column = 1, pady = (0, 30), padx = (220, 0))
    
    Thread(target = som_clique).start()
    window.protocol('WM_DELETE_WINDOW', lambda: [remover_arquivos(), window.destroy(), exit()])
    window.mainloop()
    

''' Funções: '''

# Essa função é ativada ao por o nome do curso e apertar o botão de pesquisar;
# Serve para chamar as funções que lidam com os arquivos e se alguma der erro, impede do programa continuar, mas não o fecha;
# Se tudo correr bem, chama a função que checa as maiores e as menores notas, além da média de cada cota e mostra na tela.
def criar_arquivos() -> None:
    global cotas_notas, dados, inscricoes_aprovados
    if combobox.get().strip().upper() not in NOMES_DOS_CURSOS:
        mudar_status('Status: Curso inexistente', VERMELHO_CLARO)
        return
    
    # Reseta essas variáveis caso estejamos pesquisando um curso após já ter pesquisado algum.
    cotas_notas = {s: list() for s in SIMBOLO_COTAS}
    dados = ''
    inscricoes_aprovados.clear()
    
    curso = combobox.get().replace(' ', '').strip().upper()
    
    progressbar.configure(mode = 'indeterminate')
    Thread(target = progressbar.start).start()
    
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
    
    try:
        open(NOME_PDF, 'r')
        open(NOME_PDF2, 'r')
    except:
        mudar_status('Status: Erro de conexão com os documentos', VERMELHO_CLARO)
        baixou_os_pdf = False
    
    if baixou_os_pdf:
        mudar_status('Status: Lendo os documentos...', VERDE)

        worker_1 = Thread(target = lambda: extrair_dados_do_pdf(curso))
        worker_2 = Thread(target = extrair_inscricoes_do_pdf)
        worker_1.start()
        worker_2.start()
        worker_1.join()
        worker_2.join()
        
        if len(dados) > 0 and len(inscricoes_aprovados) > 0:
            mudar_status('Status: Calculando as notas...', AZUL)
            
            worker_1 = Thread(target = corrigir_dados)
            worker_2 = Thread(target = checar_aprovados)
            worker_1.start()
            worker_1.join()
            worker_2.start()
            worker_2.join()

        else:
            mudar_status('Status: Erro ao ler os documentos...', VERMELHO_CLARO)
    
    progressbar.configure(mode = 'determinate')
    progressbar.stop()
    progressbar.set(1)


def remover_arquivos():
    try:
        remove(NOME_PDF)
        pass
    except:
        pass

    try:
        remove(NOME_PDF2)
        pass
    except:
        pass
    
    
''' Função para alterar as opções da combobox: '''

def mudar_valores_combobox(opcao: str) -> None:
    Thread(target = som_clique).start()  # Não consegui iniciar essa função no lambda, então vai ser chamada aqui.
     
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

        combobox.configure(values = opcoes)
    else:
        combobox.configure(values = NOMES_DOS_CURSOS)
        
    combobox.set(opcao.capitalize())


''' Funções que alteram o texto nas caixas de texto: '''

# Essa função muda o texto na menor caixa de texto.
def mudar_status(texto: str, cor: str = 'silver') -> None:
    status.configure(state = 'normal')
    status.delete('0.0', 'end')
    status.insert('0.0', texto)
    status.configure(state = 'disabled', text_color = cor)
    
    
def adicionar_na_maior_caixa(texto: str) -> None:
    resultado.configure(state = 'normal')
    resultado.delete('0.0', 'end') if texto == 'delete' else resultado.insert('end', texto + '\n')
    resultado.configure(state = 'disabled')
    
    
def ver_resumo_das_notas_na_maior_caixa() -> None:
    mudar_status('Status: Resumo das notas dos aprovados abaixo', VERDE)
    
    adicionar_na_maior_caixa('delete')
    
    vagas = sum(len(cotas_notas[s]) for s in SIMBOLO_COTAS)
    
    # BUG: Se o usuário aperta em 'Ver Detalhes', e altera o texto da combobox, e aperta em 'Ver Resumo', o nome do curso vai mudar para o que está na combobox. 
    adicionar_na_maior_caixa('\nCurso: ' + combobox.get().title() + '\tVagas: ' + str(vagas) + '\n')

    for s in arange(len(SIMBOLO_COTAS), dtype = int):
        if s == 2:
            adicionar_na_maior_caixa('\nEscola Pública:\n')
        adicionar_na_maior_caixa(NOMES_DAS_COTAS[s] + 'Max = ' + str(max(cotas_notas[SIMBOLO_COTAS[s]])) + '; Min = '
                         + str(min(cotas_notas[SIMBOLO_COTAS[s]])) + '; Média = ' + str(mean(cotas_notas[SIMBOLO_COTAS[s]]))[:6] + '.') if len(cotas_notas[SIMBOLO_COTAS[s]]) > 0 else ''
        
    botao_detalhes.configure(fg_color = ROXO, text = 'Ver Detalhes', command = lambda: [som_clique(), ver_dados_candidatos_aprovados_na_maior_caixa()], state = 'normal')
    

# Essa função mostra todas as notas dos aprovados e suas posições em cada cota na maior caixa de texto.
def ver_dados_candidatos_aprovados_na_maior_caixa() -> None:
    mudar_status('Status: Detalhes das notas dos aprovados abaixo', VERDE)
    
    adicionar_na_maior_caixa('delete')
    
    with open('aprovados.txt', 'r') as aprovados_arquivo:
        aprovados = aprovados_arquivo.readlines()
        
    for linha in aprovados:
        adicionar_na_maior_caixa(linha.replace('\n', ''))
        
    botao_detalhes.configure(fg_color = ROXO, text = 'Ver Resumo', command = lambda: [som_clique(), ver_resumo_das_notas_na_maior_caixa()], state = 'normal')
    

''' Funções que lidam com os arquivos: ''' 

def baixar_pdf(url: str, nome_do_arquivo: str) -> None:
    try:
        pdf = get(url)
    except exceptions.RequestException as e:
        exit()

    open(nome_do_arquivo, "wb").write(pdf.content)


# Possui 'curso' como argumento para extrair apenas os dados dos candidatos desse curso e não precisar copiar tudo.
def extrair_dados_do_pdf(curso: str) -> None:  # Os dados extraídos são os presentes no cabeçalho.
    global dados

    # Como há cursos noturnos com o mesmo nome dos diurnos, vamos checar se é noturno.
    pos_n = 0
    noturno = False
    if '(NOTURNO)' in curso:
        curso = curso.replace('(NOTURNO)', '').strip()
        noturno = True
    
    # Como há cursos no campus de Ceilândia com o mesmo nome dos nos outros campus, vamos checar se este é no Ceilândia.
    pos_c = 0
    ceilandia = False
    if '(CEILÂNDIA)' in curso:
        curso = curso.replace('CEILÂNDIA', '').strip()
        ceilandia = True
    
    # Não há cursos no campus de Gama com o mesmo nome dos nos outros campus, então, apenas retiraremos o nome '(GAMA)'.
    if '(GAMA)' in curso:
        curso = curso.replace('(GAMA)', '').strip()
        
    # Como há cursos no campus de Planaltina com o mesmo nome dos nos outros campus, vamos checar se este é em Planaltina.
    pos_p = 0
    planaltina = False
    if '(PLANALTINA)' in curso:
        curso = curso.replace('(PLANALTINA)', '').strip()
        planaltina = True
    
    args = ["pdftotext",
        '-enc',
        'UTF-8',
        NOME_PDF, # Example: "pdfs/United-Kingdom-Strategic-Export-Controls-Annual-Report-2021.pdf"
        '-']
    
    res = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = res.stdout.decode('utf-8').replace(' ', '')
    
    if ceilandia:
        pos_c = output.find('CEILÂNCIA')

    if planaltina:
        pos_p = output.find('PLANALTINA')

    if noturno:
        pos_n = output.find('NOTURNO', pos_c if pos_c > 0 else pos_p)

    pos = max(pos_c, pos_p, pos_n)
    
    pos_curso = output.find(curso, pos)
    
    pos_inicio = output.find(INICIO_INSCRICAO, pos_curso)    
    pos_final = re.search(r',[\d|-]{1,4}\..\D', output[pos_inicio:]).span()[1]

    dados = re.sub('\d{1,4}\r', '', output[pos_inicio:pos_inicio + pos_final - 3])  # Remove números da página e .
    

# Como ao extrair texto do PDF ele vem com uma formatação esquisita é necessário corrigí-lo.
def corrigir_dados() -> None:
    global dados

    dados = dados.replace('\n', '').replace('\r', '').replace('\f', '').replace('/', '\n')  #.replace('\r', '').replace('/', '\n')
    dados = dados.splitlines()  # Separa as linhas em uma lista de linhas.
    
    for c in arange(len(dados), dtype = int):
        if ',,' in dados[c]:
            dados[c] = dados[c].replace(',,', ',-,')
        if dados[c].endswith(','):
            dados[c] += '-'
        dados[c] = dados[c].split(',')

              
def extrair_inscricoes_do_pdf() -> None:  # Os dados extraídos são apenas os números das inscrições dos aprovados.
    global inscricoes_aprovados

    reader = PdfReader(NOME_PDF2)
    
    with mp.Pool() as pool:
        tmp_aprovados = pool.map(copiar_inscricoes_aprovados, reader.pages)
        tmp_aprovados = str(tmp_aprovados).replace("'", '').split(' ')

    inscricoes_aprovados = tmp_aprovados
    

def copiar_inscricoes_aprovados(pagina) -> str:
    texto = pagina.extract_text()
    texto = texto.replace(' ', '').split()  # Separa as linhas em uma lista de linhas e remove espaços para maior precisão.

    tmp_aprovados_dessa_pagina = str()
    
    for linha in arange(len(texto), dtype = int):
        if INICIO_INSCRICAO in texto[linha]:
            texto[linha] = texto[linha][texto[linha].find(INICIO_INSCRICAO):texto[linha].find(INICIO_INSCRICAO) + TAMANHO_DA_INSCRICAO]  # Copia apenas a inscrição.
            tmp_aprovados_dessa_pagina += texto[linha] + ' '
            
    return tmp_aprovados_dessa_pagina
    
    
''' Funções que lidam com os dados já formatados pelas funções que lidam com os arquivos '''

# Essa função checa a partir das inscrições dos aprovados, suas notas e posições em cada cota, comparando as duas listas.
def checar_aprovados() -> None:
    # Lista para guardar cada dicionário com os dados dos candidatos aprovados.
    candidatos_aprovados = list()
 
    for candidato in dados:
        if candidato[0] in inscricoes_aprovados:
            candidatos_aprovados.append(candidato)

            # Esse dicionário guarda o valor numérico da cota a qual o candidato foi aprovado (a cota com a menor posição), e seu nome na versão resumida.
            menor_cota = {'pos': int(candidato[3]), 'nome': 's1'}
         
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

    # Optei por não adicionar as inscrições no arquivo das notas dos candidatos aprovados.
    for c in arange(len(candidatos_aprovados), dtype = int):
        del candidatos_aprovados[c][0]
        del candidatos_aprovados[c][0]
        candidatos_aprovados[c] = ','.join(candidatos_aprovados[c]) + '\n'

    with open('aprovados.txt', 'w') as aprovados_arquivo:
        aprovados_arquivo.writelines(candidatos_aprovados)

    # Mostra o resumo das notas dos aprovados na maior caixa de texto.
    som_clique()
    ver_resumo_das_notas_na_maior_caixa()


# Essa função é para ser chamado ao apertar qualquer botão e tocar o som do clique.
def som_clique(event: str = 'Esse parâmetro é apenas para a função aceitar o argumento que a combobox e o optionmenu inserem') -> None:
    mixer.music.load('click_sound.wav')
    mixer.music.play(loops = 0)
    

if __name__ == '__main__':
    main()
