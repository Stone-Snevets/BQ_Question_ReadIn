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
    # Search through the Question Introductory Remark to find 'QC'
    list_UWS = df.loc[(df['Q_Intro'] == 'QC') | (df['Q_Intro'] == 'EC')]
    num_UWS = len(list_UWS)
    
    # Find the index of that instance of the intro
    for i in range(num_UWS):
        index_UWS = list_UWS.index[i]

        # Assign 'UWS' to the Notes column in that row
        df.loc[index_UWS, 'Notes'] = 'UWS'


    # ----- 'ofs' - Questions asking to complete / begin an 'of' phrase -----

    # --- Complete the Phrase ---

    # --- Begin the Phrase ---


    # ----- 'ADJ' - Questions asking for something an adjective describes -----

    # ----- 'acc' - Questions that start with 'According to *insert reference*' -----

    # ----- 'besides' - Questions that begin with the word 'Besides' -----


    # Write the Dataframe to the File we Received
    print(df.head(30))


# DELETE WHEN DONE WITH PROGRAM
if __name__ == '__main__':
    add_in_notes()