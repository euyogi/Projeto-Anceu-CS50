# Grade Analyzer
#### Video Demo:  <URL HERE>
#### Description: A Python app made to solve a real problem

My project was made in Python it is a GUI app, that has 2 main functionalities:

* The first one let's you select a course from the University of Brasília (The main federal university in Brazil's capital) and then it displays like a table with the highest grade, the lowest grade, and the average grade of the approved students in each quota that the university provides of the past selective processes, so that we, students, can have an idea of the performance needed to be approved.

* The second one is a grade converter, as the university has different weights for different course areas (a weight for humanities courses and a weight for exact sciences), and the grades shown in the table after your search already has those weights applied, so you need to convert your grade to compare because it can change depending on the desired area.

it has mainly 2 files:

* app.py

* click_sound.wav

app.py has the code and click_sound.wav is the sound it reproduces when you click stuff in the app.

The data:

To understand the code first we need to understand the data used to get the grades and the approved ones, those are in two different pdf files, available on a site called cebraspe, that is the site that the university uses on those selective processes to publish opening notices and stuff.

The data in the first pdf is like that (not so perfect, because there is
a lot of text explaining the formatting and the document in general):

COURSE NAME

10012345,Student Name,999.99, 1, -, -, -, -, -, -, -, -, -/10098765,Student Name,499.99, 42, -, -, -, -, -, -, -, -, -/.../10042424, Student Name,700.00, 30, -, 1, -, 2, -, -, 3, -, 4.

ANOTHER COURSE NAME

...

The "..." shows that it repeats thousands of times, as there are thousands of applicants, the 8 character long number is the subscription number of the applicant, The "000.00" number after the name is the grade, and the 10 spaces after are the positions of the applicant in each quota.

The data in the second pdf has, as the first one, a bunch of text explaining the document but the main part has the subscription number and name of each approved applicant.

So to get the grades of each approved we need to compare the two pdf files data. We just need to, for each subscription number in the second pdf, search for them in the first pdf, and get the grade and positions of them, but like that it would get grades and positions of every approved of every course, so first we need to get just a piece of data from the first pdf that contains only the data from the course that we want to search.

Now finally to the code itself

First I declared some variables like the two urls of the pdf files, two names for the pdf files, 10 quotes names, a lot of course names, then UI stuff, then functions like the main functions, an UI function, a welcome message function, and the search function (when you press search button), that mainly calls the functions to download, convert to text, format the pdf data, and show the results on the screen, it also handles errors that can happen like connection or other stuff, showing error messages on the GUI.

Now a brief explaining on each of the others functions

* "baixar_pdf" downloads the pdf files, it handles exceptions and it creates the files accordingly to the names passed to it, and I pass the names declared in the variables before

* "extrair_dados_do_pdf" converts the pdf that has grades and positions to text, first it converts everything but after it gets only the data of the desired course, i used PyMuPDF to convert to text, replace method to get rid of spaces or \n to make the data more consistent, and regex to get the right positions to "crop" the text I want, that is only the data of the desired course.

* "corrigir_dados" basicly it gets the data got before and splits it into lists, each list has like one candidate positions and grade, it also handles the format of pdf files in the years before, that was different, changing it a little bit.

* "extrair_inscricoes_do_pdf" gets the subscription numbers of every approved one, similar to before it uses PyMuPDF to convert, replace method, and regex to get the subscriptions numbers.

* "checar_aprovados" that function like compare the subscription number of every approved one and the grades/positions of the selected course, and insert the approved ones grades in the list respective to the quote that the candidate was approved for, for that we check the quote in each he got the best position first. I also deleted names and subscription numbers of the data that we actually had because it doesn't have value for the students actually checking the performance of those candidates, and a list with every grade and positions is stored into a file called "aprovados.txt", after we open that file if we want to see it in the app, and it's also available in the directory in each the app is to open manually.

* "ver_resumo_das_notas_na_maior_caixa" It shows how many were approved in each quote and the max, min, average grade in each quote of the course searched, basically displays what we got with the data.

* "ver_dados_candidatos_aprovados_na_maior_caixa" That txt file I talked before, that function reads it and shows on the text box, all the grades/positions of each approved candidate. (when you press "Ver Detalhes" button)

* "remover_pdfs" Try removing the pdf files it's called when we close the app, not before because we may want to search another course, and to save time we just search the pdf for the desired course data again.

* "balao" shows like a balloon message when hovering some buttons in the app like the ones with "?" and "i".

* "converter" Converts the grades inserted by the user to the area choosen, like exact sciences or humanities.

* "ver_info" Shows some information about me and the app to the user. (When you press "!" button)

* "ver_url_grupo" Shows a url to check what is the area of the course you want and some more informations about the process of that university. (When you press "i" button)

* "mudar_opcoes_menu_cursos" It's for filtering the courses in the dropdown like when you choose "BACHARELADOS" that's bachelors, it shows only bachelors courses in the dropdown. (called in the select menu at the side of the main dropdown)

* "mudar_ano_e_chamada" That changes the content of the two url variables at the top of the code, changing so the pdf we download and get the data, for selecting different years and calls of the selective process of the university for your course. (called when you choose different options in the select buttons)

* "mudar_status" that changes the status text we have in the little text box, it's called mainly on the search function to show it's searching, if we got an error, or if everything went well after finished.

* "adicionar_na_maior_caixa" that changes the text we have in the big box, used for all functions that shows something in the big box, like when we press the "i" buttons, or when finishing searching the course grades.

* "som_clique" reproduces the click sound

Well, that's basically it, it was wonderful making that app, learned a lot in the process, and could at the end help real people with it. Oh and I chose downloading and converting the pdf for when years pass it's easy to just put two more urls in the list and the app can analyze the grades, if they release a new pdf with newer data it's easier to update too, I also changed the pdf converter some times, first I tried PdfReader2 I think, and it was very slow, then pdftotext.exe with subprocess library, but it was .exe and when I made the app a .exe it would open terminals, finally PyMuPDF and it works very good. 





