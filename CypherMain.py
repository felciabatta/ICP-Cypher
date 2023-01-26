# CypherMain
"""
Created on Fri Nov 27 14:48:00 2020

@author: felixdubicki-piper
"""

from CypherInput import *
from CypherCryption import *
from CypherAnalysis import *

Alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


## PART 1.1,3.X,4.1 User Input ## -----------------------------------------------


CypherMode = ModeInput()


if CypherMode != "ad":
    R = RotationInput()


Message = MessageInput()


# PART 4
if CypherMode == "ad":
    
    # check message contains letters
    if any( [Chr in Message for Chr in Alphabet] ):
        
        # run autodecrypt
        ADResult = AutoDecrypt(Message)
        
        # rotation value & success status
        R = ADResult[1]
        Success = ADResult[0]
        
        # PART 4.3b) if no decryption found
        if Success != "y":
            print("\nAuto-Decryption unsucessful :(")
            
    # if message contains no letters
    else:
        print(f'\n" {Message} "\n\nNothing to decrypt!')


## En/Decryption & Analysis ## --------------------------------------------------


# make sure message contains letters
if any( [Chr in Message for Chr in Alphabet] ):
    
    # don't run if auto-decryption failed
    if CypherMode == "e" or CypherMode == "d" or (CypherMode == "ad" and Success == "y"):
        
        # PART 1.3-1.5 run en/decryption
        Message = RotateChars(Message, R, CypherMode)
        
        # PART 2.1 turn Message into list of words for analysis
        WordList = GetWordsOnly(Message)
        
        # PART 2.1a),b),d) collecing metrics 
        TotalWordCount = len(WordList)
        UniqueWordCount = len( set(WordList) ) # set removes duplicates
        MaxLength = max([len(W) for W in set(WordList)])
        MinLength = min([len(W) for W in set(WordList)])
        
        # PART 2.2 print metrics
        print(f"Total Word Count: {TotalWordCount}")
        print(f"Unique Word Count: {UniqueWordCount}")
        print(f"Min Word Length: {MinLength}")
        print(f"Max Word Length: {MaxLength}")
        
        # PART 2.1c),e)/2.2 
        CountPerLetter(Message)
        WordTally = CountPerWord(WordList)
        
        #!EXTRA# bar chart generated
        WordChart(WordTally)
        
        # PART 2.3
        with open("MessageMetrics.txt", 'w') as f:
            f.write(f"Total Word Count: {TotalWordCount}\n")
            f.write(f"Unique Word Count: {UniqueWordCount}\n")
            f.write(f"Min Word Length: {MinLength}\n")
            f.write(f"Max Word Length: {MaxLength}\n")

# if message contains no letters
elif CypherMode == "e":
    print(f'\n" {Message} "\n\nNothing to encrypt!')
elif CypherMode == "d":
    print(f'\n" {Message} "\n\nNothing to decrypt!')



## END ##