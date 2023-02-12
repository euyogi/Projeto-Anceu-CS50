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


![IMG_20230212_121918](https://user-images.githubusercontent.com/46427886/218320104-99481e98-e56d-4936-80d2-8d2e1cf98472.png)
![IMG_20230212_121927](https://user-images.githubusercontent.com/46427886/218320105-39566226-8fca-42fc-a3a1-297be4a51d7e.png)
![IMG_20230212_121940](https://user-images.githubusercontent.com/46427886/218320106-2c5b545c-6dc3-4da8-b7ff-ee039b228f25.png)
![IMG_20230212_121951](https://user-images.githubusercontent.com/46427886/218320107-507a1a8b-5bf9-4577-82bf-12d8be47bdd9.png)
![IMG_20230212_122017](https://user-images.githubusercontent.com/46427886/218320109-57c5d25f-cc6a-47d4-a9fe-8220c65268c7.png)
![IMG_20230212_122051](https://user-images.githubusercontent.com/46427886/218320110-da69c9dd-1148-4521-8bd3-0e832f369bf5.png)
![IMG_20230212_122104](https://user-images.githubusercontent.com/46427886/218320112-03dee077-6f8c-48e5-a080-53bae4e27f24.png)
![IMG_20230212_122308](https://user-images.githubusercontent.com/46427886/218320113-da714646-3a33-4b99-8db1-340cc978c679.png)
![IMG_20230212_122317](https://user-images.githubusercontent.com/46427886/218320115-7738c1d2-e3da-42e6-823c-d589ebe66e88.png)
![IMG_20230212_122332](https://user-images.githubusercontent.com/46427886/218320116-d0a00156-5cf7-457c-b783-6845668b1279.png)
![IMG_20230212_122341](https://user-images.githubusercontent.com/46427886/218320119-468a96b9-e302-4257-9a7c-e05b85efeb36.png)
![IMG_20230212_122325](https://user-images.githubusercontent.com/46427886/218320120-b0aa64f9-3932-4130-8fa0-44f9131e0bba.png)
![IMG_20230212_121556](https://user-images.githubusercontent.com/46427886/218320121-3d943c12-0b58-4e1c-9d3b-343d8d0527a2.png)
![IMG_20230212_121808](https://user-images.githubusercontent.com/46427886/218320122-629c2a8b-6bf1-409e-96f4-d6f3e4f73110.png)![IMG_20230212_121855](https://user-images.githubusercontent.com/46427886/218320123-cf02ca76-4aec-4653-8f1a-5f5b4e722a42.png)
