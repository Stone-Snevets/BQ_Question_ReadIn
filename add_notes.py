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

    # --- Quotation Completion Questions ---
    # Search through the Question Introductory Remark to find 'QC'
    list_QC = df.loc[df['Q_Intro'] == 'QC']
    num_QC = len(list_QC)
    
    # Find the index of that instance of the intro
    for i in range(num_QC):
        index_QC = list_QC.index[i]

        # Assign 'UWS' to the Notes column in that row
        df.loc[index_QC, 'Notes'] = 'UWS'

    # --- Essence Completion Questions ---
    list_EC = df.loc[df['Q_Intro'] == 'EC']
    num_EC = len(list_EC)
    
    # Find the index of that instance of the intro
    for i in range(num_EC):
        index_EC = list_EC.index[i]

        # Assign 'UWS' to the Notes column in that row
        df.loc[index_EC, 'Notes']= 'UWS'


    # ----- 'ofs' - Questions asking to complete / begin an 'of' phrase -----

    # ----- 'ADJ' - Questions asking for something an adjective describes -----

    # ----- 'acc' - Questions that start with 'According to *insert reference*' -----

    # ----- 'besides' - Questions that begin with the word 'Besides' -----


    # Write the Dataframe to the File we Received
    print(df.head(30))


# DELETE WHEN DONE WITH PROGRAM
if __name__ == '__main__':
    add_in_notes()