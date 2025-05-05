"""
File to automatically add in the part answer of each concordance question found in the given set

Author: Solomon Stevens
Date: *ENTER DATE COMPLETED*

"""

# ===== Preliminary ===============================================================================
# --- Libraries ---
import pandas as pd # For creating and working with a data frame
import re # For finding the numbers associated with each concordance question

# --- Constants ---
FILE_RECEIVED = 'output.csv'

# ===== Functions =================================================================================
# --- Add in Concordance --------------------------------------------------------------------------
def add_in_conc():
    """
    Function to find how many answers are in each Concordance question

    """
    # Create a Dataframe Using the Output of the Question File
    #-> The 'latin' encoding allows the program to read in utf-8 quotation marks without an error
    df = pd.read_csv(FILE_RECEIVED, encoding='latin')

    # Add a Blank 'Conc' Column to the Dataframe
    df['Conc'] = ''



    # Begin Adding Concordance


    # Find all Concordance Questions
    #-> Check if the 'Notes' column was generated
    if 'Notes' in df.columns:
        # If so, find all rows where the 'Notes' column reads 'conc'
        list_conc = df.loc[(df['Notes'] == 'A conc') | (df['Notes'] == 'conc QE') | (df['Notes'] == 'conc fv')]

    #-> If not find all concordance questions manually
    #--> A concordance: Concordance questions with Chapter Analysis answers
    #--> conc fv: Concordance questions that come from the verse(s)
    #--> conc QE: Concordance questions that ask the quizzer to Quote / give in Essence the verses
    else:
        list_conc = df.loc[(df['A_Intro'].str.contains('A', case = True)) & 
                    ((df['Question'].str.contains('\d+[- ]word')) |                                                                                 # A #-word
                     (df['Question'].str.contains('oncerning')) |                                                                                   # A concerning
                     (df['Question'].str.contains(' in ')) |                                                                                        # A in A
                     ((df['Question'].str.contains('Which \S+ are named\?')) & (df['Question'].str.contains('individual|geographical') == False)) | # A titles
                     ((df['Location'].str.contains('C|S', case = True)) & (df['Question'].str.contains('Who', case = True))) |                      # A verb
                     (df['Question'].str.contains('references for the verses&named'))) |                                                             # Ref of A
                     ((df['Location'].str.contains('S|chs|bks|secs', case = True)) & (df['Q_Intro'].str.contains('Q|E') == False)) |                # conc fv
                     ((df['Location'].str.contains('C|S|chs|bks|secs', case = True)) & (df['Q_Intro'].str.contains('Q|E')))]                       # conc QE

    
    # For each Concordance Question
    for i in range(len(list_conc)):
        # Grab the index of each Concordance Question
        index_conc = list_conc.index[i]

        # Check the Answer Intro for a Number
        if re.search('\d+', df.loc[index_conc, 'A_Intro']) != None:
            # If it's there, assign that number to the 'Conc' column
            df.loc[index_conc, 'Conc'] = re.search('(\d+)', df.loc[index_conc,'A_Intro']).group(1)

        # If it's not there, Check the Question Intro for a Number
        if re.search('\d+', df.loc[index_conc, 'Q_Intro']) != None:
            # If it's there, assign that number the the 'Conc' column
            df.loc[index_conc, 'Conc'] = re.search('(\d+)', df.loc[index_conc, 'Q_Intro']).group(1)

        # If it's not there, Check the Location Intro for a Number
        if re.search('\d+', df.loc[index_conc, 'Location']) != None:
            # If it's there, assign that number the the 'Conc' column
            df.loc[index_conc, 'Conc'] = re.search('(\d+)', df.loc[index_conc, 'Location']).group(1)

        # If not, assign a '1' to the 'Conc' column
        else:
            df.loc[index_conc, 'Conc'] = '1'
    
    # Write the Dataframe to the File we Received
    #-> Set index = False to avoid additional index columns
    df.to_csv(FILE_RECEIVED, index = False, encoding='latin')


# TODO DELETE WHEN DONE WITH PROGRAM
if __name__ == '__main__':
    add_in_conc()