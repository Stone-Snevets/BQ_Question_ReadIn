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
# --- Extract the text from PDF files -------------------------------------------------------------
def text_from_pdf(file_name):
   """
   Function to pull and return the text from a PDF file for further processing

   """
   # Import PdfReader from the pypdf library for working with the PDF file
   from PyPDF2 import PdfReader # type: ignore

   # Create a reader object and pass in the user-given file
   reader = PdfReader(file_name)

   # Determine the number of pages the file is
   num_pages = len(reader.pages)

   # Create an empty string -> All extracted text will get appended to the string
   text_of_pdf = ""

   # For Each Page
   for i in range(num_pages):
      # Create a page object -> It contains the extract_text function we need to call
      page = reader.pages[i]

      # Extract the text from the document and append it to the string
      text_of_pdf += page.extract_text()

   # Return the text of the document
   return text_of_pdf



# --- Extract the text from DOC files -------------------------------------------------------------
def text_from_doc(file_name):
   """
   Function to pull and return the text from a DOC file for further processing
   NOTE: Currently adding following line to output:
         "Evaluation Warning: The document was created with Spire.Doc for Python."

   """
   # Import the necessary Spire Libraries for reading DOC files
   from spire.doc import Document #type: ignore

   # Create a Document Object
   doc = Document()

   # Load in the DOC file
   doc.LoadFromFile(file_name)

   # Extract the Text from the Document
   text_of_doc = doc.GetText()

   # Return the Extracted Text
   return text_of_doc
   


# --- Extract the text from DOCX files ------------------------------------------------------------
def text_from_docx(file_name):
   """
   Function to pull and return the text from a DOCX file for further processing

   """
   # Import docx2txt for working with the DOCX file
   print('* Importing')
   import docx2txt #type: ignore

   # Extract the text from the document
   print('* Extracting the text')
   text_of_docx = docx2txt.process(file_name)

   # Return the extracted text
   print('* Returning extracted text')
   return text_of_docx



# --- Get Question File ---------------------------------------------------------------------------
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
      # If the file extension is PDF, call text_from_pdf()
      if file_extension[0] == '.pdf':
         text_of_file = text_from_pdf(user_input)

      # If the file extension is DOC, call text_from_doc()
      elif file_extension[0] == '.doc':
         text_of_file = text_from_doc(user_input)

      # If the file extension is DOCX, call text_from_docx()
      elif file_extension[0] == '.docx':
         text_of_file = text_from_docx(user_input)

   except: # The file type was not PDF, DOC, or DOCX
      # Output an Error Message
      print('------------------------------------------------------------------')
      print('ERROR: File Type Not Supported')
      print('Make sure the file you want to submit is either PDF, DOC, or DOCX')
      print('------------------------------------------------------------------\n')

      # Return back to Main - There's nothing more the program can do
      return


   # Call process_questions and Pass the File Path
   process_questions(text_of_file)




# --- Process Questions ---------------------------------------------------------------------------
def process_questions(text_of_input_file):
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

      # Find the first question  
      find_q = re.search('Question ', text_of_input_file)

      # For each question
      while find_q != None:
         # Find the index of the question
         q_num_index = find_q.end()
  
         # If it is 'n' -> number
         if text_of_input_file[q_num_index] == 'n':
            # Parse through 'number' to get to the question number
            q_num = re.search('number (\d+)', text_of_input_file).group(1)
            print('Question Number:', q_num)
    
            # Keep parsing through to get the point value
            pt_value = re.search('for (\d+)', text_of_input_file).group(1)
  
         # If it is 'f' -> for -> It's a Substitute Question
         elif text_of_input_file[q_num_index] == 'f':
            # Parse through 'for' to get to the point value
            #-> 10 points = question number is 21
            #-> 20 points = question number is 22
            #-> 30 points = question number is 23
            pt_value = re.search('for (\d+)', text_of_input_file).group(1)
            if pt_value == 10:
               q_num = 21
            elif pt_value == 20:
               q_num = 22
            else: #pt_value == 30
               q_num = 23
            print('Number:', q_num)
    
         else:
            print('uuuhhhhh')
  
         # Display the Point Value of the Question
         print('Point Value:', pt_value)
  
         # Determine the Index of the Reference containing the answer
         ref_index = re.search('(\S+) (\d+):(\d+)', text_of_input_file)
         book = ref_index.group(1)
         chapter = ref_index.group(2)
         verse = ref_index.group(3)
         print(f'Reference: {book} {chapter}:{verse}')
  
         # Determine if there are Question intros
         #-> Look for 'question.'
         q_part_index = re.search('([^.]+ question\.|[^.]+ Question\.)', text_of_input_file)
  
         #-> Calculate if the index is before the reference index
         #-> Determine if the index exists
         if q_part_index != None and q_part_index.start() < ref_index.start():
            #--> If yes, there is a question part
            print(q_part_index.group(1))
  
         # Determine if there are Answer Intros
         #-> Look for 'answer.'
         a_part_index = re.search('([^.]+ answer[s.]|[^.]+ Answer[s.])', text_of_input_file)
  
         #-> Calculate if the index exists and is before the reference index
         if a_part_index != None and a_part_index.start() < ref_index.start():
            #--> If yes, there is an answer part
            print(a_part_index.group(1))
  
         # Determine if there are Location Intros
         #-> Look for '. From'
         location_index = re.search('\. (From [^.]+)', text_of_input_file)
  
         #-> Calculate if the index exists and is before the reference index
         if location_index != None and location_index.end() < ref_index.start():
            #--> If yes, there is an intro part
            print(location_index.group(1))
      
         print()
    
         # Eliminate the previously-used text as it has now been processed
         #-> Use the last index we have on hand (probably reference)
         text_of_input_file = text_of_input_file[ref_index.end():]
  
         # Move on to the next question
         find_q = re.search('Question ', text_of_input_file)
    
  



# --- Determine Question Introductory Remarks -----------------------------------------------------

# --- Determine Answer Introductory Remarks -------------------------------------------------------

# --- Determine Location Introductory Remarks -----------------------------------------------------

# ===== Main ======================================================================================
if __name__ == "__main__":
   #-> Call function to get a question file
   get_question_file()

   #-> Inform User that process is complete
   print('Question Reading Process Complete')