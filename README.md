# BQ_Question_ReadIn
Receive Bible Quiz questions in PDF, TXT, DOCX format and break them down to specific introductions for analyzing

### Author: Solomon Stevens
### Date: April 2nd, 2025

# Prerequisites
* Python 3 installed
* Git installed and configured correctly

# What is Bible Quiz
Bible Quiz is a ministry based out of the Assembly of God denomination. It encourages students ranging from 1st - 12th grade to engage in God's word through memorization. For the older levels of quizzing (6th-12th grade), portions of the Bible are selected each year, and questions are written based on the chosen portion. Throughout the schoolyear, teams from all over the country gather to compete in various levels of competition. Each round pits two teams against each other. There are twenty questions in each round, some 10 points, some 20 points, and some 30 points. Whichever team has more points at the end of the twenty questions is declared the winner of the round. There are a wide variety of introductory remarks designed to clue quizzers in as to what the question may be (see [list_of_intros](https://github.com/Stone-Snevets/BQ_Question_ReadIn/blob/main/list_of_intros.txt) for a complete list of introductory remarks and what they mean). To keep a competitive edge, teams may try to analyze past questions and look for patterns to help their quizzers even more.

# Basic Steps
1. Receive link to PDF, TXT, or DOCX file contianing Bible Quiz questions
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
The process begins by creating a virtual environment in which to create and run the code.  The point of a virtual environment is to keep different projects from interfering with other projects that may be on the same physical machine. 
\
`python -m venv .bqquestions2tablevenv`
\
The virtual machine can now be activated using
\
`.bqquestions2tablevenv\Scripts\activate`
\
Now clone over this repository.  The following command was used for such:
\
`git clone https://github.com/Stone-Snevets/BQ_Question_ReadIn.git`
\
Before installing necessary packages (using pip), a good idea would be to first check if there is anything we can update.
\
`python -m pip install --upgrade pip`
\
Now everything is ready to install any external packages needed for this project
* `pip install pypdf2` - Extracts the text from PDF files
* `pip install docx2txt` - Extract the text from DOCX files
* `pip install pandas` - Create and manipulate data using Pandas Dataframes


# Resources
* [Add New Column to Pandas Dataframe](https://www.geeksforgeeks.org/how-to-add-empty-column-to-dataframe-in-pandas/#)
* [Appending to Strings](https://www.geeksforgeeks.org/initialize-empty-string-in-python/)
* [Browsing for a File](https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/)
* [Calling separate Python script](https://www.geeksforgeeks.org/run-one-python-script-from-another-in-python/#)
* [Check Boxes using tkinter](https://www.geeksforgeeks.org/python-tkinter-checkbutton-widget/)
* [Determine the type of a variable](https://r.search.yahoo.com/_ylt=AwrFDNsJ48Fn2AIAe8NXNyoA;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3Ny/RV=2/RE=1741969418/RO=10/RU=https%3a%2f%2fstackoverflow.com%2fquestions%2f402504%2fhow-to-determine-a-python-variables-type/RK=2/RS=U5bQmz1DCApWoOYTwkb0TkqPJcU-)
* [docx2txt Documentation](https://pypi.org/project/docx2txt/)
* [Find part of a string in pandas DataFrame] (https://note.nkmk.me/en/python-pandas-str-contains-match/#partial-match-contains-specific-string-strcontains)
* [Fix utf-8 Error Reading in Quotation Marks](https://stackoverflow.com/questions/55563399/how-to-solve-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-positio)
* [Multi-Conditional If Statements](https://www.w3schools.com/python/python_conditions.asp)
* [Newlines in Markdown](https://www.w3schools.io/file/markdown-line-break/)
* [pywin32 Doesn't Work on Machines without MS Office](https://stackoverflow.com/questions/62427468/com-error-2147221005-invalid-class-string-none-none)
* [Reading DOCX Files](https://theautomatic.net/2019/10/14/how-to-read-word-documents-with-python/)
* [Reading PDF Files](https://pypdf2.readthedocs.io/en/3.x/user/extract-text.html)
* [Reading User Input](https://www.w3schools.com/python/python_user_input.asp)
* [Regular Expressions in Python](https://www.w3schools.com/python/python_regex.asp)
* [Regular Expressions Documentation](https://docs.python.org/3/library/re.html)
* [Regular Expressions in the Middle of a String](https://stackoverflow.com/questions/28840903/python-regex-match-middle-of-string)
* [Remove the First n Characters from a String](https://stackoverflow.com/questions/11806559/removing-first-x-characters-from-string)
* [Searching for Text within a String](https://www.w3schools.com/python/python_strings.asp)
* [Setting up Virtual Environment](https://github.com/denisecase/datafun-01-textbook)
* [Understanding Virtual Environment](https://code.tutsplus.com/understanding-virtual-environments-in-python--cms-28272t)
* [Why Spire.Doc Fails](https://www.e-iceblue.com/forum/limitation-t10856.html)
* [Why 'textract' Fails](https://stackoverflow.com/questions/67130147/textract-cannot-find-a-pdf-file-python)
* [Writing to a CSV File](https://www.pythontutorial.net/python-basics/python-write-csv-file/)
