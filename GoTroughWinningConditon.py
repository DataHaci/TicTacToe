'If player1 or player2 contains all three numbers of WinningConditions in one of the WinningConditions, then win condition'
'n element in WinningConditions'
def GoTroughWinningConditions(n):
    WCwin = (WinningConditions[n][0] in player1, WinningConditions[n][1] in player1, WinningConditions[n][2] in player1)
    Alle = all(WCwin)
    print(Alle)