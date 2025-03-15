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
   print('* Importing')
   from PyPDF2 import PdfReader # type: ignore

   # Create a reader object and pass in the user-given file
   print('* Reading in document')
   reader = PdfReader(file_name)

   # Determine the number of pages the file is
   num_pages = len(reader.pages)

   # Create an empty string -> All extracted text will get appended to the string
   print('* Extracting text from the document')
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
   #TODO: Convert DOC to DOCX file
   #      -> Pass that DOCX file to text_from_docx()
   #      -> Return received text

   # Return the Extracted Text
   #return text_of_doc
   return 'Temp_return'
   


# --- Extract the text from DOCX files ------------------------------------------------------------
def text_from_docx(file_name):
   """
   Function to pull and return the text from a DOCX file for further processing

   """
   # Import docx2txt for working with the DOCX file
   print('* Importing')
   import docx2txt #type: ignore

   # Extract the text from the document
   print('* Extracting text from the document')
   text_of_docx = docx2txt.process(file_name)

   # Return the extracted text
   return text_of_docx



# --- Determine Question Introductory Remarks -----------------------------------------------------
def get_question_part(q_intro):
   # Create an output variable to append things to
   q_shorthand = ''

   # Search for the following key intros in the question intro
   # Appened the shorthand to the output variable if the intro exists
   #-> Statement and question
   if 'tatament' in q_intro:
      q_shorthand += 'S'
  
   #-> #-part question
   if re.search('(\d+)', q_intro):
      q_shorthand += str(re.search('(\d+)', q_intro).group(1))
  
   #-> Scripture-text question
   if 'ext' in q_intro:
      q_shorthand += 'T'
  
   #-> Application question
   if 'pplication' in q_intro:
      q_shorthand += 'A'
  
   #-> Quotation question
   if 'uotation' in q_intro:
      q_shorthand += 'Q'
  
   #-> Essence question
   if 'ssence' in q_intro:
      q_shorthand += 'E'
  
   #-> Quotation/Essence Completion question
   if 'ompletion' in q_intro:
      q_shorthand += 'C'
    
   # Return the question intro's shorthand
   return q_shorthand


#--- Determine Answer Introductory Remarks --------------------------------------------------------
def get_answer_part(a_intro):
   # Create an empty string to appened the answers to
   a_shorthand = ''
  
   # Check for the following intros
   #-> #-part answer
   if re.search('(\d+)', a_intro):
      a_shorthand += str(re.search('(\d+)', a_intro).group(1))
  
   #-> Complete answer
   if 'omplete' in a_intro:
      a_shorthand += 'C'
  
   #-> Chapter Ananysis answer
   if 'nalysis' in a_intro:
      a_shorthand += 'A'
  
   # Return the shorthand string
   return a_shorthand



#--- Determine Location Introductory Remarks ------------------------------------------------------
def get_location(location):
   # Create the empty string to eventually return
   loc_shorthand = ''
  
     # Create a flag for help determining multiple books, sections, or chapters
   is_section = 0
  
   # Search for the following key words
   #-> Number of verses
   if re.search('From (\d+) [Cc]onsecutive', location):
       loc_shorthand += str(re.search('From (\d+) [Cc]onsecutive', location).group(1))
  
   elif re.search('From (\d+) [Ss]eparate', location):
      loc_shorthand += str(re.search('From (\d+) [Ss]eparate', location).group(1))
  
   #-> Consecutive Verses
   if 'onsecutive verses' in location:
      loc_shorthand += 'C'
  
   #-> Separate Verses
   elif 'eparate verses' in location:	#NOTE: can't be both consecutive and separate
      loc_shorthand += 'S'
      
   #-> Section
   if 'section' in location or 'Section' in location:
      loc_shorthand += 'sec'
      # Set our flag to true
      is_section = 1
  
   #-> Chapter
   elif 'hapter' in location:
      loc_shorthand += 'ch'
  
   #-> Book
   elif 'verses.' not in location:
      loc_shorthand += 'bk'
  
   #-> Multiple?
   # Check if the flag is true or not
   if is_section == 0:
      # If not, simply look for the word 'and'
      if ' and' in location:
         loc_shorthand += 's'
   else:
      # If the flag was raised, check if there is an "and" before the section title
      and_index = re.search(' and', location)
      title_index = re.search('title', location)
      if and_index != None and title_index != None and and_index.start() < title_index.start():
         # If it is before, we can append the s
         loc_shorthand += 's'

      # Also check if the word "sections" is found in the intro
      elif 'ections' in location:
         # If so, append the s
         loc_shorthand += 's'
  
   # Return the shorthand
   return loc_shorthand



# --- Process Questions ---------------------------------------------------------------------------
def process_questions(text_of_input_file):
   """
   Function to -> process all questions in a file received from "get_question_file"
               -> send all findings to a csv file

   """
   # --- Local Variable Initiation ---
   set_num = 0

   # Open a csv file to write to
   #-> Set the 'newline' flag to a space to avoid gap rows between each input
   print('Opening Output File\n')
   with open(FILE_TO_WRITE_TO, 'w', newline='') as output_file:
       
      # Create a Writer Object to write with
      writer = csv.writer(output_file)

      # Write a Header Row
      writer.writerow(HEADER)

      # Find First Question's Point Value
      pt_val_index = re.search('(\d+) points', text_of_input_file)

      # While not end of file
      while pt_val_index != None:  
         q_begins = pt_val_index.end()
         # Use the Point Value to find the Question Number
         #-> Find the Point Value
         #--> Cast it to an integer rather than a string
         pt_value = int(pt_val_index.group(1))
         #-> Back up to find Question Number
         q_num_index = re.search('Question number (\d+)', text_of_input_file)
  
         #-> If number doesn't exist, Assign appropriate Sub Question Number
         if q_num_index == None or q_num_index.end() > pt_val_index.start():
            # If 10 Points -> Question Number = 21
            if pt_value == 10:
               q_num = 21
            # If 20 Points -> Question Number = 22
            elif pt_value == 20:
               q_num = 22
            # If 30 Points -> Question Number = 23
            else:
               q_num = 23
    
         # If number DOES exist, Find it and Assign it
         else:
            q_num = int(q_num_index.group(1))
  
     
         # Determine the Set Number
         #-> if the question number == 1, we started a new set
         if q_num == 1:
            set_num += 1

            # Display Status to User
            print('Processing Set', set_num)

  
         # Find the (first) Reference for the Answer
         ref_index = re.search('\n(|\s+)(\[?)(\S+) (\d+):(\d+)', text_of_input_file)
         ref = (f'{ref_index.group(3)} {ref_index.group(4)}:{ref_index.group(5)}')
  
  
         # See if Question Intros exist in Current Question
         #-> Grab the next Question Intros' Index
         q_part_index = re.search('([^.]+ question.|[^.]+ Question.)', text_of_input_file)
  
         #-> If that index is before the reference index, we have a question part
         if q_part_index != None and q_part_index.end() < ref_index.start():
            q_begins = q_part_index.end()
            # Sent the Question Intros to get_question_part()
            q_part = get_question_part(q_part_index.group(1))

         #-> If not, assign an underscore "_" to q_part
         else:
            q_part = '_'
  
  
         # See if Answer Intros exist in Current Question
         #-> Grab the next Answer Intros' Index
         a_part_index = re.search('([^.]+ answer[s.]|[^.]+ Answer[s.])', text_of_input_file)
  
         #-> If that index is before the reference index, we have an answer part
         if a_part_index != None and a_part_index.end() < ref_index.start():
            q_begins = a_part_index.end()
            # Sent the Answer Intros to get_answer_part()
            a_part = get_answer_part(a_part_index.group(1))

         #-> If not, assign the underscore
         else:
            a_part = '_'
  
  
         # See if Location(s) exist in Current Question
         #-> Grab the next location's index
         location_index = re.search('. (From [^.]+)', text_of_input_file)
  
         #-> If that index is before the reference index, we have a location in the intros
         if location_index != None and location_index.end() < ref_index.start():
            q_begins = location_index.end()
            # Send the Location to get_location()
            location = get_location(location_index.group(1))

         #-> If not, assign the underscore
         else:
            location = '_'
  
  
         # Copy Over Question
         q_index = re.search('\n(.+)', text_of_input_file[q_begins:ref_index.start()])
         
         # If q_index doesn't exist, go to the next reference to expand the horizon
         #-> The question itself may have started with a reference
         while q_index == None:
            # Consume the text up to the reference
            text_of_input_file = text_of_input_file[ref_index.end():]

            # Find the next reference
            ref_index = re.search('\n(|\s+)(\[?)(\S+) (\d+):(\d+)', text_of_input_file)

            # Recheck the question index
            q_index = re.search('\n(.+)', text_of_input_file[q_begins:ref_index.start()])

         # Grab the contents of the question index
         question = q_index.group(1)


  
         # Consume the Used Question Parts
         text_of_input_file = text_of_input_file[ref_index.end():]
         
  
         # Check for Additional References in the Answer
         #-> Find next Question Index
         pt_val_index = re.search('(\d+) points', text_of_input_file)
         if pt_val_index == None:
            print('->', text_of_input_file)


         #-> Find the next Reference Index
         ref_index = re.search('\n(|\s+)(\[?)(\S+) (\d+):(\d+)', text_of_input_file)

         #-> Determine if the Reference Index is Less than the Point Value Index
         #--> Also determine if both actually exist
         while pt_val_index != None and ref_index != None and ref_index.end() < pt_val_index.start():
            # If all checks out, we have another reference to paste
            ref += (f' / {ref_index.group(3)} {ref_index.group(4)}:{ref_index.group(5)}')

            # Consume the Text before the reference
            text_of_input_file = text_of_input_file[ref_index.end():]

            # Check for the next reference index
            ref_index = re.search('\n(|\s+)(\[?)(\S+) (\d+):(\d+)', text_of_input_file)

            # Check for the new index of the next Point Value
            pt_val_index = re.search('(\d+) points\.', text_of_input_file)
               
    
         # Write this Question's Information to the Output File
         #-> set 'newline' to a whitespace to avoid gaps between inputs
         writer.writerow([set_num, q_num, pt_value, q_part, a_part, location, question, ref])



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
         print('Type of File: PDF')
         text_of_file = text_from_pdf(user_input)

      # If the file extension is DOC, call text_from_doc()
      elif file_extension[0] == '.doc':
         print('Type of File: DOC')
         text_of_file = text_from_doc(user_input)

      # If the file extension is DOCX, call text_from_docx()
      elif file_extension[0] == '.docx':
         print('Type of File: DOCX')
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
   print('\nCalling Function to Process Questions\n')
   process_questions(text_of_file)




# ===== Main ======================================================================================
if __name__ == "__main__":
   #-> Call function to get a question file
   get_question_file()

   #-> Inform User that process is complete
   print('Question Reading Process Complete')