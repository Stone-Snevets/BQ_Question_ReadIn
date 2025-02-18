"""
Program to read in and summarize Bible Quiz questions based on their introductory remarks
-> See "list_of_intros" in this repository for a full list / description of introductory remarks

Written by Solomon Stevens
Date Completed:

------- Basic Steps -------
1. Ask user for PDF, DOC, or DOCX file containing questions
   -> See "question_formatting_rules" for how questions should be formatted
2. Open given file
3. Open csv file to write information to
4. For each question
   a. Determine the question introductory remarks
   b. Determine the answer intoructory remarks
   c. Determine the location introductory remarks
   d. Copy over the question
   e. Copy over the verse reference(s) where the answer is coming from
5. Write appropriate introductory remarks to the csv file
6. Close both files

"""