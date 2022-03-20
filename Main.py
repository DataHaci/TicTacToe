'read thoughts.txt'
'3x3 Matrix is like:' \
'123' \
'456' \
'789'

'List of Winning Coordinates'
'If list would be bigger, I suggest to use dictionaries/hashmaps'
WinConList = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

player1 = [1, 2, 3, 0, 0, 0, 0, 0, 0]
player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

'If player1 or player2 contains all three numbers of WinConList in one of the WinConList, then win condition'
'n element in WinConList'
def proofWinConList(n):
    WCwin = (WinConList[n][0] in player1, WinConList[n][1] in player1, WinConList[n][2] in player1)
    Alle = all(WCwin)
    print(Alle)

'Iterate trough all WinConList'
def IterateWCL():
    n = 0
    while n < 8:
        proofWinConList(n)
        n += 1

IterateWCL()





