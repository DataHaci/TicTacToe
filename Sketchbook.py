WinningConditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(5):
    Position = input("Which field? ")
    Position = int(Position)
    player1[Position-1] = Position
    print("player1 ", player1)

    Position = input("Which field? ")
    Position = int(Position)
    player2[Position-1] = Position
    print("player2 ", player2)