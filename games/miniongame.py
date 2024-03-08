import numpy as np
from pathlib import Path

def minion_game(playerOneName,playerTwoName,string):
    vowels = "AEIOU"
    PlayerOne, PlayerTwo = 0, 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            PlayerTwo += length - i
        else:
            PlayerOne += length - i

    if PlayerOne > PlayerTwo:
        print(f"{playerOneName} {PlayerOne}")
    elif PlayerTwo > PlayerOne:
        print(f"{playerTwoName} {PlayerTwo}")
    else:
        print("Draw")
        
def UploadingWords():
    
    folderLocation=Path(__file__).parent.resolve()
    file_path = folderLocation/"words.txt"
    
    with open(file_path, "r") as file:
        lines=file.readlines()
    return lines
    
def start():
    PlayerOne=input("Enter the name of first player")
    PlayerTwo=input("Enter the name of second player")
    minion_game(PlayerOne,PlayerTwo,UploadingWords()[np.random.randint(0,101)])
    
