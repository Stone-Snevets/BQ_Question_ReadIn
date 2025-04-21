"""
Function to automatically include notes about some of the questions in the set that is received

Author: Solomon Stevens
Date: *Enter Date Completed*

"""

# ===== Preliminary ===============================================================================
# --- Libraries ---
import pandas as pd # For creating and working with a data frame

# --- Constants ---
FILE_RECEIVED = 'output.csv'

# ===== Functions =================================================================================
# --- Add in Notes --------------------------------------------------------------------------------
def add_in_notes():
    """
    Function to actually add in notes where the program can

    """
    # Create a Dataframe Using the Output of the Question File
    #-> NOTE: The 'latin' encoding allows the program to read in utf-8 quotation marks without an error
    df = pd.read_csv(FILE_RECEIVED, encoding='latin')

    # Add a Blank 'Notes' Column to the Dataframe
    df['Notes'] = ''



    # Begin Adding Notes

    # ----- 'UWS' - Quotation Completion / Essence Completion Question -----

    # Search through the Question Introductory Remark to find 'QC' or 'EC'
    list_UWS = df.loc[(df['Q_Intro'] == 'QC') | (df['Q_Intro'] == 'EC')]
    num_UWS = len(list_UWS)
    
    # Find the INdex of that Instance of the Intro
    for i in range(num_UWS):
        index_UWS = list_UWS.index[i]

        # Assign 'UWS' to the Notes Column in that Row
        df.loc[index_UWS, 'Notes'] = 'UWS'



    # ----- 'ofs' - Questions asking to complete / begin an 'of' phrase -----

    # Search through the Actual Question to Find the 'of' Phrase Questions
    #-> Complete the phrase
    #-> Begin the (#-word) phrase
    list_ofs = df.loc[(df['Question'].str.contains('complete the phrase')) |
                      (df['Question'].str.contains('begin the') & df['Question'].str.contains('phrase'))]
    num_ofs = len(list_ofs)

    # Find the Index of Each 'of' Phrase Question
    for i in range(num_ofs):
        index_ofs = list_ofs.index[i]

        # Assign 'of' to the Notes Column in that Row
        df.loc[index_ofs, 'Notes'] = 'of'


    # ----- 'ADJ' - Questions asking for something an adjective describes -----

    # ----- 'acc' - Questions that start with 'According to *insert reference*' -----

    # ----- 'besides' - Questions that begin with the word 'Besides' -----


    # Write the Dataframe to the File we Received
    print(df.head(30))


# TODO DELETE WHEN DONE WITH PROGRAM
if __name__ == '__main__':
    add_in_notes()