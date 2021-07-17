import json
from difflib import get_close_matches as GCM
from difflib import SequenceMatcher as SM
import random

data = json.load(open("data.json")) 
loop = True
answerSensitivity = .85 #how close the word needs to match the answer

def GetDefinition(word): #Pulls the dictionary definition from the data.json file
    originalWord = word
    word = word.lower()
    
    if(word in data): #If the lowercase word is a key in data
        return(data[word])
    elif(originalWord in data): #If the original word is a key in data
        return(data[originalWord])
    else:
        match = GCM(originalWord, data, n=3, cutoff=0.7) #finds the top 3 matches in the data keys and puts them in a list
        print(f"Closest matches {match}")
        while(len(match) > 0): #While there are matches
            i = input(f"Did you mean {match[0]}? Y or N ").lower()
            if(i == 'y'): #If this is the word return the match
                return(data[match[0]])
            elif(i == 'n'): #If it's not the word remove it from the list
                match.pop(0)
            else:
                print("Please Type (Y) for yes or (N) for no.")
        else:
            return f"The word {word} was not found. Please double check your spelling."

def Proceed(): #Checks if the user would like to find another word.
    proceed = None
    while(proceed != 'y' or proceed != 'n'):
        proceed = input("Would you like to try again? Y or N ").lower()
        if(proceed == 'y'):
            return True  
        elif(proceed == 'n'):
            return False
        else:
            print("Please Type (Y) for yes or (N) for no.")

def ChooseRandomWord():
    return random.choice(list(data.keys()))
    

#Find Definition Program Loop
def FindDefinition():
    provided = input("What would you like the definition of? ")
    print(GetDefinition(provided))
    
def Game():
    invalid = True
    while(invalid):
        counter = 0
        chosenword = ChooseRandomWord()
        for i in data[chosenword]:
            if "ISO" in i:
                counter += 1
        if counter > 0:
            invalid = True
        else:
            invalid = False
            

    print(data[chosenword])
    chosenword = chosenword.lower()
    answer = input("Can you tell me what word i'm defining? ").lower()
    match = SM(None,answer,chosenword).ratio()
    if(match > answerSensitivity):
        print(f'Correct! The answer was {chosenword}')
    else:
        print(f'Incorrect! The answer was {chosenword}')
    
def ModeSelect():
    answer = None
    while answer != "1" or answer != "2":
            
        answer = input("Type the numer of the mode you'd like to use.\n 1.Get Definition \n 2.Game \n")
        if answer == "1":
            return FindDefinition()
        if answer == "2":
            
            return Game()
        else:
            print("invalid selection, try again!")


while loop:
    mode = ModeSelect()
    mode
    loop = Proceed()
    