
'read thoughts.txt'
'3x3 Matrix is like:' \
'123' \
'456' \
'789'

import numpy as np

#wcx = WinningCondition
wc1 = [1, 2, 3]
wc2 = [4, 5, 6]
wc3 = [7, 8, 9]
wc4 = [1, 4, 7]
wc5 = [2, 5, 8]
wc6 = [3, 6, 9]
wc7 = [1, 5, 9]
wc8 = [3, 5, 7]

player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

'If player1 or player2 contains all three numbers of wcx in one of the wcx, then win condition'

WCPlayer1 = (wc1[0] in player1, wc1[1] in player1, wc1[2] in player1)
print(WCPlayer1)


