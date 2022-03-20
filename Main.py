
'read thoughts.txt'
'3x3 Matrix is like:' \
'123' \
'456' \
'789'

#wcx = WinConditions
WinConList = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7])

player1 = [1, 2, 3, 0, 0, 0, 0, 0, 0]
player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

'If player1 or player2 contains all three numbers of wcx in one of the wcx, then win condition'

def proofWinConList():
    n = 0
    WCwin = (WinConList[n][0] in player1, WinConList[n][1] in player1, WinConList[n][2] in player1)
    Alle = all(WCwin)
    print(Alle)

'Iterate trough all wcx'
'wc + n'



