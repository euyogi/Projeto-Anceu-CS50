# Projeto-CS50

Esse é o meu projeto final para o curso CS50 - é um aplicativo feito em python,
que checa as notas dos candidatos que participaram do Enem e se inscreveram na
Universidade de Brasília - UNB, mostrando por fim um resumo para cada
curso da instituição, com as maiores notas, as menores notas (nota de corte), e
a média em cada cota disponível.

É possível calcular também a sua própria nota, já que a universidade possui um
sistema de pesos para as notas de cada área.

Necessário instalar customtkinter, numpy, Pmw, pygame e requests com pip install
caso ainda não tenha-os instalados.

Além do click_sound.wav e do pdftotext.exe junto com o arquivo desse código.


Screenshots do programa:

* Tela Inicial
![photo1676213092](https://user-images.githubusercontent.com/46427886/218318041-9d811d31-d56b-4525-926c-71453e33f188.jpeg)

* Tela Informações
![photo1676213195](https://user-images.githubusercontent.com/46427886/218318057-89dd17f8-dc78-4802-8c39-d91ab6fc4f78.jpeg)

Tela Link Grupos
![photo1676213183](https://user-images.githubusercontent.com/46427886/218318072-a0a21a2d-f3d0-4acd-a992-9cde2a4a51c2.jpeg)

Tela Após Pesquisar Notas de Algum Curso (Nesse caso o curso pesquisado foi engenharias)
![image](https://user-images.githubusercontent.com/46427886/218318100-182c48bb-e681-4d95-82f6-b968720b1be9.png)

Tela Após Selecionar Ver Detalhes
![image](https://user-images.githubusercontent.com/46427886/218318637-38648814-28d1-4cc9-8fab-330706a8a14d.png)


Como vocês podem ver o programa possui:

* Uma caixa de opções para pesquisar/escolher o curso desejado

* Uma outra caixa de opções ao lado, com filtros para o tipo de curso (Bacharelado, licenciatura, ...)

* Opções para escolher o ano em que quer pesquisar as notas (2022, 2021...)

* Opções para escolher a chamada, para ver as notas de quem foi aprovado nessa chamada (1ª, 2ª...)

* Opção para ver uma lista com todas as notas e as respectivas posições dos candidatos aprovados separados por vírgulas (999.99,1,-,3...)

* Painel para aplicar os pesos da UnB à sua nota

* Entre outros...


Bom, escolhi criar esse programa pois eu tive bastante dificuldade para checar as notas para o curso que eu quero
e quase não havia informações na internet sobre as notas do ano de 2022, assim, por ser um processo que se manual
é bem trabalhoso tendo que comparar e pesquisar termos em dois PDFs e impossibilitado de ver as informações em uma
ordem, decidi criar esse programa, ele passou por diversos estágios desde um processo semi-automático em que era necessário
copiar os dados manualmente, para automático em que o programa baixava o PDF e extraia os dados com o aperto de um botão,
além de melhorias no desempenho que melhoraram o tempo de resposta em mais de 33x em alguns casos.

Apesar do programa ainda não ser acessível ao público geral, como em um site ou um aplicativo mobile ainda pude ajudar
dezenas de pessoas com as mesmas dificuldades que eu tive no começo com o programa:

Solarized dark             |  Solarized Ocean          |  Solarized dark
:-------------------------:|:-------------------------:|:-------------------------:
![IMG_20230212_121556](https://user-images.githubusercontent.com/46427886/218320654-9e24f341-b665-4fbc-bf4d-092dd43e8df1.png)|![IMG_20230212_121808](https://user-images.githubusercontent.com/46427886/218320686-2ccc6c78-dd03-49be-96fc-355722831061.png)

