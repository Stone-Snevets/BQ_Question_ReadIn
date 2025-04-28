"""
Function to automatically include notes about some of the questions in the set that is received

Author: Solomon Stevens
Date: *Enter Date Completed*

This program adds notes to the following types of questions:
> A before / after A - Questions that ask for Chapter Analysis that comes before / after other Chapter Analysis
> A ch - Questions that ask for Chapter Analysis from a chapter
> A conc - Questions that ask for separate Chapter Analysis answers that have something in common
> A fv - Questions that have a Chapter Analysis answer but have a question that comes from a verse
> A sec - Questions that ask for Chapter Analysis from a section
> A vs - Questions that ask for Chapter Analysis from a verse
> acc - Questions that begin with 'According to *insert reference*'
> Adj - Questions that ask for what a given adjective describes
> before / after A - Questions that ask for the words of someone before / after Chapter Analysis
> besides - Questions that begin with the word 'Besides'
> conc fv - Questions that require answers from different verses that have something in common
> conc QE - Questions that ask quizzers to say verses with something in common
> convo - Questions asking for a conversation between two people / groups of people
> desc - Questions that begin with the word describe
> did what - Questions that contain the phrase 'what did (person) do' or '(person) did what'
> hd - Questions that begin with 'How does verse #' or 'How do verses #...' or 'How does the #th verse' or 'How do(es) the opening/closing verse(s)'
> if - Questions that ask for questions having to do with the word 'if'
> mentioned - Questions that end with the word 'mentioned'
> noun - Questions that ask for the chapters in which a noun / verb is contained
> of - Questions that ask the quizzer to complete / begin an 'of' phrase
> ref of sec - Questions that ask for the references of a section
> respond - Questions that ask how someone responded to either Chapter Analysis or some other event
> std - Questions that ask the quizzer to say a verse given the reference
> true / happened - Questions that contain with the phrase 'what is true' / 'what happened'
> unique word - Questions that give the quizzer a word mentioned only once in the material being studied
> UWS - Quotation Completion / Essence Completion questions
> VTGT - Non-Quote / Non-Essence questions with answers coming from consecutive verses
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



    # ----- 'A before / after A' - Questions that ask for Chapter Analysis that comes immediately before / after other Chapter Analysis

    # Search through the Answer Introductory Remark to find all Chapter Analysis then...
    # Search through the Actual Question for the words 'after, before, follow, precede, procede'
    list_A_before_after_A = df.loc[(df['A_Intro'].str.contains('A', case = True)) & (df['Question'].str.contains('after|before|follow|precede|procede', regex = True))]

    # Find the index of all applicable questions
    for i in range(len(list_A_before_after_A)):
        index_A_before_after_A = list_A_before_after_A.index[i]

        # Assign 'A before / after A' to the Notes column in that row
        df.loc[index_A_before_after_A, 'Notes'] = 'A before / after A'
    
    
    
    # ----- 'A ch' - Questions that ask for Chapter Analysis from a chapter

    # Search through the Answer Introductory Remark to find all Chapter Analysis then...
    # Search through the Location Indroductory Remark to find 'ch'
    #-> Check if the Actual Question is directly asking for Chapter Analysis
    # If 'ch' is not in the Location Introductory Remark, check the Actual Question for the word 'chapter'
    list_A_ch = df.loc[(df['A_Intro'].str.contains('A', case = True)) & 
                        (((df['Location'].str.contains('ch')) & (df['Question'].str.contains('individual|geographical|parenthetical|exclamation|Testament|question', regex = True))) |
                        df['Question'].str.contains('chapter'))]

    # Find the index of all applicable questions
    for i in range(len(list_A_ch)):
        index_A_ch = list_A_ch.index[i]

        # Assign 'A vs' to the Notes column in that row
        df.loc[index_A_ch, 'Notes'] = 'A ch'
    
    
    
    # ----- 'A conc' - Questions that ask for Separate Chapter Analysis that have something in common
    #-> A #-word
    #-> A concerning
    #-> A in A
    #-> A titles
    #-> A verb
    #-> Ref of A

    # Search through the Answer Introductory Remark to find all Chapter Analysis then...
    # Search through the Actual Question for one of the types of concordance questions we are looking for
    list_A_conc = df.loc[(df['A_Intro'].str.contains('A', case = True)) & 
                       ((df['Question'].str.contains('\d+[- ]word')) |                                                                      # A #-word
                       (df['Question'].str.contains('oncerning')) |                                                                         # A concerning
                       ((df['Question'].str.contains('Which&named?')) & (df['Question'].str.contains('individual|geographical') == False)) |# A titles
                       ((df['Location'].str.contains('C|S', case = True)) & (df['Question'].str.contains('Who', case = True))) |            # A verb
                       (df['Question'].str.contains('references for the verses&named')))]                                                   # Ref of A

    # Find the index of all applicable questions
    for i in range(len(list_A_conc)):
        index_A_conc = list_A_conc.index[i]

        # Assign 'A conc' to the Notes column in that row
        df.loc[index_A_conc, 'Notes'] = 'A conc'
    
    
    
    # ----- 'A fv' - Questions that ask for Chapter Analysis, but the question comes from the verse

    # Search through the Answer Introductory Remark to find all Chapter Analysis
    list_A_fv = df.loc[df['A_Intro'].str.contains('A', case = True)]

    # Find the index of all applicable questions
    for i in range(len(list_A_fv)):
        index_A_fv = list_A_fv.index[i]

        # Assign 'A vs' to the Notes column in that row
        #-> Check if the Notes column is still blank
        if df.loc[index_A_fv, 'Notes'] == '':
            #-> If so, Assign 'A fv' to it
            df.loc[index_A_fv, 'Notes'] = 'A fv'
    
    
    
    # ----- 'A sec' - Questions that ask for Chapter Analysis from a section

    # Search through the Answer Introductory Remark to find all Chapter Analysis then...
    # Search through the Location Indroductory Remark to find 'sec'
    #-> Check if the Actual Question is directly asking for Chapter Analysis
    # If 'sec' is not in the Location Introductory Remark, check the Actual Question for the word 'section'
    list_A_sec = df.loc[(df['A_Intro'].str.contains('A', case = True)) & 
                        (((df['Location'].str.contains('sec')) & (df['Question'].str.contains('individual|geographical|parenthetical|exclamation|Testament|question', regex = True))) |
                        df['Question'].str.contains('section'))]

    # Find the index of all applicable questions
    for i in range(len(list_A_sec)):
        index_A_sec = list_A_sec.index[i]

        # Assign 'A vs' to the Notes column in that row
        # NOTE: This will overwrite some questions marked 'A fv'.  Since 'A fv' is basically for all Chapter Analysis Questions that previously weren't marked, overwriting them with the correct label is acceptable
        df.loc[index_A_sec, 'Notes'] = 'A sec'
    
    
    
    # ----- 'A vs' - Questions that ask for Chapter Analysis from a verse

    # Search through the Answer Introductory Remark to find all Chapter Analysis then...
    # Search through the Actual Question for the word 'verse'
    list_A_vs = df.loc[(df['A_Intro'].str.contains('A', case = True)) & (df['Question'].str.contains('verse'))]

    # Find the index of all applicable questions
    for i in range(len(list_A_vs)):
        index_A_vs = list_A_vs.index[i]

        # Assign 'A vs' to the Notes column in that row
        # NOTE: This will overwrite some questions marked 'A fv'.  Since 'A fv' is basically for all Chapter Analysis Questions that previously weren't marked, overwriting them with the correct label is acceptable
        df.loc[index_A_vs, 'Notes'] = 'A vs'
    
    
    
    # ----- 'acc' - Questions that begin with 'According to *insert reference*'

    # Search the Actual Question for ones that start with our key phrase
    list_acc = df.loc[df['Question'].str.contains('According to \S+ \d+:\d+', regex = True)]

    # Find the index of each instance
    for i in range(len(list_acc)):
        index_acc = list_acc.index[i]

        # Assign 'acc' to the Notes column in that row
        df.loc[index_acc, 'Notes'] = 'acc'


    
    # ----- 'ADJ' - Questions asking for something an adjective describes -----

    # Search through the Actual Question to find Adjective questions
    #-> 'The word (adjective) is used to describe what/who/whom?'
    #-> 'What is/was (adjective)?
    list_adj = df.loc[df['Question'].str.contains('is used to describe|What is \S+?|What was \S+?')]

    # Find the index of each Adjective question
    for i in range(len(list_adj)):
        index_adj = list_adj.index[i]

        # Assign 'Adj' to the Notes column in that row
        df.loc[index_adj, 'Notes'] = 'Adj'



    # ----- 'before / after A' - Questions that ask for non-Chapter Analysis answers that come immediately before / after Chapter Analysis

    # Search through the Actual Question for the word 'before / after' then...
    # Search through the Actual Question for the word 'immediately'
    list_before_after_A = df.loc[(df['Question'].str.contains('before|after')) & (df['Question'].str.contains('immediately'))]

    # Find the index of all applicable questions
    for i in range(len(list_before_after_A)):
        index_before_after_A = list_before_after_A.index[i]

        # Assign 'before / after A' to the Notes column in that row
        df.loc[index_before_after_A, 'Notes'] = 'before / after A'
    
    
    
    # ----- 'besides' - Questions that begin with the word 'Besides' -----

    # Search the Actual Question to find 'besides' questions
    list_besides = df.loc[df['Question'].str.contains('Besides', case = True)]

    # Find the index of each 'besides' question
    for i in range(len(list_besides)):
        index_besides = list_besides.index[i]

        # Assign 'besides' to the Notes column in that row
        df.loc[index_besides, 'Notes']  = 'besides'



    # ----- 'conc fv' - Questions that ask for something similar in multiple verses -----

    # Search the Location Introductory Remark to find all the Separate / Consecutive verse answers then...
    # Searth the Question Introductory Remark to exclude all Quotation / Essence Questions
    list_conc_fv = df.loc[(df['Location'].str.contains('C|S', case = True)) &
                          (df['Q_Intro'].str.contains('Q|E') == False)]
    
    # Find the index of each of these questions
    for i in range(len(list_conc_fv)):
        index_conc_fv = list_conc_fv.index[i]

        # Assign 'conc QE' to the Notes column in that row
        #-> Check if the Notes column is already occupied by 'A conc'
        if df.loc[index_conc_fv, 'Notes'] == '':
            # If not, assign 'conc fv' to it
            df.loc[index_conc_fv, 'Notes'] = 'conc fv'
    
    
    
    # ----- 'conc QE' - Questions that ask the quizzer to say more than one verse with something in common -----

    # Search the Location Introductory Remark to find all the Separate / Consecutive verse answers then...
    # Search the Question Introductory Remark to find all Quotation / Essence Questions
    list_conc_qe = df.loc[(df['Location'].str.contains('C|S', case = True)) &
                          (df['Q_Intro'].str.contains('Q|E'))]
    
    # Find the index of each of these questions
    for i in range(len(list_conc_qe)):
        index_conc_qe = list_conc_qe.index[i]

        # Assign 'conc QE' to the Notes column in that row
        df.loc[index_conc_qe, 'Notes'] = 'conc QE'
    
    
    
    # ----- 'convo' - Questions asking for a conversation between two people / groups of people

    # Search the Actual Question to find conversations
    list_convo = df.loc[df['Question'].str.contains('conversation')]

    # Find the index of each conversation
    for i in range(len(list_convo)):
        index_convo = list_convo.index[i]

        # Assign 'convo' to the Notes column in that row
        df.loc[index_convo, 'Notes'] = 'convo'
    


    # ----- 'desc' - Questions that begin with the word 'Describe'

    # Search through the Actual Question to find all questions that begin with the word 'Describe'
    list_desc = df.loc[df['Question'].str.contains('Describe', case = True)]

    # Find the index of all questions that begin with 'Describe'
    for i in range(len(list_desc)):
        index_desc = list_desc.index[i]

        # Assign 'desc' to the Notes column in that row
        df.loc[index_desc, 'Notes'] = 'desc'
    
    
    
    # ----- 'did what' - Questions that ask for something a person / group of people did

    # Search the Actual Question to find 'what did (person) do' or '(person) did what'
    list_do_what = df.loc[df['Question'].str.contains('what did \S+ do|\S+ did what', regex = True)]

    # Find the index of each question that matches this criteria
    for i in range(len(list_do_what)):
        index_do_what = list_do_what.index[i]

        # Assign 'do what' to the Notes column in that row
        df.loc[index_do_what, 'Notes'] = 'do what'
    
    
    
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

    
    
    
    # ----- 'if' - Questions that have to do with the word 'if'

    # Search through the Actual Question to find all questions having to do with this word
    #-> 'Under what condition'
    #-> 'which conditional if statement'
    list_if = df.loc[df['Question'].str.contains('nder what condition|hich conditional')]

    # Find the index of each 'if'
    for i in range(len(list_if)):
        index_if = list_if.index[i]

        # Assign 'if' to the Notes column in that row
        df.loc[index_if, 'Notes'] = 'if'
    
    
    
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
    


    # ----- 'ref of sec' - Questions that ask for the references of a section

    # Search through the Actual Question to find questions asking for the references for verses contained in a section
    list_ref_of_sec = df.loc[df['Question'].str.contains('contained in the section titled')]

    # Find the index of each of these questions
    for i in range(len(list_ref_of_sec)):
        index_ref_of_sec = list_ref_of_sec.index[i]

        # Assign 'ref of sec' to the Notes column in that row
        df.loc[index_ref_of_sec, 'Notes'] = 'ref of sec'
    
    
    
    # ----- 'respond' - Questions that ask how someone responds to either a Chapter Analysis or an action

    # Search through the Actual Question to find questions asking how someone responds, replies, or answers
    list_respond = df.loc[df['Question'].str.contains('How [\s+\S+] respond|How [\s+\S+] reply|How [\s+\S+] answer')]

    # Find the index of each responding question
    for i in range(len(list_respond)):
        index_respond = list_respond.index[i]

        # Assign 'respond' to the Notes column in that row
        df.loc[index_respond, 'Notes'] = 'respond'
    
    
    
    # ----- 'std' - Quotation / Essence questions that give the quizzer the reference(s) of the verse(s) to say

    # Search through the Actual Question to find 'quote / give in essence verse #' or 'quote / give in essence the # verse'
    list_std = df.loc[df['Question'].str.contains('Quote verse|Quote the \d+|Give in essence verse|Give in essence the \d+', regex = True)]

    # Find the index of each Standard Quote / Essence Question
    for i in range(len(list_std)):
        index_std = list_std.index[i]

        # Assign 'std' to the Notes column in that row
        # NOTE: This is intended to overwrite some conc QE questions since these are not technically concordance quesitons
        df.loc[index_std, 'Notes'] = 'std'
    
    
    
    # ----- 'true / happened' - Questions that contain with the phrase 'what is true' or 'what happened'

    # Search through the Actual Question to find 'what is true' / 'what happened' questions
    list_true_happened = df.loc[(df['Question'].str.contains('what is true|what happened', regex = True))]
    
    # Find the index of each instance of these phrases
    for i in range(len(list_true_happened)):
        index_true_happened = list_true_happened.index[i]

        # Assign 'true / happened' to the Notes column in that row
        df.loc[index_true_happened, 'Notes'] = 'true / happened'
        
        
        
    # ----- 'unique word' - Questions that give the quizzer a word mentioned only once in the material being studied

    # Search through the Actual Question to find questions asking quizzers to give 'this verse' or identify 'this chapter'
    list_unique_word = df.loc[df['Question'].str.contains('this verse.|this chapter.')]

    # Find the index of each unique word question
    for i in range(len(list_unique_word)):
        index_unique_word = list_unique_word.index[i]

        # Assign 'unique word' to the Notes column of each instance
        df.loc[index_unique_word, 'Notes'] = 'unique word'
    
    
    
    # ----- 'UWS' - Quotation Completion / Essence Completion Question -----

    # Search through the Question Introductory Remark to find 'QC' or 'EC'
    list_UWS = df.loc[(df['Q_Intro'] == 'QC') | (df['Q_Intro'] == 'EC')]
    
    # Find the index of that instance of the intro
    for i in range(len(list_UWS)):
        index_UWS = list_UWS.index[i]

        # Assign 'UWS' to the Notes column in that row
        df.loc[index_UWS, 'Notes'] = 'UWS'



    # ----- 'VTGT' - Non-Quotation / Non-Essence questions that come from consecutive verses

    # Search the Location Introductory Remark to find questions coming from consecutive verses, then...
    # Search the Question Introductory Remark to rule out all Quotation / Essence Questions
    list_vtgt = df.loc[(df['Location'].str.contains('C', case = True)) & ((df['Q_Intro'].str.contains('Q|E', regex = True)) == False)]
    
    # Find the index of each question with Verses That Go Together (VTGT)
    for i in range(len(list_vtgt)):
        index_vtgt = list_vtgt.index[i]

        # Assign 'VTGT' to the Notes column in that row
        #-> Check if the 'Notes' column in that row is empty
        #-> Check if we need to overwrite a question labeled 'conc fv'
        if ((df.loc[index_vtgt, 'Notes'] == '') | (df.loc[index_vtgt, 'Notes'] == 'conc fv')):
            # If so, then assign 'VTGT'
            df.loc[index_vtgt, 'Notes'] = 'VTGT'
    
    
    
    # ----- 'words of' - Questions that ask for the words of a person / group of people

    # Search through the Actual Question to find ones asking for what person / group of people said
    #-> Exclude ones that start with 'About' and 'Concerning'
    #--> These are generic and usually ask for what the author of the book being learned says
    list_words_of = df.loc[df['Question'].str.contains('Give all|what did \S+ say|\S+ said what', regex = True) &
                           (df['Question'].str.contains('About|Concerning', case = True, regex = True) == False)]
    
    # Find the index of each instance
    for i in range(len(list_words_of)):
        index_words_of = list_words_of.index[i]

        # Assign 'words of' to the Notes column in that row
        # NOTE: This may overwrite some questions with the 'VTGT' Note. But 'words of' is more of a narrow search. So this is intentional
        df.loc[index_words_of, 'Notes'] = 'words of'



    # Write the Dataframe to the File we Received
    df.to_csv(FILE_RECEIVED)


# TODO DELETE WHEN DONE WITH PROGRAM
if __name__ == '__main__':
    add_in_notes()