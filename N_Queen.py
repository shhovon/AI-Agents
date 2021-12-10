queens = int(input("Enter the number of queens: "))
board = [[0]*queens for _ in range(queens)]

def in_attack(i, j):
    for k in range(0,queens):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    for k in range(0,queens):
        for m in range(0,queens):
            if (k+m == i+j) or (k-m == i-j):
                if board[k][m] == 1:
                    return True
    return False

def NQueen(n):
    if n == 0:
        return True
    for i in range(0,queens):
        for j in range(0,queens):
            if (not(in_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                if NQueen(n-1) == True:
                    return True
                board[i][j] = 0
    return False

NQueen(queens)
for i in board:
    print(i)
