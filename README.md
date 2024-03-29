# Projeto-Anceu-CS50

<img alt="Header" width=100% src="https://capsule-render.vercel.app/api?type=waving&color=b03955&height=100&section=header">

Esse é o meu projeto final para o curso CS50 - é um aplicativo que <ins>a</ins>nalisa as <ins>n</ins>otas de <ins>c</ins>orte do <ins>e</ins>nem para a <ins>U</ins>nB, feito <s>em python</s> agora em C++, que checa as notas dos candidatos que participaram do Enem e se inscreveram na Universidade de Brasília - UnB, mostrando por fim um resumo para cada curso
da instituição, com as maiores notas, a média e as menores notas (nota de corte) em cada cota disponível.

É possível calcular também a sua própria nota, já que a universidade possui um sistema de pesos para as notas de cada área.


<h2>Para testar:</h2>

Baixe o programa <a href="https://github.com/euyogi/Projeto-CS50/releases/download/release/Anceu.exe">aqui</a> [WINDOWS] (desenvolvido para windows 11 mas funcionou em outras versões nos meus testes).

Se quiser ver o código e compilar você mesmo, baixe o .zip com todos os arquivos, nele se você quiser compilar com Visual Studio tem uma solução do Visual Studio 2022, além de ser possível compilar também com CMake. Ambos disponíveis na pasta new_cpp_app e a antiga versão Python em old_python_app, baixe o .zip <a href="https://github.com/euyogi/Projeto-CS50/archive/refs/heads/main.zip">aqui</a>.

<h2>Tela Inicial:</h2>

<p align="center">
  <img alt="Tela inicial" width="75%" src="https://github.com/euyogi/Projeto-Anceu-CS50/assets/46427886/3c0c855b-b918-4258-83b1-3dd41b5871f0">
</p>

<h2>Pesquisando Curso:</h2>

<p align="center">
  <img alt="Pesquisando curso" width="75%" src="https://github.com/euyogi/Projeto-Anceu-CS50/assets/46427886/a47fb9d9-548e-4c2d-ad7d-1e8184faa573">
</p>

<h2>Tela Após Pesquisar Notas de Algum Curso (Nesse caso o curso pesquisado foi medicina):</h2>

<p align="center">
  <img alt="Após pesquisar curso" width="75%" src="https://github.com/euyogi/Projeto-Anceu-CS50/assets/46427886/5fb00d78-8edc-4603-b2be-926bb5ebc7a1">
</p>

<h2>Tela Após Selecionar Ver Detalhes:</h2>

<p align="center">
  <img alt="Após selecionar ver detalhes" width="75%" src="https://github.com/euyogi/Projeto-Anceu-CS50/assets/46427886/71550219-9078-4a7a-b0ea-9b196eefbf8b">
</p>

<h2>Funcionalidades:</h2>

* Uma barra de pesquisa com opções para pesquisar/escolher o curso desejado
* Opções para escolher o ano em que quer pesquisar as notas (2023, 2022 ou 2021)
* Opções para escolher a chamada, para ver as notas de quem foi aprovado nas outras chamadas (1ª, 2ª, 3ª...)
* Opção para ver uma lista com todas as inscrições, notas e as respectivas posições dos candidatos aprovados separados por vírgulas assim como nos pdfs (10000000, 999.99,5,-,1...)
* Painel para aplicar os pesos da UnB à sua nota
* Possibilidade de copiar os resultados facilmente
* Possibilidade de dar zoom na maior caixa de texto (a que aparece os resultados) para melhor visualização

<h2>Diferença da nova versão em C++:</h2>

* De (em alguns casos como medicina) 10s para menos de 1s para pesquisar notas do curso
* A versão .exe anterior tinha mais de 30mb e só funcionava com diversos arquivos .dll, agora é menos de 5mb e funciona sozinha (teoricamente, ainda tenho que testar)
* Agora a barra de pesquisa vai mostrando o nome dos cursos similares ao que você está digitando (muito bom)
* O menu com a lista de cursos agora tem uma barra de rolagem (graças a deus)
* Agora o programa é dimensionável e suporta diferentes escalas do windows (100%, 125%, etc...) (antes se mudasse a escala textos ficariam estranhos)
* O tamanho padrão da janela é menor que antes
* Agora da para dar zoom na maior caixa de texto
* Ao pesquisar a barra de progresso funciona durante todo o processo (antes era só enquanto estava baixando os pdfs)
* Não criamos mais um arquivo .txt com os resultados (você ainda pode copiar os resultados)
* A parte onde insere suas notas agora só aceita números e formata automaticamente eles (para o formato 000.00)
* É possível abrir os links da tela de informações 
* As dicas agora tem bordas arredondadas
* Mudança do som do clique
* Mudança da fonte (Cascadia Code para Ubuntu Mono Regular)
* Mudança do ícone (antes era o padrão do customtkinter)
* Adicionado opções de 2023, removido opções de 2020
* Otimizações se for pesquisar cursos do mesmo ano e chamada em seguida

<h2>Bibliotecas e códigos:</h2>

Toda a interface do programa é feita com <a href="https://github.com/ocornut/imgui">Dear ImGui</a> e a barra de pesquisa foi feita
pelo khlorz e está disponível <a href="https://github.com/khlorz/imgui-combo-filter">aqui</a>,
apesar de ter feito algumas alterações mínimas em ambos.
Também utilizei <a href="https://www.codeproject.com/articles/7056/code-to-extract-plain-text-from-a-pdf-file">esse código</a> do NeWi para começar o conversor de pdf.
(Por isso o nome Neyo -> NeWi + Yogi)
<h2>Escolhas:</h2>

Bom, escolhi criar esse programa pois eu tive bastante dificuldade para checar as notas para o curso que eu quero
e quase não havia informações na internet sobre as notas do ano de 2022, assim, por ser um processo que se manual
é bem trabalhoso tendo que comparar e pesquisar termos em dois PDFs e impossibilitado de ver as informações organizadinhas,
decidi criar esse programa, ele passou por diversos estágios desde um processo semi-automático em que era necessário
copiar os dados manualmente, para automático em que o programa baixava o PDF e extraia os dados com o aperto de um botão,
além de melhorias no desempenho, até por fim uma nova versão em C++ mais polida e muito mais rápida, leve e agora com
uma versão .exe (executável para windows) facilmente baixável.

Apesar do programa não ser nada muito grande, nem ser super portável como um site ou
um aplicativo mobile ainda pude ajudar dezenas de pessoas com as mesmas dificuldades que
eu tive no começo com o programa:

<div>
  <img src= "https://user-images.githubusercontent.com/46427886/218320799-b91f68ee-b1e1-4c8b-9fb5-5468b04a81d9.png" width="32%" alt-text="Imagem de pessoas foram ajudadas" />
  <img src="https://user-images.githubusercontent.com/46427886/218320829-f5b17ce9-dfe2-4071-b8d9-32db85629928.png" width="32%" alt-text="Imagem de pessoas foram ajudadas" /> 
  <img src="https://user-images.githubusercontent.com/46427886/218320832-d2756cbf-6056-44c9-9d0a-dfa1cedafeab.png" width="32%" alt-text="Imagem de pessoas foram ajudadas" />
</div>
<div>
  <img src= "https://user-images.githubusercontent.com/46427886/218329386-b3c500fa-bd21-4558-bf72-4ca69539eff8.png" width="32%" alt-text="Imagem de pessoas ajudadas" />
  <img src="https://user-images.githubusercontent.com/46427886/218320834-bd4dac48-3fc4-400f-a614-88d5b03bf956.png" width="32%" alt-text="Imagem de pessoas ajudadas" /> 
  <img src="https://user-images.githubusercontent.com/46427886/218320835-4a579395-d23f-400e-a59f-ceb6e97a2215.png" width="32%" alt-text="Imagem de pessoas ajudadas" />
</div>
<div>
  <img src= "https://user-images.githubusercontent.com/46427886/218320836-2bb2411e-5a9e-43ce-8235-3a4cec75a404.png" width="32%" alt-text="Imagem de pessoas ajudadas" />
  <img src="https://user-images.githubusercontent.com/46427886/218320837-3f628db3-850b-4943-a036-d2552aeb2a12.png" width="32%" alt-text="Imagem de pessoas ajudadas" /> 
  <img src="https://user-images.githubusercontent.com/46427886/218320838-39f0920b-0952-4bf6-9710-713838778827.png" width="32%" alt-text="Imagem de pessoas ajudadas" />
</div>
<div>
  <img src= "https://user-images.githubusercontent.com/46427886/218320841-71459d9b-e5fe-4f20-b418-f2621bd71dd9.png" width="32%" alt-text="Imagem de pessoas ajudadas" />
  <img src="https://user-images.githubusercontent.com/46427886/218320843-6cc8348d-7e8d-471e-a017-18b6b81f4c70.png" width="32%" alt-text="Imagem de pessoas ajudadas" /> 
  <img src="https://user-images.githubusercontent.com/46427886/218320844-0586deb6-31d5-457f-b5f3-79a5492f366a.png" width="32%" alt-text="Imagem de pessoas ajudadas" />
</div>
<div>
  <img src="https://user-images.githubusercontent.com/46427886/218320845-a15fc401-f331-4ba7-ac1b-3fc79d4c2efe.png" width="32%" alt-text="Imagem de pessoas ajudadas" />
  <img src="https://user-images.githubusercontent.com/46427886/218320846-2dcb3610-cfbb-41d9-9d93-74fd1834ec0c.png" width="32%" alt-text="Imagem de pessoas ajudadas" /> 
  <img src="https://user-images.githubusercontent.com/46427886/218329385-ad9ab4a2-49a4-4c29-a3c2-22456845330b.png" width="32%" alt-text="Imagem de pessoas ajudadas" />
</div>

<h2>Como era o programa em Python? (muito parecido, pelo menos em visual)</h2>

<div>
  <img src= "https://user-images.githubusercontent.com/46427886/218318041-9d811d31-d56b-4525-926c-71453e33f188.jpeg" width="49%" alt-text="Tela inicial Python" />
  <img src="https://user-images.githubusercontent.com/46427886/218318100-182c48bb-e681-4d95-82f6-b968720b1be9.png" width="49%" alt-text="Tela após pesquisar curso (engenharias) Python" /> 
</div>
<div>
  <img src="https://user-images.githubusercontent.com/46427886/218318637-38648814-28d1-4cc9-8fab-330706a8a14d.png" width="49%" alt-text="Tela após clicar botão ver detalhes Python" />
 <img src="https://user-images.githubusercontent.com/46427886/218318057-89dd17f8-dc78-4802-8c39-d91ab6fc4f78.jpeg" width="49%" alt-text="Tela após clicar botão ver detalhes Python" />
</div>
<p align="center">
Projeto feito por: Yogi Nam de Souza Barbosa
</p>

<img alt="Footer" width=100% src="https://capsule-render.vercel.app/api?type=waving&color=b03955&height=100&section=footer">
