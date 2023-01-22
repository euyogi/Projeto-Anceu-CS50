import customtkinter
import tkinter

from numpy import arange
from csv import DictReader
from sys import exit
from os import remove
from requests import get
from PyPDF2 import PdfReader
from operator import itemgetter
from dataclasses import dataclass

# Links dos pdf's que contém dados dos candidatos, incluindo notas; E um com as inscrições dos aprovados.
URL_DAS_NOTAS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_6_ACESSOENEM_22_RES_FINAL_BIOP_SCEP_E_NO_PROCESSO.PDF'
URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_7_ACESSOENEM_22_RES_CONV_1_CHAMADA.PDF'

# O modelo do cabeçalho e o tamanho da inscrição devem estar disponíveis no pdf acessível pelo url das notas.
CABECALHO = 'inscricao,nota,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10\n'  # Nome removido do cabeçalho, pois não pareceu necessário.

SIMBOLO_COTAS = CABECALHO[CABECALHO.find('s1'):].removesuffix('\n').split(',')

TAMANHO_DA_INSCRICAO = 9  # Inclui a "," após o número.

# Modelos de inscrições devem estar disponíveis no pdf acessível pelo url dos aprovados.
INICIO_INSCRICAO = '100'

# Pode ser qualquer nome.
NOME_PDF = 'dados.pdf'
NOME_CSV = NOME_PDF.replace('.pdf', '.csv')
NOME_TXT = NOME_PDF.replace('.pdf', '.txt')

NOMES_DOS_CURSOS = sorted(['ADMINISTRAÇÃO', 'AGRONOMIA', 'ARQUITETURA', 'ARTES CÊNICAS - INTERPRETAÇÃO TEATRAL',
                    'ARTES VISUAIS (LICENCIATURA)', 'BIBLIOTECONOMIA', 'BIOTECNOLOGIA', 'CIÊNCIA DA COMPUTAÇÃO',
                    'CIÊNCIA POLÍTICA', 'CIÊNCIAS BIOLÓGICAS', 'CIÊNCIAS CONTÁBEIS', 'CIÊNCIAS ECONÔMICAS',
                    'SOCIOLOGIA (BACHARELADO/LICENCIATURA)', 'AUDIOVISUAL', 'PUBLICIDADE E PROPAGANDA',
                    'DESIGN', 'DIREITO', 'EDUCAÇÃO FÍSICA', 'ENFERMAGEM', 'ENGENHARIA AMBIENTAL', 'ENGENHARIA CIVIL',
                    'ENGENHARIA DE COMPUTAÇÃO', 'ENGENHARIA DE REDES DE COMUNICAÇÃO', 'ENGENHARIA ELÉTRICA',
                    'ENGENHARIA MECÂNICA', 'ENGENHARIA MECATRÔNICA', 'ENGENHARIA QUÍMICA', 'ESTATÍSTICA', 'FARMÁCIA',
                    'FILOSOFIA (BACHARELADO/LICENCIATURA)', 'FÍSICA', 'GEOFÍSICA', 'GEOGRAFIA (BACHARELADO/LICENCIATURA)',
                    'GEOLOGIA', 'HISTÓRIA (BACHARELADO/LICENCIATURA)', 'JORNALISMO', 'PORTUGUÊS DO BRASIL COMO SEGUNDA LÍNGUA (LICENCIATURA)',
                    'TRADUÇÃO – FRANCÊS', 'TRADUÇÃO – INGLÊS', 'LICENCIATURA EM ARTES CÊNICAS', 'LÍNGUA ESTRANGEIRA APLICADA',
                    'LÍNGUA FRANCESA E RESPECTIVA LITERATURA (BACHARELADO/LICENCIATURA)', 'LÍNGUA INGLESA E RESPECTIVA LITERATURA(BACHARELADO/LICENCIATURA)',
                    'LÍNGUA PORTUGUESA E RESPECTIVA LITERATURA (BACHARELADO/LICENCIATURA)', 'MATEMÁTICA (BACHARELADO/LICENCIATURA)',
                    'MEDICINA', 'MEDICINA (BACHARELADO) – SUB JUDICE', 'MEDICINA VETERINÁRIA', 'MUSEOLOGIA', 'MÚSICA',
                    'MÚSICA (LICENCIATURA)', 'NUTRIÇÃO', 'ODONTOLOGIA', 'PEDAGOGIA (LICENCIATURA)', 'PSICOLOGIA (BACHARELADO / LICENCIATURA / PSICÓLOGO)',
                    'QUÍMICA', 'QUÍMICA TECNOLÓGICA', 'RELAÇÕES INTERNACIONAIS', 'TURISMO', 'SAÚDE COLETIVA', 'SERVIÇO SOCIAL', 'HISTÓRIA DA ARTE', 'FISIOTERAPIA',
                    'FONOAUDIOLOGIA', 'TERAPIA OCUPACIONAL', 'ENGENHARIAS', 'CIÊNCIAS NATURAIS (LICENCIATURA)', 'NOTURNO CIÊNCIAS NATURAIS (LICENCIATURA)', 'GESTÃO AMBIENTAL'])

VERDE = '#83F28F'
VERMELHO_CLARO = '#D9381E'
VERMELHO = '#A5361F'
VERMELHO_ESCURO = '#521B0F'
AZUL_ESCURO = '#008B8B'

@dataclass
class Cota:
    quantidade: int = 0
    soma: int = 0

    max: int = 0
    min: int = 1000

    def calcular_media(self):
        self.media = self.soma / self.quantidade if self.quantidade > 0 else 0


resumo = {s: Cota() for s in SIMBOLO_COTAS}

NOMES_DAS_COTAS = [
    'Sistema Universal',
    'Cotas para Negros',
    'PPI < 1,5',
    'PPI < 1,5 D',
    'Branco < 1,5',
    'Branco < 1,5 D',
    'PPI > 1,5',
    'PPI > 1,5 D',
    'Branco > 1,5',
    'Branco > 1,5 D'
]
    
def main():
    mudar_status('Status: Checando aprovados.....', VERDE)

    aprovados_arquivo = open(NOME_TXT, 'r')
    aprovados = aprovados_arquivo.read()

    dados_arquivo = open(NOME_CSV, 'r')
    dados = DictReader(dados_arquivo)

    candidatos_aprovados = list()

    vagas = 0
    for candidato in dados:
        if candidato['inscricao'] in aprovados:
            candidatos_aprovados.append(candidato)

            vagas += 1
            candidato['nota'] = float(candidato['nota'])

            menor_cota = [int(candidato['s1']), 's1']

            for s in arange(len(SIMBOLO_COTAS)):
                if candidato[SIMBOLO_COTAS[s]] != '-' and int(candidato[SIMBOLO_COTAS[s]].replace('-', '')) < menor_cota[0]:
                    menor_cota[0] = int(candidato[SIMBOLO_COTAS[s]])
                    menor_cota[1] = SIMBOLO_COTAS[s]

            registrar_cotas(candidato, menor_cota[1])

    candidatos_aprovados = sorted(candidatos_aprovados, key = itemgetter('nota'))

    for idx in arange(len(candidatos_aprovados)):
        candidatos_aprovados[idx]['nota'] = str(candidatos_aprovados[idx]['nota'])
        del candidatos_aprovados[idx]['inscricao']
        candidatos_aprovados[idx] = ','.join(list(candidatos_aprovados[idx].values())) + '\n'

    candidatos_aprovados_arquivo = open('candidatos_aprovados.txt', 'w')
    candidatos_aprovados_arquivo.writelines(candidatos_aprovados)
    candidatos_aprovados_arquivo.close()

    mudar_status('Status: Resumo das notas abaixo')
    
    resultado.configure(state = 'normal')
    resultado.delete('0.0', 'end')
    resultado.configure(state = 'disabled')
    
    adicionar_resultado('\nCurso: ' + combobox.get().title() + '; Vagas: ' + str(vagas) + '\n')

    c = 0
    for s in arange(len(SIMBOLO_COTAS)):
        if s == 2:
            adicionar_resultado('\nEscola Pública:\n')
            c += 2
        adicionar_resultado(NOMES_DAS_COTAS[s] + ': Max = ' + str(resumo[SIMBOLO_COTAS[s]].max) + '; Min = '
                         + str(resumo[SIMBOLO_COTAS[s]].min) + '; Média = ' + str(resumo[SIMBOLO_COTAS[s]].media)[:6] + '.') if resumo[SIMBOLO_COTAS[s]].max > 0 else ''
        c += 1

    aprovados_arquivo.close()
    dados_arquivo.close()
    remove(NOME_CSV)
    remove(NOME_TXT)

    
    
def mudar_status(texto = 'vazio', cor = 'silver'):
    status.configure(state = 'normal')
    status.delete('0.0', 'end')
    status.insert('0.0', texto)
    status.configure(state = 'disabled', text_color = cor)


def adicionar_resultado(texto = 'vazio'):
    resultado.configure(state = 'normal')
    resultado.insert('end', texto + '\n')
    resultado.configure(state = 'disabled')
    
    
def baixar_pdf(url):
    mudar_status('Status: Baixando PDF.....', VERDE)
    response = get(url)

    open(NOME_PDF, "wb").write(response.content)


# Possui 'curso' como argumento para extrair apenas os dados dos candidatos desse curso e não precisar copiar tudo.
def extrair_dados_do_pdf_em_csv(nome_pdf, curso):  # Os dados extraídos são os presentes no cabeçalho.
    mudar_status('Status: Extraindo dados do PDF.....', AZUL_ESCURO)

    try:
        reader = PdfReader(nome_pdf)
    except:
        mudar_status('Status: Erro ao extrair dados do arquivo ' + nome_pdf, VERMELHO_CLARO)
        return

    numero_de_paginas = len(reader.pages)

    achou_curso = False
    for idx in arange(numero_de_paginas):
        idx = int(idx)

        pagina = reader.pages[idx]
        texto = pagina.extract_text()

        if not achou_curso:
            if curso in texto:
                achou_curso = True

                texto = texto[texto.find(curso):]

                # No pdf das notas, os dados de cada candidato começa com a inscrição.
                texto = texto[texto.find(INICIO_INSCRICAO):] # Apaga qualquer texto antes dos dados do primeiro candidato.

                arquivo = open(NOME_CSV, 'a')

        # No pdf das notas, os dados do último candidato termina com '-.'.
        if achou_curso and '-.' in texto:
            texto = texto[:texto.find('-.') + 1]  # Apaga qualquer texto após os dados do último candidato.
            arquivo.writelines(texto)
            arquivo.close()
            return 0

        if achou_curso:
            arquivo.writelines(texto)
    if not achou_curso:
        mudar_status('Status: Erro ao extrair dados do arquivo, curso não encontrado', VERMELHO_CLARO)
        return

# Como ao extrair texto do pdf ele vem com uma formatação esquisita é necessário corrigí-lo.
def corrigir_dados_do_csv(nome_csv):
    mudar_status('Status: Corrigindo dados do CSV.....', 'yellow')

    try:
        arquivo = open(nome_csv, 'r')
    except FileNotFoundError:
        mudar_status('Erro ao corrigir os dados do csv pois o arquivo '+ nome_csv + 'não existe.', VERMELHO_CLARO)
        return

    copia = arquivo.read()  # Copia o arquivo em uma string.
    copia = copia.replace('\n', '').replace(' ', '').replace('/', '\n')  # Remove "\n" equivocados, espaços e troca as "/" por "\n".
    copia = copia.splitlines()  # Separa as linhas em uma lista de linhas.

    for idx in arange(len(copia)):
        idx = int(idx)

        if copia[idx].isdigit():  # Apaga linhas que tenham apenas o número da página.
            copia[idx] = ''

        # Apaga os nomes, eles ficam entre a 1ª e a 2ª vírgula.
        else:
            pos1 = copia[idx].find(',')  # Posição da 1ª vírgula.
            pos2 = copia[idx].find(',', pos1 + 1)  # Posição da 2ª vírgula.

            copia[idx] = copia[idx][:pos1] + copia[idx][pos2:] + '\n'

    arquivo = open(nome_csv, 'w')
    arquivo.write(CABECALHO + ''.join(copia))
    arquivo.close()


def extrair_dados_do_pdf_em_txt(nome_pdf):  # Os dados extraídos são apenas os números das inscrições dos aprovados.
    mudar_status('Status: Extraindo dados do PDF.....', AZUL_ESCURO)
    
    try:
        reader = PdfReader(nome_pdf)
    except:
        mudar_status('Status: Erro ao extrair dados do arquivo ' + nome_pdf, VERMELHO_CLARO)
        return

    numero_de_paginas = len(reader.pages)

    arquivo = open(NOME_TXT, 'a')

    for idx in arange(numero_de_paginas):
        idx = int(idx)

        pagina = reader.pages[idx]
        texto = pagina.extract_text()

        texto = texto.split()  # Separa as linhas em uma lista de linhas.

        for idx_2 in arange(len(texto)):
            idx_2 = int(idx_2)

            if INICIO_INSCRICAO in texto[idx_2]:  # No pdf dos aprovados, as inscrições começam com '100'
                texto[idx_2] = texto[idx_2][texto[idx_2].find(INICIO_INSCRICAO):texto[idx_2].find(INICIO_INSCRICAO) + TAMANHO_DA_INSCRICAO - 1] + '\n'  # Copia apenas a inscrição.
            else:
                texto[idx_2] = ''

        arquivo.writelines(''.join(texto))

    arquivo.close()


def criar_arquivos():
    if combobox.get().strip().upper() not in NOMES_DOS_CURSOS:
        mudar_status('Status: Curso inexistente', VERMELHO_CLARO)
        return
    
    baixar_pdf(URL_DAS_NOTAS)
    extrair_dados_do_pdf_em_csv(NOME_PDF, combobox.get().strip().upper())

    remove(NOME_PDF)

    corrigir_dados_do_csv(NOME_CSV)

    baixar_pdf(URL_DOS_APROVADOS)
    extrair_dados_do_pdf_em_txt(NOME_PDF)

    remove(NOME_PDF)
    
    main()


def registrar_cotas(candidato, pos_cota):
    resumo[pos_cota].quantidade += 1
    resumo[pos_cota].soma += candidato['nota']

    if candidato['nota'] > resumo[pos_cota].max:
            resumo[pos_cota].max = candidato['nota']

    if candidato['nota'] < resumo[pos_cota].min:
            resumo[pos_cota].min = candidato['nota']
            
    resumo[pos_cota].calcular_media()


# UI
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')
    
app = customtkinter.CTk()
app.title('Checador de notas')
app.geometry('940x780')

app.grid_rowconfigure(3)
app.grid_columnconfigure(1)
        
frame = customtkinter.CTkFrame(master = app)
frame.pack(pady = 30, padx = 30)
    
combobox = customtkinter.CTkComboBox(master = frame,
                                     font = ('', 20),
                                     dropdown_font = ('', 15),
                                     height = 50,
                                     values = NOMES_DOS_CURSOS)
combobox.grid(row = 0, column = 0, pady = 30, padx = 40, sticky="nsew")
combobox.set('Cursos')

botao_pesquisar = customtkinter.CTkButton(master = frame, font = ('', 20), height = 50, text = 'Pesquisar', command = criar_arquivos)
botao_pesquisar.grid(row = 0, column = 1, pady = 30, padx = 40, sticky='nsew')

status = customtkinter.CTkTextbox(master = frame, font = ('', 20), height = 50, width = 410, state = 'disabled')
status.grid(row = 1, columnspan = 2, pady = 15, padx = 20)
mudar_status('Status: Insira o curso para começar')

resultado = customtkinter.CTkTextbox(master = frame, font = ('', 20), height = 400, width = 820, state = 'disabled')
resultado.grid(row = 2, columnspan = 2, pady = 15, padx = 30, sticky='nsew')

botao_sair = customtkinter.CTkButton(master = frame, font = ('', 20), height = 50, width = 150, fg_color = VERMELHO, hover_color = VERMELHO_ESCURO, text = 'Sair', command = exit)
botao_sair.grid(row = 3, columnspan = 2, pady = 30, padx = 20)

app.mainloop()
