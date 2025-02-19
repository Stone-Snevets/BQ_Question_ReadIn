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
   a. Find the question number and point value
   b. Determine the question introductory remarks
   c. Determine the answer intoructory remarks
   d. Determine the location introductory remarks
   e. Copy over the question
   f. Copy over the verse reference(s) where the answer is coming from
5. Write appropriate introductory remarks to the csv file
6. Close both files

"""

# ===== Preliminary ===============================================================================
# --- Libraries to Include ---
import csv # For Creating and Writing to a CSV File

# --- Constants ---
FILE_TO_WRITE_TO = 'output.csv'
HEADER = ['Set_Num', 'Q_Num', 'Pt_Val', 'Q_Intro', 'A_Intro','Location','Question','Ans_Reference']

# ===== Functions =================================================================================
# --- Get Question File ---
def get_question_file():
   """
   Function to ask user for the path of a file

   """
   #-> Ask User for File
   user_input = input('Enter the Full Path of the Question File: ')

   #-> Acknowledge to User that File Path was Received
   print(f'File Name: {user_input}\n')

   #-> Call process_questions and Pass the File Path
   process_questions(user_input)

   #-DUMMY-----------------------#
   print('\nProcessing Complete\n')  #
   #-END-DUMMY-------------------#

# --- Process Questions ---
def process_questions(question_file_path):
   """
   Function to process all questions in a file received from "get_question_file"
               send all findings to a csv file

   """
   #-> Open the user-given file
   with open(question_file_path, "r") as input_file:

      #-> Open a csv file to write to
      with open(FILE_TO_WRITE_TO, 'w') as output_file:
        
         # Create a Writer Object to write with
         writer = csv.writer(output_file)

         # Write a Header Row
         writer.writerow(HEADER)

         #-> For each question
#--> Determine Question Number
#--> Determine Point Value
#--> Check for Question, Answer, and/or Location Introductory Remarks
#---> If none of any, skip that function
#--> Copy over the question
#--> Find the reference(s) of the answer

# --- Determine Question Introductory Remarks ---

# --- Determine Answer Introductory Remarks ---

# --- Determine Location Introductory Remarks ---

# ===== Main ======================================================================================
if __name__ == "__main__":
   #-> Call function to get a question file
   get_question_file()

   #-> Inform User that process is complete
   print('Question Reading Process Complete')