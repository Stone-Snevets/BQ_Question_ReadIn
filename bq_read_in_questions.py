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

"""

# ===== Preliminary ===============================================================================
# --- Libraries to Include ---
import csv # For Creating and Writing to a CSV File
import re # For working with Regular Expressions (RegEx)

# --- Constants ---
FILE_TO_WRITE_TO = 'output.csv'
HEADER = ['Set_Num', 'Q_Num', 'Pt_Val', 'Q_Intro', 'A_Intro','Location','Question','Ans_Reference']

# ===== Functions =================================================================================
# --- Get Question File ---
def get_question_file():
   """
   Function to ask user for the path of a file

   """
   # Ask User for File
   user_input = input('Enter the Full Path of the Question File: ')

   # Acknowledge to User that File Path was Received
   print(f'File Name: {user_input}\n')

   # Determine what kind of file is being entered
   #-> Figure out the file extension
   file_extension = re.findall('\.pdf|\.docx|\.doc', user_input)
      # returns a list containing the file extension
      # NOTE: DOCX must come before DOC in the search
      #       because the or (|) clause sees 'doc' without
      #       the x in 'docx' and automatically lists it
      #       as a DOC file rather than a DOCX file

   #-> Call appropriate function to extract the text from it
   try:
      print('\n FILE EXTENSION: ', file_extension, '\n')
      # If the file extension is PDF, call text_from_pdf()
      if file_extension[0] == '.pdf':
         text_from_pdf(user_input)

      # If the file extension is DOC, call text_from_doc()
      elif file_extension[0] == '.doc':
         text_from_doc(user_input)

      # If the file extension is DOCX, call text_from_docx()
      elif file_extension[0] == '.docx':
         text_from_docx(user_input)

   except: # The file type was not PDF, DOC, or DOCX
      # Output an Error Message
      print('------------------------------------------------------------------')
      print('ERROR: File Type Not Supported')
      print('Make sure the file you want to submit is either PDF, DOC, or DOCX')
      print('------------------------------------------------------------------\n')

      # Return back to Main - There's nothing more the program can do
      return


   # Call process_questions and Pass the File Path
   #process_questions(user_input)

   #-DUMMY---------------------------#
   print('\nProcessing Complete\n')  #
   #-END-DUMMY-----------------------#

# --- Extract the text from PDF files ---
def text_from_pdf(file_name):
   """
   Function to pull and return the text from a PDF file for further processing

   """
   # Import pypdf for working with the PDF file

   # Extract the text from the document

   # Return the extracted text
   
   #-DUMMY--------#
   print('pdf')   #
   #-END-DUMMY----#


# --- Extract the text from DOC files ---
def text_from_doc(file_name):
   """
   Function to pull and return the text from a DOC file for further processing

   """
   # Import pywin32 for working with the DOC file

   # Extract the text from the document

   # Return the extracted text
   
   #-DUMMY--------#
   print('doc')   #
   #-END-DUMMY----#


# --- Extract the text from DOCX files ---
def text_from_docx(file_name):
   """
   Function to pull and return the text from a DOCX file for further processing

   """
   # Import docx2txt for working with the DOCX file

   # Extract the text from the document

   # Return the extracted text
   
   #-DUMMY---------#
   print('docx')   #
   #-END-DUMMY-----#

# --- Process Questions ---
def process_questions(question_file_path):
   """
   Function to -> process all questions in a file received from "get_question_file"
               -> send all findings to a csv file

   """
   # Open a csv file to write to
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