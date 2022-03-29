'read thoughts.txt'
'3x3 Matrix is like:' \
'123' \
'456' \
'789'

'List of Winning Coordinates'
'If list would be bigger, I suggest to use dictionaries/hashmaps'
WinningConditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

player1 = [1, 2, 3, 0, 0, 0, 0, 0, 0]
player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

'If player1 or player2 contains all three numbers of WinningConditions in one of the WinningConditions, then win condition'
'n element in WinningConditions'
def GoTroughWinningConditions(n):
    WCwin = (WinningConditions[n][0] in player1, WinningConditions[n][1] in player1, WinningConditions[n][2] in player1)
    Alle = all(WCwin)
    print(Alle)



'''
'Iterate trough all WinningConditions'
def IterateWinningConditions():
    n = 0
    while n < 8:
        proofWinningConditions(n)
        n += 1

IterateWinningConditions()

'''



