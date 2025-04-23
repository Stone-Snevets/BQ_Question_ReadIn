"""
Function to automatically include notes about some of the questions in the set that is received

Author: Solomon Stevens
Date: *Enter Date Completed*

This program adds notes to the following types of questions:
> TODO A before / after A - Questions that ask for Chapter Analysis that comes before / after other Chapter Analysis
> TODO A ch - Questions that ask for Chapter Analysis from a chapter
> TODO A conc - Questions that ask for separate Chapter Analysis answers that have something in common
-> A concerning
-> A in A
-> A same name
-> A titles
-> A verb
> TODO A fv - Questions that have a Chapter Analysis answer but have a question that comes from a verse
> TODO A sec - Questions that ask for Chapter Analysis from a section
> TODO A vs - Questions that ask for Chapter Analysis from a verse
> acc - Questions that begin with 'According to *insert reference*'
> Adj - Questions that ask for what a given adjective describes
-> 'What was ADJ'
> TODO before / after A - Questions that ask for the words of someone before / after Chapter Analysis
-> Check overwriting by 'words of' -> check if Notes = ''
> besides - Questions that begin with the word 'Besides'
> TODO conc fv - Questions that require answers from different verses that have something in common
> TODO conc QE - Questions that ask quizzers to say verses with something in common
> convo - Questions asking for a conversation between two people / groups of people
> TODO did what - Questions that contain the phrase 'what did (person) do' or '(person) did what'
> hd - Questions that begin with 'How does verse #' or 'How do verses #...' or 'How does the #th verse' or 'How do(es) the opening/closing verse(s)'
> mentioned - Questions that end with the word 'mentioned'
> noun - Questions that ask for the chapters in which a noun / verb is contained
> of - Questions that ask the quizzer to complete / begin an 'of' phrase
> TODO - respond - Questions that ask how someone responded to either Chapter Analysis or some other event
> TODO std - Questions that ask the quizzer to say a verse given the reference
> true / happened - Questions that contain with the phrase 'what is true' / 'what happened'
> TODO unique word - Questions that give the quizzer a word mentioned only once in the material being studied
> UWS - Quotation Completion / Essence Completion questions
> TODO VTGT - Non-Quote / Non-Essence questions with answers coming from consecutive verses
> words of - Questions that ask for the words of a person / group of people

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



    # ----- 'acc' - Questions that begin with 'According to *insert reference*'

    # Search the Actual Question for ones that start with our key phrase
    list_acc = df.loc[df['Question'].str.contains('According to (\S+) (\d+):(\d+)', regex = True)]

    # Find the index of each instance
    for i in range(len(list_acc)):
        index_acc = list_acc.index[i]

        # Assign 'acc' to the Notes column in that row
        df.loc[index_acc, 'Notes'] = 'acc'


    
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
    list_besides = df.loc[df['Question'].str.contains('Besides', case = True)]

    # Find the index of each 'besides' question
    for i in range(len(list_besides)):
        index_besides = list_besides.index[i]

        # Assign 'besides' to the Notes column in that row
        df.loc[index_besides, 'Notes']  = 'besides'



    # ----- 'convo' - Questions asking for a conversation between two people / groups of people

    # Search the Actual Question to find conversations
    list_convo = df.loc[df['Question'].str.contains('conversation')]

    # Find the index of each conversation
    for i in range(len(list_convo)):
        index_convo = list_convo.index[i]

        # Assign 'convo' to the Notes column in that row
        df.loc[index_convo, 'Notes'] = 'convo'
    


    # ----- 'hd' - Questions that begin with something like 'How does verse # describe'

    # Search through the Actual Question to find these types of questions
    #-> How does verse #
    #-> How does the #th verse
    #-> How does the opening / closing verse
    #-> How do verses # and #
    #-> How do the opening / closing verses
    list_hd = df.loc[df['Question'].str.contains('How does verse \d+|How does the \d+|How does the opening|How does the closing|How do verses|How do the opening|How do the closing', regex = True)]

    # Find the index of each 'hd' question
    for i in range(len(list_hd)):
        index_hd = list_hd.index[i]

        # Assign 'hd' to the Notes column of each question
        df.loc[index_hd, 'Notes'] = 'hd'

    
    
    
    # ----- 'mentioned' - Questions that end with the word 'mentioned'

    # Search through the Actual Question to check the last word
    list_mentioned = df.loc[df['Question'].str.contains('mentioned?')]

    # Find the index of each Adjective question
    for i in range(len(list_mentioned)):
        index_mentioned = list_mentioned.index[i]

        # Assign 'Adj' to the Notes column in that row
        df.loc[index_mentioned, 'Notes'] = 'mentioned'



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

    # Find the index of each 'of' phrase question
    for i in range(len(list_ofs)):
        index_ofs = list_ofs.index[i]

        # Assign 'of' to the Notes column in that row
        df.loc[index_ofs, 'Notes'] = 'of'
    


    # ----- 'true / happened' - Questions that contain with the phrase 'what is true' or 'what happened'

    # Search through the Actual Question to find 'what is true' / 'what happened' questions
    list_true_happened = df.loc[(df['Question'].str.contains('what is true|what happened', regex = True))]
    
    # Find the index of each instance of these phrases
    for i in range(len(list_true_happened)):
        index_true_happened = list_true_happened.index[i]

        # Assign 'true / happened' to the Notes column in that row
        df.loc[index_true_happened, 'Notes'] = 'true / happened'
        
        
        
    # ----- 'UWS' - Quotation Completion / Essence Completion Question -----

    # Search through the Question Introductory Remark to find 'QC' or 'EC'
    list_UWS = df.loc[(df['Q_Intro'] == 'QC') | (df['Q_Intro'] == 'EC')]
    
    # Find the index of that instance of the intro
    for i in range(len(list_UWS)):
        index_UWS = list_UWS.index[i]

        # Assign 'UWS' to the Notes column in that row
        df.loc[index_UWS, 'Notes'] = 'UWS'



    # ----- 'words of' - Questions that ask for the words of a person / group of people

    # Search through the Actual Question to find ones asking for what person / group of people said
    #-> Exclude ones that start with 'About' and 'Concerning'
    #--> These are generic and usually ask for what the author of the book being learned says
    list_words_of = df.loc[df['Question'].str.contains('words of|what did \S+ say|\S+ said what', regex = True) &
                           (df['Question'].str.contains('About|Concerning', case = True, regex = True) == False)]
    
    # Find the index of each instance
    for i in range(len(list_words_of)):
        index_words_of = list_words_of.index[i]

        # Assign 'words of' to the Notes column in that row
        df.loc[index_words_of, 'Notes'] = 'words of'



    # Write the Dataframe to the File we Received
    print(df.head(30))


# TODO DELETE WHEN DONE WITH PROGRAM
if __name__ == '__main__':
    add_in_notes()