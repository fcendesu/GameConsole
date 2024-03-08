vals=["E" for i in range(9)]
testList=[i for i in range(1,9)]
testValuesRightSide=[-1,3,-3]
testValuesLeftSide=[1,3,-3]
testValuesMidSide=[-1,1,-3,3]
import numpy as np

def board(vals):
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

def randomNumbers():
    order=0
    while True:
        randnumber=np.random.randint(1,9)
        if not randnumber in vals:
            vals[order]=randnumber
            order+=1
        if order==8:
            break
    location=np.random.randint(0,9)
    temp=vals[location]
    vals[location]="E"
    vals[8]=temp
    return board(vals)

def cellchecker(emptyIndex):
    cells=[]
    if emptyIndex in (0,3,6):
        for i in testValuesLeftSide: 
            if emptyIndex+i>-1 and emptyIndex+i<9:
                cells.append(emptyIndex+i)
    elif emptyIndex in (2,5,8):
        for i in testValuesRightSide:
            if emptyIndex+i>-1 and emptyIndex+i<9:
                cells.append(emptyIndex+i)
    else:
        for i in testValuesMidSide:
            if emptyIndex+i>-1 and emptyIndex+i<9:
                cells.append(emptyIndex+i)
    return cells
     
def game():
    randomNumbers()
    
    while True:
        emptyIndex=vals.index("E")
        emptyPossibleBoxes=cellchecker(emptyIndex)
        while True:
            replaceCell=int(input("Enter the cell wanna replace with the Empyt cell "))
            if not replaceCell>0 and not replaceCell<9:
                print("please enter the between 1 and 9")
            if vals.index(replaceCell)==emptyIndex:
                print("please select a number except E cell")
        
            if vals.index(replaceCell) in emptyPossibleBoxes:
                break
            print("please choose a cell that complies with the game rules!")
        replaceIndex=vals.index(replaceCell)
        vals[emptyIndex]=vals[replaceIndex]
        vals[replaceIndex]="E"
        board(vals)
        if True==isTheGameOver():
            break
        
def isTheGameOver():
    count=0
    for i in testList:
        if vals[i-1]==i:
            count+=1
    if count==8:
        print("Congrats! Good Game Well Played!")
        return True

def beforeStarting():
    print("Game Rules, Empty cell (defined as 'E') You can only swap numbers in adjacent cells.\
          \nit must be as the following for winning. have a nice game.\
          \n1 2 3\
          \n3 4 5\
          \n7 8 E")
    print()
    answer=input("Are you ready to play the game ")
    if answer.upper()=='Y':
        game()
    elif answer.upper()=='N':
        print("bye bye")
    else:
        print()
        print("Your answer is wrong please enter again")
        beforeStarting()
        

