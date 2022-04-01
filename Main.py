'read thoughts.txt' \
'3x3 Matrix is like:' \
'123' \
'456' \
'789'

WinningConditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

#only one field object


player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def WriteInPlayer():
    for x in range(5):
        Position = input("Which field Player 1? ")
        Position = int(Position)
        player1[Position - 1] = Position
        print("player1 ", player1)

        IterateWinningConditions()

        Position = input("Which field Player 2? ")
        Position = int(Position)
        player2[Position - 1] = Position
        print("player2 ", player2)

        IterateWinningConditions()

def GoTroughWinningConditions(n):
    WCwin = (WinningConditions[n][0] in player1, WinningConditions[n][1] in player1, WinningConditions[n][2] in player1)
    Alle = all(WCwin)
    if Alle:
        print("You have won!")
        quit()

def IterateWinningConditions():
    n = 0
    while n < 8:
        GoTroughWinningConditions(n)
        n += 1

WriteInPlayer()





