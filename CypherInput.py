#CypherInput
"""
Created on Thu Dec 10 15:58:02 2020

@author: felixdubicki-piper
"""

import numpy.random as r
from os.path import isfile

Alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")



# INPUT FUNCTIONS ---------------------------------------------------------------



def ModeInput():
    '''Specify cypher mode
    I=<User Input>
    O=CypherMode
    '''
    
    # PART 1.1, 4.1
    CypherMode = input( "Enter e for encryption, "+
                       "d for decryption or "+
                       "ad for auto-decryption: " ).strip().lower()
    
    # PART 1.2 invalid input
    if (CypherMode != "e") and (CypherMode != "d") and (CypherMode != "ad"):
        print("Invalid input: Please only enter e, d or ad.")
        return ModeInput()
    else:    
        return CypherMode



def RotationInput():
    '''input rotation value or generate random
    I=<User Input>
    O=R
    '''
    
    # PART 1.1, 1.6
    R = input("Enter a rotation value or r for random: ").strip().lower()
    
    # PART 1.2 reinput if empty input
    if R == "":
        print("No Input Provided: Please enter an integer or r")
        return RotationInput()
    
    # PART 1.2 determine if R is an intger (valid input)
    IsNeg = (R[0] == "-") and R.replace("-","",1).isdigit()
    IsPos = R.isdigit()
    
    # PART 1.6 random input
    if R == "r":
        R = r.randint(1,26)
        print(f"Your encryption key is {R}")
        return R
    
    # PART 1.2 reinput if invalid input
    elif (IsPos ^ IsNeg) == False:
        print("Invalid input: Please enter an integer or r")
        return RotationInput()
    
    # convert str to int
    else:
        R = int(R)
        return R



# PART 1.1, 3.1 message entry
def MessageInput():
    '''ask entry mode, and input message
    I=<User Input>
    O=Message, MessageEntryMode
    '''
    
    # PART 3.1
    MessageEntryMode = input("Type m for manual entry, "+
                             "or f for file entry: ").strip().lower()
    
    # PART 3.2 manual entry
    if MessageEntryMode == "m":
        def ManualInput():
            global Message
            
            # PART 1.1 enter message
            Message = input("Enter classified message:\n\n").strip().upper()
        
        ManualInput()
    
    # PART 3.2 read from file
    elif MessageEntryMode == "f":
        def FileInput():
            global Message
            
            # enter filepath
            FilePath = input("Enter message filepath: ").strip()
            
            # PART 3.3 convert to message
            if isfile(FilePath):
                with open(FilePath,"r") as f:
                    Message = "".join([line for line in f]).upper()
            
            # PART 3.4 reinput if file doesn't exist
            else:
                print("Filepath cannot be found, please enter a valid filepath.")
                FileInput()
        
        FileInput()
            
    # if invalid MessageEntryMode input
    else:
        print("Invalid input: Please enter either only m or f")
        MessageInput()
        
    # PART 1.2 reinput if message empty
    if Message.strip() == "":
        print("Message empty! Please enter a new message.")
        return MessageInput()
    else:
        return Message
    


# PART 2.1 turn Text into list of words (WordList)
def GetWordsOnly(Text):
    '''creates list of all words in message (with non-letters removed)
    I=Text
    O=WordList
    '''
    
    # list of all strings separated by spaces
    WordList = Text.split() 
    
    # remove non-letters: 
    for i in range( len(WordList) ):
        WordList[i] = "".join( [Chr for Chr in WordList[i] if Chr in Alphabet] )
    
    # remove empty elements
    WordList = [Str for Str in WordList if Str != ""] 
    
    return WordList



# END