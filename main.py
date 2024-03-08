from games import miniongame
from games import hangmangame
from games import puzzle
from games import TicTacToe


print("Choose which game you want to play for puzzle press 1, miniongame 2, hangmangame 3, and tictacdoe 4")
print("for quiting the GameConsole press 5")
flag=False
while(True):
    selectedGame=int(input("Your game is: "))
    
    if selectedGame==1:
        puzzle.beforeStarting()
    
    elif selectedGame==2:
        miniongame.start()
    
    elif selectedGame==3:
        hangmangame.start()
    
    elif selectedGame==4:
        TicTacToe.start()
    elif selectedGame==5:
        print("Thanks for playing!")
        break
    else:
        print("You Pressed wrong command")
