'read thoughts.txt' \
'3x3 Matrix is like:' \
'123' \
'456' \
'789'

#Test if field is already used
#clean code

WinConditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

Field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def FieldVisualization():
    print(Field[0:3])
    print(Field[3:6])
    print(Field[6:9])

def Playersmoves():
    for x in range(5):
        Position = int(input("Which field Player 1? "))
        player1[Position - 1] = Position
        Field[Position - 1] = "X"

        FieldVisualization()
        CheckIfP1won()

        Position = int(input("Which field Player 2? "))
        player2[Position - 1] = Position
        Field[Position - 1] = "O"

        FieldVisualization()
        CheckIfP2won()

def CheckIfP1won():
    for x in WinConditions:
        WCwin = (x[0] in player1, x[1] in player1, x[2] in player1)
        Alle = all(WCwin)
        if Alle:
            print("""
            #################################
            CONGRATULATION - PLAYER1 HAS WON!
            #################################""")
            quit()

def CheckIfP2won():
    for x in WinConditions:
        WCwin = (x[0] in player2, x[1] in player2, x[2] in player2)
        Alle = all(WCwin)
        if Alle:
            print("""
            #################################
            CONGRATULATION - PLAYER2 HAS WON!
            #################################""")
            quit()

Playersmoves()

