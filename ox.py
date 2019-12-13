board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def isRowFull(row):
    return row[0] > 0 and row[0] == row[1] and row[1] == row[2]

def isColumnFull(col):
    return board[col][0] > 0 and board[col][0] == board[col][1] and board[col][1] == board[col][2]

for row in board:
    print(row)