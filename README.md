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


Como vocês podem ver o programa possui:

* Uma caixa de opções para pesquisar/escolher o curso desejado

* Uma outra caixa de opções ao lado, com filtros para o tipo de curso (Bacharelado, licenciatura, ...)

* Opções para escolher o ano em que quer pesquisar as notas (2022, 2021...)

* Opções para escolher a chamada, para ver as notas de quem foi aprovado nessa chamada (1ª, 2ª...)

* Opção para ver uma lista com todas as notas e as respectivas posições dos candidatos aprovados separados por vírgulas (999.99,1,-,3...)

* Painel para aplicar os pesos da UnB à sua nota
