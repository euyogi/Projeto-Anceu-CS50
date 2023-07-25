# Projeto-CS50

Esse é o meu projeto final para o curso CS50 - é um aplicativo feito <s>em python</s> agora em C++, que checa as notas dos candidatos que
participaram do Enem e se inscreveram na Universidade de Brasília - UnB, mostrando por fim um resumo para cada curso
da instituição, com as maiores notas, a média e as menores notas (nota de corte) em cada cota disponível.

É possível calcular também a sua própria nota, já que a universidade possui um sistema de pesos para as notas de cada área.

<h2>Tela Inicial:</h2>

![Imagem da tela inicial](https://user-images.githubusercontent.com/46427886/218318041-9d811d31-d56b-4525-926c-71453e33f188.jpeg)

<h2>Tela Informações:</h2>
 
![Imagem da tela de informações](https://user-images.githubusercontent.com/46427886/218318057-89dd17f8-dc78-4802-8c39-d91ab6fc4f78.jpeg)

<h2>Tela Link Grupos:</h2>

![Imagem da tela do link dos grupos](https://user-images.githubusercontent.com/46427886/218318072-a0a21a2d-f3d0-4acd-a992-9cde2a4a51c2.jpeg)

<h2>Tela Após Pesquisar Notas de Algum Curso (Nesse caso o curso pesquisado foi medicina):</h2>

![Imagem da tela após pesquisar algum curso](https://user-images.githubusercontent.com/46427886/218318100-182c48bb-e681-4d95-82f6-b968720b1be9.png)

<h2>Tela Após Selecionar Ver Detalhes:</h2>

![Imagem da tela após apertar o botão ver detalhes](https://user-images.githubusercontent.com/46427886/218318637-38648814-28d1-4cc9-8fab-330706a8a14d.png)


<h2>Funcionalidades:</h2>

* Uma barra de pesquisa com opções para pesquisar/escolher o curso desejado

* Opções para escolher o ano em que quer pesquisar as notas (2023, 2022 ou 2021)

* Opções para escolher a chamada, para ver as notas de quem foi aprovado nas outras chamadas (1ª, 2ª, 3ª...)

* Opção para ver uma lista com todas as inscrições, notas e as respectivas posições dos candidatos aprovados separados por vírgulas assim como nos pdfs (10000000, 999.99,5,-,1...)

* Painel para aplicar os pesos da UnB à sua nota

* Possibilidade de copiar os resultados facilmente

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

<h2>Para testar:</h2>

Baixe o programa aqui, se quiser ver o código e compilar você mesmo, uma solução do Visual Studio 2022 está disponível aqui.

<p align="center">
Projeto feito por: Yogi Nam de Souza Barbosa
</p>

<div align="center">
  <img src="https://user-images.githubusercontent.com/46427886/218377101-f832c1a3-6c48-4016-92d2-0d8b6a4fafd5.gif" width="10%" alt-text="Minha imagem de perfil (um cachorro)" />
</div>
