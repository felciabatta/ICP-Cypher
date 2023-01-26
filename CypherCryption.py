# CypherCryption
"""
Created on Thu Dec 10 16:48:07 2020

@author: felixdubicki-piper
"""

from CypherInput import GetWordsOnly

Alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")



# EN/DECRYPTION FUNCTIONS -------------------------------------------------------



def AutoDecrypt(Text):
    '''finds rotation value for which decryption is sucessful
    I=Message,Alphabet
    O=R,Success
    '''
    
    # variable indicates success status
    Success = ""
    
    # PART 4.2 read list of common words
    with open("words.txt", 'r') as f:
        CommonWords = [ line.upper().strip() for line in f ]
    
    # extract first line as list (ChoppedUp)
    ChoppedUp = []
    for Chr in Text:
        if Chr == "\n":
            break
        ChoppedUp.append(Chr)
        
    # PART 4.3 rotation interation
    for R in range(1, len(Alphabet)):
        for i in range( len(ChoppedUp) ):
            
            if ChoppedUp[i] in Alphabet:
                
                # PART 4.3a) rotate by current R+1
                ChoppedUp[i] = Alphabet[ (Alphabet.index(ChoppedUp[i])+1)%26 ]
                
        RotatedMessage = "".join(ChoppedUp)
        
        # PART 4.3b)i,ii compare to words.txt
        if any( [W in CommonWords for W in GetWordsOnly(RotatedMessage) ] ):
            
            # PART 4.3b)iii ask if successful
            Success = input(f'" {RotatedMessage} "\n\nIs this decryption successful?\n'
                            +'Enter y if yes, hit enter if no: ').strip().lower()
            
            if Success == "y":
                break
    return Success,R



# PART 1.3-1.5 & 4.3b)iii en/decryption
def RotateChars(Text, R, CypherMode): 
    '''Rotation algorithms for each CypherMode
    I=Text, R, CyperMode
    O=Message
    '''
    
    # convert message to list of elements
    ChoppedUp = list(Text) 
    
    # rotation time!
    for i in range( len(ChoppedUp) ):
        if ChoppedUp[i] in Alphabet:
            
            # PART 1.3 & 4.3b)iii encrypt (and autodecrypt) mode
            if CypherMode == "e" or CypherMode == "ad":
                # rotates by R
                ChoppedUp[i] = Alphabet[ (Alphabet.index(ChoppedUp[i])+R)%26 ] 
            
            # PART 1.4 decrypt mode
            elif CypherMode == "d":
                # rotates by -R
                ChoppedUp[i] = Alphabet[ (Alphabet.index(ChoppedUp[i])-R)%26 ] 
    
    # PART 1.5 print encrypted message
    if CypherMode == "e":
        print("\nEncryption is complete:"+
              '\n\n" '+"".join(ChoppedUp)+' "\n')
        return Text
    
    # PART 1.5 & 4.3b)iii print decrypted message
    if CypherMode == "d" or CypherMode == "ad":
        print("\nDecryption is complete:"+
              '\n\n" '+"".join(ChoppedUp)+' "\n')
        Message = "".join(ChoppedUp) # assigns decrypted message for analysis
        return Message
    
    print("Keep it a secret!\n")



# END