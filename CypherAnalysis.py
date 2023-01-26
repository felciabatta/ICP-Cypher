# CypherAnalysis
"""
Created on Thu Dec 10 17:56:43 2020

@author: felixdubicki-piper
"""

import numpy as np
import matplotlib.pyplot as plt

Alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")



# ANALYSIS FUNCTIONS ------------------------------------------------------------



# PART 2.1c)
def CountPerWord(WordList):
    '''tallies occurences of each unique word
    I=WordList ( or GetWordsOnly(Message) )
    O=print()
    '''
    
    # list of unique words
    UniqueWords = list( set(WordList) ) 
    WordTally = [ ["",W] for W in UniqueWords ] # create list with tally for 
                                                # each unique word
    # count and sort words
    for i in range( len(WordTally) ):
        WordTally[i][0] = WordList.count( UniqueWords[i] )
    WordTally = sorted(WordTally, reverse=True)
    
    # PART 2.2 prints top ten words
    for n in range( len(WordTally) ):
        if n == 10:
            break
        else:
            print(f"{n+1}. {WordTally[n][1]} : {WordTally[n][0]}")
    print()
    
    return(WordTally)



# PART 2.1e) 
def CountPerLetter(Text):
    '''finds most common letter
    I=Message,Alphabet
    O=print()
    '''
    
    LetterTally = [ ["",Letter] for Letter in Alphabet]
    
    # count letters 
    for i in range( len(Alphabet) ):
        LetterTally[i][0] = Text.count( Alphabet[i] )
    
    # list of letters most to least common
    LetterTally = sorted(LetterTally, reverse=True)
    
    # PART 2.2
    print(f"Most common letter: {LetterTally[0][1]},",
          f"with {LetterTally[0][0]} occurrences\n")
    


#!EXTRA# bar chart
def WordChart(TallyData):
    # generates bar chart using Word Tally
    
    # extract tally
    yData = sorted( [ int(x[0]) for x in TallyData ][:10] )
    # extract words
    xTicks = np.flipud( np.array( TallyData )[:10,1] )
    
    # plot
    xPos = np.arange( len(xTicks) )
    plt.bar(xPos,yData,align="center")
    
    # customise features
    plt.xticks(xPos,xTicks,rotation=30,)
    plt.xlabel("$Word$")
    plt.ylabel("$Tally$")
    plt.title("10 Most Common Words")
    
    plt.savefig('WordChart.pdf') 
    plt.show()
    
     
    
    

# END