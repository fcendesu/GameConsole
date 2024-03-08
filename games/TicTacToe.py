
winnerSets=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
letters=""
vals=[' ' for i in range(0,9)]

def tictactoe(vals):
    print("\n")
    print("\t     |     |")
    print("\t  %s  |  %s  |  %s"%(vals[0],vals[1],vals[2]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  %s  |  %s  |  %s"%(vals[3],vals[4],vals[5]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  %s  |  %s  |  %s"%(vals[6],vals[7],vals[8]))
    print("\t     |     |")
    
def playerEnterX(letters):
    
    while True:
        choicex=int(input("player X which box= "))
        if vals[choicex-1]!= "X" and vals[choicex-1]!="O":
            break
        print()
        print("please fill the empyt columns")
        tictactoe(vals)
        
    vals[choicex-1]="X"
    for winset in winnerSets:
        letters=""
        for propersubset in winset:
            if vals[propersubset-1]=="X":
                letters=letters+"X"
        if letters=="XXX":
            break
    return letters
    
def playerEnterO(letters):
    while True:
        choiceo=int(input("player O which box= "))
        if vals[choiceo-1]!= "X" and vals[choiceo-1]!="O":
            break
        print()
        print("please fill the empty columns")
        tictactoe(vals)
        
    vals[choiceo-1]="O"
    for winset in winnerSets:
        letters=""
        for propersubset in winset:
            if vals[propersubset-1]=="O":
                letters=letters+"O"
        if letters=="OOO":
            break
    return letters
    
def start():
     tictactoe(vals)
     for i in range(5):   
         
         if playerEnterX(letters)=="XXX":
             tictactoe(vals)
             print("'Player X' won")
             break
         tictactoe(vals)
         if i==4:
             break
         if playerEnterO(letters)=="OOO": 
             tictactoe(vals)
             print("'Player O' won")
             break
         tictactoe(vals)
 
    
    
    
    
    
    
    
    

