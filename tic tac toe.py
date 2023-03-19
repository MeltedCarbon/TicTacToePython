import random

print("""
        A   B    C
       -----------
    1 |   |   |   |
      | - | - | - |
    2 |   |   |   |
      | - | - | - |
    3 |   |   |   |
       -----------
    
    You are O's, Python is X's.
    """)

A1 = " "
A2 = " "
A3 = " "
B1 = " "
B2 = " "
B3 = " "
C1 = " "
C2 = " "
C3 = " "

winState = 0
x = 0
spacesList = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
usedSpacesList = []
            #  A1   B1   C1   A2   B2   C2   A3   B3   C3
spaceValues = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def playRound():
    
    global A1
    global A2
    global A3
    global B1
    global B2
    global B3
    global C1
    global C2
    global C3

    userInput = input("Enter space to mark: ")

    if userInput.upper() in usedSpacesList:
        print("Space already taken")
        playRound()
    elif userInput.upper() in spacesList:
        if userInput.upper() == (f'{A1=}'.split('=')[0]):
            A1 = "O"
            usedSpacesList.append("A1")
            spaceValues[0] = "O"
        elif userInput.upper() == (f'{A2=}'.split('=')[0]):
            A2 = "O"
            usedSpacesList.append("A2")
            spaceValues[3] = "O"
        elif userInput.upper() == (f'{A3=}'.split('=')[0]):
            A3 = "O"
            usedSpacesList.append("A3")
            spaceValues[6] = "O"
        elif userInput.upper() == (f'{B1=}'.split('=')[0]):
            B1 = "O"
            usedSpacesList.append("B1")
            spaceValues[1] = "O"
        elif userInput.upper() == (f'{B2=}'.split('=')[0]):
            B2 = "O"
            usedSpacesList.append("B2")
            spaceValues[4] = "O"
        elif userInput.upper() == (f'{B3=}'.split('=')[0]):
            B3 = "O"
            usedSpacesList.append("B3")
            spaceValues[7] = "O"
        elif userInput.upper() == (f'{C1=}'.split('=')[0]):
            C1 = "O"
            usedSpacesList.append("C1")
            spaceValues[2] = "O"
        elif userInput.upper() == (f'{C2=}'.split('=')[0]):
            C2 = "O"
            usedSpacesList.append("C2")
            spaceValues[5] = "O"
        elif userInput.upper() == (f'{C3=}'.split('=')[0]):
            C3 = "O"
            usedSpacesList.append("C3")
            spaceValues[8] = "O"
    else:
        print("Improper space input")

    checkForWin()

    if winState == 0:
        pythonPick()
        if pythonChoice == (f'{A1=}'.split('=')[0]):
            A1 = "X"
            usedSpacesList.append("A1")
            spaceValues[0] = "O"
        elif pythonChoice == (f'{A2=}'.split('=')[0]):
            A2 = "X"
            usedSpacesList.append("A2")
            spaceValues[3] = "O"
        elif pythonChoice == (f'{A3=}'.split('=')[0]):
            A3 = "X"
            usedSpacesList.append("A3")
            spaceValues[6] = "O"
        elif pythonChoice == (f'{B1=}'.split('=')[0]):
            B1 = "X"
            usedSpacesList.append("B1")
            spaceValues[1] = "O"
        elif pythonChoice == (f'{B2=}'.split('=')[0]):
            B2 = "X"
            usedSpacesList.append("B2")
            spaceValues[4] = "O"
        elif pythonChoice == (f'{B3=}'.split('=')[0]):
            B3 = "X"
            usedSpacesList.append("B3")
            spaceValues[7] = "O"
        elif pythonChoice == (f'{C1=}'.split('=')[0]):
            C1 = "X"
            usedSpacesList.append("C1")
            spaceValues[2] = "O"
        elif pythonChoice == (f'{C2=}'.split('=')[0]):
            C2 = "X"
            usedSpacesList.append("C2")
            spaceValues[5] = "O"
        elif pythonChoice == (f'{C3=}'.split('=')[0]):
            C3 = "X"
            usedSpacesList.append("C3")
            spaceValues[8] = "O"
    elif winState == 1:
        print("You win")
        x = 1
        return
    elif winState == 2:
        print("Python wins")
        x = 1
        return

    checkForWin()
    if winState == 1:
        if x == 1:
            return
        else:
            print("You win")
            return
    elif winState == 2:
        if x == 1:
            return
        else:
            print("Python wins")
            return

    board = str(f"""
        A   B    C
        -----------
    1 | {A1} | {B1} | {C1} |
      | - | - | - |
    2 | {A2} | {B2} | {C2} |
      | - | - | - |
    3 | {A3} | {B3} | {C3} |
        -----------
    """)
    print(board)
    playRound()
    
def pythonPick():
    global pythonChoice
    pythonChoice = random.choice(spacesList)
    if pythonChoice in usedSpacesList:
        pythonPick()
    else:  
        return

def checkForWin():
    global winState
    if A1 == "O" and B1 == "O" and C1 == "O":
        winState = 1
    elif A2 == "O" and B2 == "O" and C2 == "O":
        winState = 1
    elif A3 == "O" and B3 == "O" and C3 == "O":
        winState = 1
    elif A1 == "O" and A2 == "O" and A3 == "O":
        winState = 1
    elif B1 == "O" and B2 == "O" and B3 == "O":
        winState = 1
    elif C1 == "O" and C2 == "O" and C3 == "O":
        winState = 1
    elif A1 == "O" and B2 == "O" and C3 == "O":
        winState = 1
    elif A3 == "O" and B2 == "O" and C1 == "O":
        winState = 1

    elif A1 == "X" and B1 == "X" and C1 == "X":
        winState = 2
    elif A2 == "X" and B2 == "X" and C2 == "X":
        winState = 2
    elif A3 == "X" and B3 == "X" and C3 == "X":
        winState = 2
    elif A1 == "X" and A2 == "X" and A3 == "X":
        winState = 2
    elif B1 == "X" and B2 == "X" and B3 == "X":
        winState = 2
    elif C1 == "X" and C2 == "X" and C3 == "X":
        winState = 2
    elif A1 == "X" and B2 == "X" and C3 == "X":
        winState = 2
    elif A3 == "X" and B2 == "X" and C1 == "X":
        winState = 2
    return winState and x
        
playRound()
