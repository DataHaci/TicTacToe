'read thoughts.txt' \
'3x3 Matrix is like:' \
'123' \
'456' \
'789'

WinningConditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

#only one field object
Field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def WriteInPlayer():
    for x in range(5):
        Position = input("Which field Player 1? ")
        Position = int(Position)
        player1[Position - 1] = Position
        Field[Position - 1] = "X"
        print(Field[0:3])
        print(Field[3:6])
        print(Field[6:9])

        IterateWinningConditionsP1()

        Position = input("Which field Player 2? ")
        Position = int(Position)
        player2[Position - 1] = Position
        Field[Position - 1] = "O"
        print(Field[0:3])
        print(Field[3:6])
        print(Field[6:9])

        IterateWinningConditionsP2()

def GoTroughWinningConditionsP1(n):
    WCwin = (WinningConditions[n][0] in player1, WinningConditions[n][1] in player1, WinningConditions[n][2] in player1)
    Alle = all(WCwin)
    if Alle:
        print("Player 1 has won!")
        quit()

def IterateWinningConditionsP1():
    n = 0
    while n < 8:
        GoTroughWinningConditionsP1(n)
        n += 1

def GoTroughWinningConditionsP2(n):
    WCwin = (WinningConditions[n][0] in player2, WinningConditions[n][1] in player2, WinningConditions[n][2] in player2)
    Alle = all(WCwin)
    if Alle:
        print("Player 2 has won!")
        quit()

def IterateWinningConditionsP2():
    n = 0
    while n < 8:
        GoTroughWinningConditionsP2(n)
        n += 1


WriteInPlayer()





