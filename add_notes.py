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
    print('\n\nCalled add_notes.py Successfully\n\n')
    # Create a Dataframe Using the Output of the Question File
    df = pd.read_csv(FILE_RECEIVED, encoding='latin')
    print(df.head(10))


if __name__ == '__main__':
    add_in_notes()