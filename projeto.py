''' Esse é o meu projeto final para o curso CS50 - é um aplicativo feito em python, que checa as notas dos candidatos
    que participaram do Enem e se inscreveram na Universidade Nacional de Brasília - UNB, mostrando por fim um resumo
    para cada curso da instituição, com as maiores notas, as menores notas (nota de corte), e a média em cada cota disponível.'''

''' O código tá na ordem: (Bibliotecas / Variáveis / Funções / UI) '''

''' Bibliotecas e módulos necessários para o programa. '''

import customtkinter

from requests import get

from PyPDF2 import PdfReader

from csv import DictReader

from os import remove

from dataclasses import dataclass

from numpy import arange

from operator import itemgetter


''' Variáveis para armazenar dados necessários para as funções. '''

# Links dos PDF's que contém dados dos candidatos; NOTAS possui as notas de todos os candidatos; APROVADOS as inscrições dos aprovados.
URL_DAS_NOTAS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_6_ACESSOENEM_22_RES_FINAL_BIOP_SCEP_E_NO_PROCESSO.PDF'
URL_DOS_APROVADOS = 'https://cdn.cebraspe.org.br/vestibulares/unb_22_acessoenem/arquivos/ED_7_ACESSOENEM_22_RES_CONV_1_CHAMADA.PDF'

# Cabeçalho de acordo com o disponibilizado nos PDF's.
CABECALHO = 'inscricao,nota,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10\n'  # Nome removido do cabeçalho, pois não pareceu necessário.

# Lista com cada cota em sua versão resumida 's1', 's2'... Extraídas a partir do cabeçalho.
SIMBOLO_COTAS = CABECALHO[CABECALHO.find('s1'):].removesuffix('\n').split(',')

# Cada cota pode é identificado pelo programa pela sua versão resumida 's1', 's2'... Mas para o usuário é mostrado os nomes delas.
NOMES_DAS_COTAS = [
    'Sistema Universal: ',
    'Cotas para Negros: ',
    'PPI < 1,5:         ',
    'PPI < 1,5 D:       ',
    'Branco < 1,5:      ',
    'Branco < 1,5 D:    ',
    'PPI > 1,5:         ',
    'PPI > 1,5 D:       ',
    'Branco > 1,5:      ',
    'Branco > 1,5 D:    '
]

# As inscrições tem 8 dígitos e começam com '100', útil para achar o início dos dados de cada candidato.
INICIO_INSCRICAO = '100'
TAMANHO_DA_INSCRICAO = 9  # Inclui a "," após o número.

# Nomes dos arquivos; Pode ser qualquer nome pois só existem enquanto o programa está rodando.
NOME_PDF = 'dados.pdf'
NOME_CSV = NOME_PDF.replace('.pdf', '.csv')
NOME_TXT = NOME_PDF.replace('.pdf', '.txt')

# Para ter os nomes dos cursos na combobox a partir do início do programa foi necessário declará-los.
NOMES_DOS_CURSOS = sorted(['ADMINISTRAÇÃO', 'AGRONOMIA', 'ARQUITETURA E URBANISMO', 'ARTES CÊNICAS – INTERPRETAÇÃO TEATRAL', 'ARTES VISUAIS', 'ARTES VISUAIS (LICENCIATURA)',
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
                    'GESTÃO AMBIENTAL (PLANALTINA) (NOTURNO)'])

# Cores para output's.
AZUL = '#4169E1'
CINZA = '#333333'
CINZA_ESCURO = '212121'
VERDE = '#83F28F'
VERMELHO_CLARO = '#D9381E'
VERMELHO = '#A5361F'
VERMELHO_ESCURO = '#521B0F'

# Essa classe nos disponibiliza a maior e a menor nota dos candidatos aprovados na cota x, além da média.
@dataclass
class Cota:
    n_pessoas: int = 0
    soma_notas: int = 0

    max: int = 0
    min: int = 1000

    def calcular_media(self):
        self.media_notas = self.soma_notas / self.n_pessoas if self.n_pessoas > 0 else 0


# Como existem 10 cotas, nessa varíavel é armazenado as maiores e as menores notas de cada uma, além de suas médias.
resumo = {s: Cota() for s in SIMBOLO_COTAS}

''' Funções: '''

# Essa função é ativada ao por o nome do curso e apertar o botão de pesquisar;
# Serve para chamar as funções que lidam com os arquivos e se alguma der erro, impede do programa continuar, mas não o fecha;
# Se tudo correr bem, chama a função que checa as maiores e as menores notas, além da média de cada cota e mostra na tela.
def criar_arquivos():
    if combobox.get().strip().upper() not in NOMES_DOS_CURSOS:
        mudar_status('Status: Curso inexistente', VERMELHO_CLARO)
        return
    
    if baixar_pdf(URL_DAS_NOTAS) != 0:
        return
    
    if extrair_dados_do_pdf_em_csv(NOME_PDF, combobox.get().replace(' ', '').strip().upper()) != 0:
        try:
            remove(NOME_PDF)
        except:
            pass
        return
    
    remove(NOME_PDF)
    
    if corrigir_dados_do_csv(NOME_CSV) != 0:
        return

    if baixar_pdf(URL_DOS_APROVADOS) != 0:
        return
    
    if extrair_dados_do_pdf_em_txt(NOME_PDF) != 0:
        try:
            remove(NOME_PDF)
        except:
            pass
        return

    remove(NOME_PDF)
    
    checar_aprovados()


''' Função para alterar as opções da combobox: '''

def mudar_valores_combobox(opcao):
    filtro = opcao.removesuffix('S')
    opcoes = list()
    
    if opcao != 'TODOS':
        for c in arange(len(NOMES_DOS_CURSOS)):
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
def mudar_status(texto = 'vazio', cor = 'silver'):
    status.configure(state = 'normal')
    status.delete('0.0', 'end')
    status.insert('0.0', texto)
    status.configure(state = 'disabled', text_color = cor)
    
    
# Essa função é utilizada para adicionar texto na maior caixa de texto.
def adicionar_resultado(texto = 'vazio'):
    resultado.configure(state = 'normal')
    resultado.delete('0.0', 'end') if texto == 'delete' else resultado.insert('end', texto + '\n')
    resultado.configure(state = 'disabled')
    
    
# Essa função mostra o resumo das notas dos aprovados na maior caixa de texto.
def ver_resumo():
    mudar_status('Status: Resumo das notas dos aprovados abaixo')
    
    adicionar_resultado('delete')
    
    vagas = sum(resumo[s].n_pessoas for s in SIMBOLO_COTAS)
    
    
    # BUG: Se o usuário aperta em 'Ver Detalhes', e altera o texto da combobox, e aperta em 'Ver Resumo', o nome do curso vai mudar para o que está na combobox. 
    adicionar_resultado('\nCurso: ' + combobox.get().title() + '\tVagas: ' + str(vagas) + '\n')

    for s in arange(len(SIMBOLO_COTAS)):
        if s == 2:
            adicionar_resultado('\nEscola Pública:\n')
        adicionar_resultado(NOMES_DAS_COTAS[s] + 'Max = ' + str(resumo[SIMBOLO_COTAS[s]].max) + '; Min = '
                         + str(resumo[SIMBOLO_COTAS[s]].min) + '; Média = ' + str(resumo[SIMBOLO_COTAS[s]].media_notas)[:6] + '.') if resumo[SIMBOLO_COTAS[s]].max > 0 else ''
        
    botao_detalhes.configure(fg_color = AZUL, text = 'Ver Detalhes', command = ver_candidatos_aprovados_arquivo, state = 'normal')
    

# Essa função mostra todas as notas dos aprovados e suas posições em cada cota na maior caixa de texto.
def ver_candidatos_aprovados_arquivo():
    mudar_status('Status: Detalhes das notas dos aprovados abaixo')
    
    adicionar_resultado('delete')
    
    with open('aprovados.txt', 'r') as aprovados_arquivo:
        aprovados = aprovados_arquivo.readlines()
        
    for linha in aprovados:
        adicionar_resultado(linha.replace('\n', ''))
        
    botao_detalhes.configure(fg_color = AZUL, text = 'Ver Resumo', command = ver_resumo, state = 'normal')
    

''' Funções que lidam com os arquivos: ''' 

def baixar_pdf(url):
    mudar_status('Status: Baixando PDF.....', VERDE)
    
    try:
        pdf = get(url)
    except:
        return 1

    open(NOME_PDF, "wb").write(pdf.content)
    return 0

# Possui 'curso' como argumento para extrair apenas os dados dos candidatos desse curso e não precisar copiar tudo.
def extrair_dados_do_pdf_em_csv(nome_pdf, curso):  # Os dados extraídos são os presentes no cabeçalho.
    mudar_status('Status: Extraindo dados do PDF.....', AZUL)

    # Como há cursos noturnos com o mesmo nome dos diurnos, vamos checar se é noturno.
    noturno = False
    pos_noturno = 0
    if '(NOTURNO)' in curso:
        curso = curso.replace('(NOTURNO)', '').strip()
        noturno = True
    
    # Como há cursos no campus de Ceilândia com o mesmo nome dos nos outros campus, vamos checar se este é no Ceilândia.
    ceilandia = False
    pag_ceilandia = 0
    if '(CEILÂNDIA)' in curso:
        curso = curso.replace('CEILÂNDIA', '').strip()
        ceilandia = True
    
    # Não há cursos no campus de Gama com o mesmo nome dos nos outros campus, então, apenas retiraremos o nome '(GAMA)'.
    if '(GAMA)' in curso:
        curso = curso.replace('(GAMA)', '').strip()
        
    # Como há cursos no campus de Planaltina com o mesmo nome dos nos outros campus, vamos checar se este é em Planaltina.
    pag_planaltina = 0
    planaltina = False
    if '(PLANALTINA)' in curso:
        curso = curso.replace('(PLANALTINA)', '').strip()
        planaltina = True
    
    try:
        reader = PdfReader(nome_pdf)
    except:
        mudar_status('Status: Erro ao extrair dados do arquivo ' + nome_pdf, VERMELHO_CLARO)
        return 2

    n_paginas = len(reader.pages)

    achou_curso = False
    
    for c in arange(n_paginas):
        c = int(c)

        pagina = reader.pages[c]
        
        # Se retirar espaços e '\n' aumenta a chance de encontrar o curso, mesmo que a leitura do PDF não seja perfeita.
        texto = pagina.extract_text().replace(' ', '').replace('\n', '')
        
        # Se o curso a ser procurado é do campus Ceilândia, vamos checar se na página está escrito 'CEILÂNCIA' e guardar a página quando encontrar.
        if ceilandia:
            if 'CEILÂNCIA' in texto:  # O erro gramático é de propósito, no documento está assim.
                pag_ceilandia = c

        # Se o curso a ser procurado é do campus Planaltina, vamos checar se na página está escrito 'PLANALTINA' e guardar a página quando encontrar.
        if planaltina:
            if 'PLANALTINA' in texto:
                pag_planaltina = c
                pag_noturno = 0  # Reseta a página do noturno pois Planltina também tem cursos noturnos.
                
        # Se o curso a ser procurado é noturno, vamos checar se na página está escrito 'noturno' e guardar a página quando encontrar.
        if noturno:
            if 'NOTURNO' in texto:
                pag_noturno = c
                
        if not achou_curso:
            if curso in texto and pag_ceilandia <= c and pag_planaltina <= c and noturno <= c:  # Garante que a página está após a página que aparece o nome do campus ou 'noturno'.
                achou_curso = True

                texto = texto[texto.find(curso):]

                # No PDF das notas, os dados de cada candidato começa com a inscrição.
                texto = texto[texto.find(INICIO_INSCRICAO):] # Apaga qualquer texto antes dos dados do primeiro candidato.

                arquivo = open(NOME_CSV, 'a')

        # No PDF das notas, os dados do último candidato termina com '-.'.
        if achou_curso and '-.' in texto:
            texto = texto[:texto.find('-.') + 1]  # Apaga qualquer texto após os dados do último candidato.
            arquivo.writelines(texto)
            arquivo.close()
            return 0

        if achou_curso:
            arquivo.writelines(texto)
            
    if not achou_curso:
        mudar_status('Status: Erro ao extrair dados do arquivo, curso não encontrado', VERMELHO_CLARO)
        return 3

# Como ao extrair texto do PDF ele vem com uma formatação esquisita é necessário corrigí-lo.
def corrigir_dados_do_csv(nome_csv):
    mudar_status('Status: Corrigindo dados do CSV.....', 'yellow')

    try:
        arquivo = open(nome_csv, 'r')
    except FileNotFoundError:
        mudar_status('Erro ao corrigir os dados do csv pois o arquivo '+ nome_csv + 'não existe.', VERMELHO_CLARO)
        return 4

    copia = arquivo.read()  # Copia o arquivo em uma string.
    copia = copia.replace('/', '\n')  # Troca as "/" por "\n".
    copia = copia.splitlines()  # Separa as linhas em uma lista de linhas.

    for c in arange(len(copia)):
        c = int(c)

        if copia[c].isdigit():  # Apaga linhas que tenham apenas o número da página.
            copia[c] = ''

        # Apaga os nomes, eles ficam entre a 1ª e a 2ª vírgula.
        else:
            pos1 = copia[c].find(',')  # Posição da 1ª vírgula.
            pos2 = copia[c].find(',', pos1 + 1)  # Posição da 2ª vírgula.

            copia[c] = copia[c][:pos1] + copia[c][pos2:] + '\n'  # String com os dados, sem o nome, e com '\n' para separar por linhas.

    arquivo = open(nome_csv, 'w')
    arquivo.write(CABECALHO + ''.join(copia))
    arquivo.close()
    return 0


def extrair_dados_do_pdf_em_txt(nome_pdf):  # Os dados extraídos são apenas os números das inscrições dos aprovados.
    mudar_status('Status: Extraindo dados do PDF.....', AZUL)
    
    try:
        reader = PdfReader(nome_pdf)
    except:
        mudar_status('Status: Erro ao extrair dados do arquivo ' + nome_pdf, VERMELHO_CLARO)
        return 5

    n_paginas = len(reader.pages)

    arquivo = open(NOME_TXT, 'a')

    for c in arange(n_paginas):
        c = int(c)

        pagina = reader.pages[c]
        texto = pagina.extract_text()

        texto = texto.split()  # Separa as linhas em uma lista de linhas.

        for d in arange(len(texto)):
            d = int(d)

            if INICIO_INSCRICAO in texto[d]:
                texto[d] = texto[d][texto[d].find(INICIO_INSCRICAO):texto[d].find(INICIO_INSCRICAO) + TAMANHO_DA_INSCRICAO - 1] + '\n'  # Copia apenas a inscrição.
            else:
                texto[d] = ''

        arquivo.writelines(''.join(texto))

    arquivo.close()
    return 0


''' Funções que lidam com os dados já formatados pelas funções que lidam com os arquivos '''

# Essa função checa a partir das inscrições dos aprovados, suas notas e posições em cada cota, comparando os dois arquivos.
def checar_aprovados():
    # Abre os dois arquivos e copia os dados deles.
    with open(NOME_TXT, 'r') as aprovados_arquivo:
        aprovados = aprovados_arquivo.read()
    remove(NOME_TXT)

    with open(NOME_CSV, 'r') as dados_arquivo:
        dados = DictReader(dados_arquivo)

        # Lista para guardar cada dicionário com os dados dos candidatos aprovados.
        candidatos_aprovados = list()

        for candidato in dados:
            if candidato['inscricao'] in aprovados:
                candidatos_aprovados.append(candidato)

                # Essa lista guarda o valor numérico da cota a qual o candidato foi aprovado (a cota com a menor posição), e seu nome na versão resumida.
                menor_cota = [int(candidato['s1']), 's1']

                # Encontra a cota a qual o candidato foi aprovado (a cota com a menor posição).
                for s in arange(len(SIMBOLO_COTAS)):
                    # Se o candidato se inscreveu por essa cota e sua posição é menor que a menor posição nas cotas antes registradas.
                    if candidato[SIMBOLO_COTAS[s]] != '-' and int(candidato[SIMBOLO_COTAS[s]].replace('-', '')) < menor_cota[0]:
                        menor_cota[0] = int(candidato[SIMBOLO_COTAS[s]])
                        menor_cota[1] = SIMBOLO_COTAS[s]

                # Ao encontrar a cota a qual o candidato foi aprovado, atualiza os dados dessa cota registrando a nota desse candidato.
                registrar_cotas(candidato, menor_cota[1])
        
    remove(NOME_CSV)

    # Para mostrar todas as notas dos aprovados e suas posições em cada cota, elas são ordenadas da menor nota para a maior.
    candidatos_aprovados = sorted(candidatos_aprovados, key = itemgetter('nota'))

    # Optei por não adicionar as inscrições no arquivo das notas dos candidatos aprovados.
    for c in arange(len(candidatos_aprovados)):
        del candidatos_aprovados[c]['inscricao']
        candidatos_aprovados[c] = ','.join(list(candidatos_aprovados[c].values())) + '\n'

    with open('aprovados.txt', 'w') as aprovados_arquivo:
        aprovados_arquivo.writelines(candidatos_aprovados)
    
    # Mostra o resumo das notas dos aprovados na maior caixa de texto.
    ver_resumo()


# Essa função atualiza a lista os valores máximos, mínimos e a média de cada cota na lista 'resumo'.
def registrar_cotas(candidato, pos_cota):
    # Para checar a maior e a menor nota, além de calcular a média é necessário converte-la para float.
    nota = float(candidato['nota'])
    
    resumo[pos_cota].n_pessoas += 1
    resumo[pos_cota].soma_notas += nota

    if nota > resumo[pos_cota].max:
            resumo[pos_cota].max = nota

    if nota < resumo[pos_cota].min:
            resumo[pos_cota].min = nota
            
    resumo[pos_cota].calcular_media()
    

''' Janela: '''

# UI
customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('dark-blue')
customtkinter.set_widget_scaling(0.8)  # Para deixar em um tamanho que achei melhor sem precisar alterar muita coisa.

window = customtkinter.CTk(fg_color = '#2C1B1A')
window.title('Checador de notas')
window.geometry('770x560')
window.resizable(False, False)

FONTE = customtkinter.CTkFont(family = 'Cascadia Code', size = 20)
FONTE_MENOR = customtkinter.CTkFont(family = 'Cascadia Code', size = 15)
BUTTON_HEIGHT = 50
            
frame = customtkinter.CTkFrame(master = window, corner_radius = 12)
frame.pack(pady = (0, 30), padx = 30)

optionmenu = customtkinter.CTkOptionMenu(master = frame,
                                         dynamic_resizing = False,
                                         font = FONTE,
                                         dropdown_font = FONTE,
                                         height = BUTTON_HEIGHT,
                                         width = 140,
                                         values = ['TODOS', 'BACHARELADOS', 'LICENCIATURAS', 'NOTURNOS', 'CEILÂNDIA', 'GAMA', 'PLANALTINA'],
                                         command = mudar_valores_combobox)
optionmenu.grid(row = 0, column = 0, pady = (30, 0), padx = (100, 0), sticky = 'nsew')
optionmenu.set('TODOS')

combobox = customtkinter.CTkComboBox(master = frame,
                                     font = FONTE,
                                     dropdown_font = FONTE,
                                     height = BUTTON_HEIGHT,
                                     values = NOMES_DOS_CURSOS)
combobox.grid(row = 0, column = 1, columnspan = 1, pady = (30, 0), padx = (15), sticky = 'nsew')
combobox.set('Cursos')

botao_pesquisar = customtkinter.CTkButton(master = frame, font = FONTE, height = BUTTON_HEIGHT, fg_color = AZUL, text = 'Pesquisar', command = criar_arquivos)
botao_pesquisar.grid(row = 0, column = 2, pady = (30, 0), padx = (0, 100), sticky = 'nsew')

status = customtkinter.CTkTextbox(master = frame, font = FONTE, height = BUTTON_HEIGHT, state = 'disabled')
status.grid(row = 1, column = 0, columnspan = 3, pady = (25, 0), padx = 100, sticky = 'nsew')
mudar_status('Status: Insira o curso para começar')

resultado = customtkinter.CTkTextbox(master = frame, font = FONTE, height = 400, state = 'disabled')
resultado.grid(row = 2, column = 0, columnspan = 3, pady = (15, 25), padx = 50, sticky='nsew')

botao_detalhes = customtkinter.CTkButton(master = frame, font = FONTE, height = BUTTON_HEIGHT, width = 200, fg_color = CINZA, text = 'Ver Detalhes', command = ver_candidatos_aprovados_arquivo, state = 'disabled')
botao_detalhes.grid(row = 3, column = 1, pady = (0, 30), padx = (0, 220))

botao_sair = customtkinter.CTkButton(master = frame, font = FONTE, height = BUTTON_HEIGHT, width = 200, fg_color = VERMELHO, hover_color = VERMELHO_ESCURO, text = 'Sair', command = exit)
botao_sair.grid(row = 3, column = 1, pady = (0, 30), padx = (220, 0))

window.mainloop()
