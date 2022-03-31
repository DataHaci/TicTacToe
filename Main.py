'read thoughts.txt' \
'3x3 Matrix is like:' \
'123' \
'456' \
'789'

WinningConditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

player1 = [1, 2, 3, 0, 0, 0, 0, 0, 0]
player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(9):

    player1[Position-1]=Position
    print(player1)

def WriteInPlayer():




def GoTroughWinningConditions(n):
    WCwin = (WinningConditions[n][0] in player1, WinningConditions[n][1] in player1, WinningConditions[n][2] in player1)
    Alle = all(WCwin)
    print(Alle)

def IterateWinningConditions():
    n = 0
    while n < 8:
        GoTroughWinningConditions(n)
        n += 1

IterateWinningConditions()





