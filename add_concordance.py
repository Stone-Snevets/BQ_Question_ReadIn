"""
File to automatically add in the part answer of each concordance question found in the given set

Author: Solomon Stevens
Date: *ENTER DATE COMPLETED*

"""

# ===== Preliminary ===============================================================================
# --- Libraries ---
import pandas as pd # For creating and working with a data frame

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

    print(df.head())


# TODO DELETE WHEN DONE WITH PROGRAM
if __name__ == '__main__':
    add_in_conc()