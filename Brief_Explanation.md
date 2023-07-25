# Anceu (Grade Analyzer)
#### Description: A <s>Python</s> C++ app made to solve a real problem

My project was made in <s>Python</s> C++ it is a GUI app, that has 2 main functionalities:

* The first one let's you select a course from the University of Brasília (The main federal university in Brazil's capital) and then it displays like a table with the highest grade, the lowest grade, and the average grade of the approved students in each quota that the university provides of the past selective processes, so that we, students, can have an idea of the performance needed to be approved.

* The second one is a grade converter, as the university has different weights for different course areas (a weight for humanities courses and a weight for exact sciences), and the grades shown in the table after your search already has those weights applied, so you need to convert your grade to compare because it can change depending on the desired area.

it works as a standalone .exe

The data:

To understand the code first we need to understand the data used to get the grades and the approved ones, those are in two different pdf files, available on a site called cebraspe, that is the site that the university uses on those selective processes to publish opening notices and stuff.

The data in the first pdf is like that (not so perfect, because there is a lot of text explaining the formatting and the document in general first):

```
COURSE NAME

10012345,Student Name,999.99, 1, -, -, -, -, -, -, -, -, -/10098765,Student Name,499.99, 42, -, -, -, -, -, -, -, -, -/.../
10042424, Student Name,700.00, 30, -, 1, -, 2, -, -, 3, -, 4.

ANOTHER COURSE NAME

...
```

The "..." shows that it repeats thousands of times, as there are thousands of applicants, the 8 character long number is the registration number of the applicant, The "000.00" number after the name is the grade, and the 10 spaces after are the positions of the applicant in each quota.

The data in the second pdf has, as the first one, a bunch of text explaining the document but the main part has the registration number and name of each approved applicant.

So to get the grades of each approved we need to compare the two pdf files data. We just need to, for each registration number in the second pdf, search for them in the first pdf, and get the grade and positions of them, but like that it would get grades and positions of every approved of every course, so before that we need to get just the piece of data from the first pdf that contains only the data from the course that we want to search. Then we can extract that and organiza it into a string to the user.

Now, talking about the code, first it was made in Python, with customtkinter for the GUI and a PyMuPDF to extract the text from those pdfs, it worked but it was slow and couldn't be a standalone .exe which was actually my goal, another main problem was that it couldn't resize and adapt to different dpis, but that was on me.

Now that I rewrote it in C++ I did with Dear ImGui for the GUI a very good library indeed, and this <a href="https://github.com/khlorz/imgui-combo-filter">imgui widget code</a> from khlorz and used zlib to extract the text from the pdf with the help of <a href="https://www.codeproject.com/articles/7056/code-to-extract-plain-text-from-a-pdf-file">this code</a> I changed it a little bit to my needs (no page numbers, no spaces or endlines, not save to a file but to a string) but it was my starting point, after that first I made console application version then converted to functions to be called from the gui buttons.

So the algorithm, first we select a course, and search, we will download the pdfs from the selected year and call, then we'll convert both and call the function to extract the grades, for that we pass the course name, so we extract the registrations into a set, analyze the course name (to see if the campus and it's shift) if it has a specific campus we first look where the grades from that campus starts on the grades pdf, then if it has a specific shift we look from the point where we are where the grades from that shift starts, then finally from where we are we look for the course, after we found it we look for registrations, check if they are on the approved set, if they are store them, the grades and positions, after we finish that we just check in what quota was the candidate approved in, and sort it, then we organize it into the final string that we'll show to the user, the process was very similar in Python and in C++ but C++ was way faster, tooking, in my machine (an outdated notebook), to convert the pdfs (about 200-400 pages) (longest part of all this proccess) about 150ms.

Well, that's basically it, it was wonderful making that app, learned a lot in the process, and could at the end help real people with it. Oh and I chose downloading and converting the pdf for when years pass it's easy to just put two more urls in the list and the app can analyze the grades, if they release a new pdf with newer data it's easier to update too, it works very good. 

