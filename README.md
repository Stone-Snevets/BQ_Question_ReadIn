# BQ_Question_ReadIn
Receive Bible Quiz questions in PDF, DOC, DOCX format and break them down to specific introductions for analyzing

### Author: Solomon Stevens
### Date: *Enter Date Completed*

# Prerequisites
* Python 3 installed
* Git installed and configured correctly

# What is Bible Quiz
Bible Quiz is a ministry based out of the Assembly of God denomination. It encourages students ranging from 1st - 12th grade to engage in God's word through memorization. For the older levels of quizzing (6th-12th grade), portions of the Bible are selected each year, and questions are written based on the chosen portion. Throughout the schoolyear, teams from all over the country gather to compete in various levels of competition. Each round pits two teams against each other. There are twenty questions in each round, some 10 points, some 20 points, and some 30 points. Whichever team has more points at the end of the twenty questions is declared the winner of the round. There are a wide variety of introductory remarks designed to clue quizzers in as to what the question may be (see [list_of_intros]() for a complete list of introductory remarks and what they mean). To keep a competitive edge, teams may try to analyze past questions and look for patterns to help their quizzers even more.

# Basic Steps
1. Receive link to PDF, DOC, or DOCX file contianing Bible Quiz questions
   NOTE: the questions MUST be formatted correctly. See [question_formatting_rules](https://github.com/Stone-Snevets/BQ_Question_ReadIn/blob/main/question_formatting_rules.txt) for specifications as to how questions need to be formatted.
2. Open a csv file to write the question summary to
3. Begin reading in each question, examining the introduction parts and the question itself
   1. Determine what question parts are present. See [list_of_intros](https://github.com/Stone-Snevets/BQ_Question_ReadIn/blob/main/list_of_intros.txt) for a full set of valid introdictory remarks
   2. Write the included question parts into the csv file
   3. Read in the question
   4. Read in the reference(s) as to where the answer comes from
4. Once all questions are done, close both files

# Initial Setup
NOTE: The author is using a WINDOWS machine.  All code-related steps are for Windows
We begin by creating a virtual environment in which to create and run the code.  The point of a virtual environment is to keep different projects from interfering with other projects that may be on the same physical machine. 
\
`python -m venv .bqquestions2tablevenv`
\
From there, we activate it using
\
`.bqquestions2tablevenv\Scripts\activate`
\
Now we can clone over this repository.  The following command was used for such:
\
`git clone https://github.com/Stone-Snevets/BQ_Question_ReadIn.git`


# Resources
* [Newlines in Markdown](https://www.w3schools.io/file/markdown-line-break/)
* [Reading Files](https://www.w3schools.com/python/python_file_open.asp)
* [Reading Files Output]()
* [Reading User Input](https://www.w3schools.com/python/python_user_input.asp)
* [Setting up Virtual Environment](https://github.com/denisecase/datafun-01-textbook)
* [Understanding Virtual Environment](https://code.tutsplus.com/understanding-virtual-environments-in-python--cms-28272t)
* [Writing to a CSV File](https://www.pythontutorial.net/python-basics/python-write-csv-file/)
