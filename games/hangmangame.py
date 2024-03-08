
import numpy as np
from pathlib import Path


def hangmanGame(selectedWord):

    hangedStr="|-0-<-<"
    wordLength=len(selectedWord)
    currentHangStr=""
    currentGuessStr=""
    guessesSoFor=""

    i=0
    while i < wordLength:
        currentGuessStr+='-'
        i=i+1


    hangIndex=0
    while currentHangStr != hangedStr:
        
        
        print(" Your current guess = ",currentGuessStr)
        print(" Your current hang statue = ", currentHangStr)
        

        guessedChar=input("please make a character guess: ")
        if guessedChar in guessesSoFor:
            print("this guess was made before")
        elif guessedChar not in selectedWord:
            currentHangStr+=hangedStr[hangIndex]
            guessesSoFor+=guessedChar
            hangIndex+=1
            if currentHangStr==hangedStr:
                print(currentHangStr)
                print("you are hanged")
        
        else:
            print("good! you made a rightt guess!")
            i=0
            temp=""
            while i< wordLength:
                if guessedChar==selectedWord[i]:
                    temp=temp+guessedChar
                else:
                    temp=temp+currentGuessStr[i]
                i+=1
            currentGuessStr=temp
            guessesSoFor+=guessedChar
            if currentGuessStr==selectedWord:
                print("Congratulations!")
                break
    
    
    
def ChoosingWord():
    
    folderLocation=Path(__file__).parent.resolve()
    file_path = folderLocation/"words.txt"
    
    with open(file_path, "r") as file:
        lines=file.readlines()
    return lines


def start():
    
    hangmanGame(ChoosingWord()[np.random.randint(0,101)])