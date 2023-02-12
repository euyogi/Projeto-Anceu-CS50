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

![IMG_20230212_122325](https://user-images.githubusercontent.com/46427886/218320443-9317b3f7-7120-46b9-8a7f-ff81b2008939.png) ![alt-text-1](image1.png "title-1") ![alt-text-2](image2.png "title-2")
![IMG_20230212_121556](https://user-images.githubusercontent.com/46427886/218320446-4f295d9c-8da6-4504-a338-e3a5c2bf83c3.png)
![IMG_20230212_121808](https://user-images.githubusercontent.com/46427886/218320447-f10b8d9e-ef10-43b5-9e66-034951c427c3.png)
![IMG_20230212_121855](https://user-images.githubusercontent.com/46427886/218320448-909f174d-cc3c-4771-be9e-01924e3ea45f.png)
![IMG_20230212_121918](https://user-images.githubusercontent.com/46427886/218320449-b1d9f169-1399-4414-aa4c-2d3710cfe8ec.png)
![IMG_20230212_121927](https://user-images.githubusercontent.com/46427886/218320450-f792eab6-6143-4bf3-8194-9113c91c61dc.png)
![IMG_20230212_121940](https://user-images.githubusercontent.com/46427886/218320451-5a45e56a-ca0f-4a60-a39c-b1a16706549f.png)
![IMG_20230212_121951](https://user-images.githubusercontent.com/46427886/218320452-ea7d55aa-e8ce-4a61-a6ec-d154d675a9fd.png)
![IMG_20230212_122017](https://user-images.githubusercontent.com/46427886/218320453-a01a70cc-78bf-43a0-baf4-73c6eeedf238.png)
![IMG_20230212_122051](https://user-images.githubusercontent.com/46427886/218320454-30155e54-eebe-4e55-9512-1db89f4a2427.png)
![IMG_20230212_122104](https://user-images.githubusercontent.com/46427886/218320455-aa660ce5-27a8-4950-81fa-ba930d2c2129.png)
![IMG_20230212_122308](https://user-images.githubusercontent.com/46427886/218320456-ba28d044-e986-42bd-9acd-b70617a9129f.png)
![IMG_20230212_122317](https://user-images.githubusercontent.com/46427886/218320458-58156ba9-4fe3-4e01-bb0e-6a92dfdfd39c.png)
![IMG_20230212_122332](https://user-images.githubusercontent.com/46427886/218320459-66b58f18-c712-4a91-8297-2eb7b28aa33f.png)
![IMG_20230212_122341](https://user-images.githubusercontent.com/46427886/218320461-6dc7827f-00e0-4e07-8ea3-a64dbbcb7764.png)
