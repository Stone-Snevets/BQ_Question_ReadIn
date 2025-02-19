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

# --- Constants ---

# ===== Functions =================================================================================
# --- Get Question File ---
def get_question_file():
   #-> Ask User for File
   user_input = input('Enter the Full Path of the Question File: ')

   #-> Read in File
   print(f'File Name: {user_input}\n')

   #---DUMMY----------------------------#
   with open(user_input, 'r') as file:  #
      print(file.read())                #
   #---END_DUMMY------------------------#

# --- Process Questions ---
#-> Open a csv file to write to
#-> For each question
#--> Determine Question number
#--> Determine Point Value
#--> Check for Question, Answer, and/or Location Introductory Remarks
#---> If none of any, skip that function
#--> Copy over the question
#--> Find the reference(s) of the answer
#-> Close both files once all questions are read in

# --- Determine Question Introductory Remarks ---

# --- Determine Answer Introductory Remarks ---

# --- Determine Location Introductory Remarks ---

# ===== Main ======================================================================================
if __name__ == "__main__":
   #-> Call function to get a question file
   get_question_file()

   #-> Inform User that process is complete
   print('Question Reading Process Complete')