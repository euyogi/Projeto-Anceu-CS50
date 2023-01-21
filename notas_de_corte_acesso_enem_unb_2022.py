# Esse programa abre um arquivo csv com nomes de candidatos à um curso da unb, suas notas e suas posições;
# E o analisa para escrever em outro arquivo csv as notas de corte desse curso e a posição dos candidatos;
# De acordo com a cota pela qual o mesmo foi aprovado na faculdade. Antes é necessário copiar os dados do;
# PDF disponibilizado pela cebraspe, desde o nome do curso até os dados do último candidato nesse curso em;
# um arquivo chamado NOME_DO_ARQUIVO que o programa irá criar caso não exista e lerá-o posteriormente.

from numpy import arange
from csv import DictReader
from sys import exit
from os import remove
from requests import get
from PyPDF2 import PdfReader
from operator import itemgetter

# Links dos pdf's que contém dados dos candidatos, incluindo notas; E um com as inscrições dos aprovados.
URL_DAS_NOTAS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_6_ACESSOENEM_22_RES_FINAL_BIOP_SCEP_E_NO_PROCESSO.PDF'
URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_7_ACESSOENEM_22_RES_CONV_1_CHAMADA.PDF'

# O modelo do cabeçalho e o tamanho da inscrição devem estar disponíveis no pdf acessível pelo url das notas.
CABECALHO = 'inscricao,nota,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10\n'  # Nome removido do cabeçalho, pois não pareceu necessário.
TAMANHO_DA_INSCRICAO = 9  # Inclui a "," após o número.

# Modelos de inscrições devem estar disponíveis no pdf acessível pelo url dos aprovados.
INICIO_INSCRICAO = '100'

# Pode ser qualquer nome.
NOME_PDF = 'dados.pdf'
NOME_CSV = NOME_PDF.replace('.pdf', '.csv')
NOME_TXT = NOME_PDF.replace('.pdf', '.txt')

class Cota:
    def __init__(self, quantidade = 0, soma = 0, media = 0, max = 0, min = 1000):
        self.quantidade = quantidade
        self.soma = soma
        self.media = media
        self.max = max
        self.min = min


resumo = {
    's1': Cota(),
    's2': Cota(),
    's3': Cota(),
    's4': Cota(),
    's5': Cota(),
    's6': Cota(),
    's7': Cota(),
    's8': Cota(),
    's9': Cota(),
    's10': Cota()
}

chaves = list(resumo.keys())

nomes_das_cotas = [
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
    print('')

    while True:
        curso = input('\033[1;33mQual o curso desejado? \033[m').strip().upper()
        if len(curso) > 0 and curso.replace(' ', '').isalpha():
            break
        else:
            print('\033[1;34mInválido.\033[m')
            
    criar_arquivos(curso)
    
    print('\033[1;33mChecando aprovados.....\033[m')
    
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
            
            for s in arange(len(chaves)):
                registrar_cotas(candidato, chaves[s])

    candidatos_aprovados = sorted(candidatos_aprovados, key = itemgetter('nota'))
    
    for idx in arange(len(candidatos_aprovados)):
        candidatos_aprovados[idx]['nota'] = str(candidatos_aprovados[idx]['nota'])
        del candidatos_aprovados[idx]['inscricao']
        candidatos_aprovados[idx] = ','.join(list(candidatos_aprovados[idx].values())) + '\n'
        
    candidatos_aprovados_arquivo = open('candidatos_aprovados.txt', 'w')
    candidatos_aprovados_arquivo.writelines(candidatos_aprovados)
    candidatos_aprovados_arquivo.close()
    
    print('')
    
    print(f'\033[1;32mCurso: {curso.title()}; Vagas: {vagas}\033[m\n')
    
    for s in arange(len(chaves)):
        if s == 2:
            print(f'\n\033[1;36mEscola Pública:\033[m\n')
        resumo[chaves[s]].media = resumo[chaves[s]].soma / resumo[chaves[s]].quantidade if resumo[chaves[s]].quantidade > 0 else 0
        print(f'\033[1;35m{nomes_das_cotas[s]}:\033[m Max = {resumo[chaves[s]].max}; Min = {resumo[chaves[s]].min}; Média = {resumo[chaves[s]].media:.2f}.') if resumo[chaves[s]].max > 0 else print(end = '')
        
    print('')

    aprovados_arquivo.close()
    dados_arquivo.close()
    
    remove(NOME_CSV)
    remove(NOME_TXT)
    
    exit(0)


def baixar_pdf(url):
    print('\033[1;32mBaixando [PDF].....\033[m')

    response = get(url)

    open(NOME_PDF, "wb").write(response.content)


# Possui 'curso' como argumento para extrair apenas os dados dos candidatos desse curso e não precisar copiar tudo.
def extrair_dados_do_pdf_em_csv(nome_pdf, curso):  # Os dados extraídos são os presentes no cabeçalho.
    print('\033[1;35mExtraindo dados do [PDF].....\033[m')

    try:
        reader = PdfReader(nome_pdf)
    except:
        print(f'\033[1;34mErro ao extrair dados do arquivo [{nome_pdf}].\033[m')
        exit(1)

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
    
    print(f'\033[1;34mO curso {curso} não foi encontrado.\033[m')
    exit(2) 
         
# Como ao extrair texto do pdf ele vem com uma formatação esquisita é necessário corrigí-lo.
def corrigir_dados_do_csv(nome_csv):
    print('\033[1;33mCorrigindo dados do [CSV].....\033[m')
    
    try:
        arquivo = open(nome_csv, 'r')
    except FileNotFoundError:
        print(f'\033[1;34mErro ao corrigir os dados do csv pois o arquivo [{nome_csv}] não existe.\033[m')
        exit(3)

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
    print('\033[1;35mExtraindo dados do [PDF].....\033[m')

    try:
        reader = PdfReader(nome_pdf)
    except:
        print(f'\033[1;34mErro ao extrair dados do arquivo [{nome_pdf}].\033[m')
        exit(4)

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


def criar_arquivos(curso):
    baixar_pdf(URL_DAS_NOTAS)
    extrair_dados_do_pdf_em_csv(NOME_PDF, curso)
    
    remove(NOME_PDF)
    
    corrigir_dados_do_csv(NOME_CSV)
    
    baixar_pdf(URL_DOS_APROVADOS)
    extrair_dados_do_pdf_em_txt(NOME_PDF)
    
    remove(NOME_PDF)
    
    
def registrar_cotas(candidato, pos_cota):
        if candidato[pos_cota] != '-':
            resumo[pos_cota].quantidade += 1
            resumo[pos_cota].soma += candidato['nota']
                    
            if candidato['nota'] > resumo[pos_cota].max:
                resumo[pos_cota].max = candidato['nota']
                        
            if candidato['nota'] < resumo[pos_cota].min:
                resumo[pos_cota].min = candidato['nota']
                    
                    
main()

