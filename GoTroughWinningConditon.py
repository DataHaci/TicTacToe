'If player1 or player2 contains all three numbers of WinningConditions in one of the WinningConditions, then win condition'
'n element in WinningConditions'


WinningConditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

player1 = [1, 2, 3, 4, 0, 0, 7, 0, 0]
player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

'''
def GoTroughWinningConditions(n):
    WCwin = (WinningConditions[n][0] in player1, WinningConditions[n][1] in player1, WinningConditions[n][2] in player1)
    Alle = all(WCwin)
    print(Alle)

WCwin = (WinningConditions[n][0] in player1, WinningConditions[n][1] in player1, WinningConditions[n][2] in player1)
Alle = all(WCwin)

if Alle:
    print("Player 1 has won!")
    quit()

'''



for x in WinningConditions:
    WCwin = (x[0] in player1, x[1] in player1, x[2] in player1)
    Alle = all(WCwin)
    print(Alle)