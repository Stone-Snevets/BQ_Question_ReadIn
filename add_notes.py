"""
Function to automatically include notes about some of the questions in the set that is received

Author: Solomon Stevens
Date: *Enter Date Completed*

This program adds notes to the following types of questions:
> TODO acc - Questions that begin with 'According to *insert reference*'
> Adj - Questions that ask for what a given adjective describes
> besides - Questions that begin with the word 'besides'
> TODO convo - Questions asking for a conversation between two people / groups of people
> noun - Questions that ask for the chapters in which a noun / verb is contained
> of - Questions that ask the quizzer to complete / begin an 'of' phrase
> TODO true happened - Questions that begin / end with the phrase 'what is true' / 'what happened'
> UWS - Quotation Completion / Essence Completion questions
> TODO words of - Questions that ask for all the words of a person / group of people

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
    #-> The 'latin' encoding allows the program to read in utf-8 quotation marks without an error
    df = pd.read_csv(FILE_RECEIVED, encoding='latin')

    # Add a Blank 'Notes' Column to the Dataframe
    df['Notes'] = ''



    # Begin Adding Notes


    
    # ----- 'ADJ' - Questions asking for something an adjective describes -----

    # Search through the Actual Question to find Adjective questions
    #-> 'The word (adjective) is used to describe what/who/whom?'
    list_adj = df.loc[df['Question'].str.contains('is used to describe')]

    # Find the index of each Adjective question
    for i in range(len(list_adj)):
        index_adj = list_adj.index[i]

        # Assign 'Adj' to the Notes column in that row
        df.loc[index_adj, 'Notes'] = 'Adj'



    # ----- 'besides' - Questions that begin with the word 'Besides' -----

    # Search the Actual Question to find 'besides' questions
    list_besides = df.loc[df['Question'].str.contains('Besides')]

    # Find the index of each 'besides' question
    for i in range(len(list_besides)):
        index_besides = list_besides.index[i]

        # Assign 'besides' to the Notes column in that row
        df.loc[index_besides, 'Notes']  = 'besides'



    # ----- 'noun' - Questions that ask for the chapters in which a noun / verb is mentioned -----

    # Search the Actual Question to find 'noun' questions
    list_noun = df.loc[df['Question'].str.contains('in which chapters?')]

    # Find the index of each 'noun' question
    for i in range(len(list_noun)):
        index_noun = list_noun.index[i]

        # Assign 'noun' to the Notes column in that row
        df.loc[index_noun, 'Notes'] = 'noun'


    
    # ----- 'ofs' - Questions asking to complete / begin an 'of' phrase -----

    # Search through the Actual Question to find the 'of' phrase questions
    #-> 'complete the phrase'
    #-> 'begin the (#-word) phrase'
    list_ofs = df.loc[(df['Question'].str.contains('complete the phrase')) |
                      (df['Question'].str.contains('begin the') & df['Question'].str.contains('phrase'))]

    # Find the Index of Each 'of' Phrase Question
    for i in range(len(list_ofs)):
        index_ofs = list_ofs.index[i]

        # Assign 'of' to the Notes column in that row
        df.loc[index_ofs, 'Notes'] = 'of'
        
        
        
    # ----- 'UWS' - Quotation Completion / Essence Completion Question -----

    # Search through the Question Introductory Remark to find 'QC' or 'EC'
    list_UWS = df.loc[(df['Q_Intro'] == 'QC') | (df['Q_Intro'] == 'EC')]
    
    # Find the index of that instance of the intro
    for i in range(len(list_UWS)):
        index_UWS = list_UWS.index[i]

        # Assign 'UWS' to the Notes column in that row
        df.loc[index_UWS, 'Notes'] = 'UWS'




    # Write the Dataframe to the File we Received
    print(df.head(30))


# TODO DELETE WHEN DONE WITH PROGRAM
if __name__ == '__main__':
    add_in_notes()