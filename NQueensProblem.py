#Given a chess board of size N*N containing queens and dragons, returns how many
#legal ways exist to locate N queens on the board
def queens_dragons(board):
    return queens_dragons_rec(len(board), 0, 0, board)


def queens_dragons_rec(remaining, row, col, board):
    if remaining == 0:
        count = 1

    else:
        count = 0
        n = len(board)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if row+j+k<n and col+i<n and board[row+j+k][col+i] == 'Q':
                        break
                    if k==n-1:
                        if row+j<n and col+i<n and board[row+j][col+i] != 'Q':
                            if legal_dragons(board, row+j, col+i):
                                board[row+j][col+i] = 'Q'
                                count += queens_dragons_rec(remaining-1, row, col+i, board)
                                board[row+j][col+i] = ' '
    
    return count


#Given a chess board, returns True if a dragon can legally be located at cell
#board[row][col] and False otherwise
def legal_dragons(board, row, col):
    if board[row][col] == 'D':
        return False
    
    for i in range(col-1,-1,-1):
        if board[row][i] == 'Q':
            if i == col-1:
                return False
            for j in range(col-1,i,-1):
                if board[row][j] == 'D':
                    break
                if j == i+1:
                    return False

    for i in range(row-1,-1,-1):
        if board[i][col] == 'Q':
            if i == row-1:
                return False
            for j in range(row-1,i,-1):
                if board[j][col] == 'D':
                    break
                if j == i+1:
                    return False

    for i in range(1,col+1):
        if row-i>=0 and col-i>=0:
            if board[row-i][col-i] == 'Q':
                if i == 1:
                    return False
                for j in range(i):
                    if board[row-j][col-j] == 'D':
                        break
                    if j == i-1:
                        return False
        n = len(board)
        if row+i<n and col-i>=0:
            if board[row+i][col-i] == 'Q':
                for j in range(i):
                    if board[row+j][col-j] == 'D':
                        break
                    if j == i-1:
                        return False             

    return True


#Given a chess board (without dragons) and a number of i queens to locate on it,
#returns True if there is a legal way to do it and False otherwise
def legal(partial, i):
    j = -1
    n = len(partial)

    for row in range(n-1,-1,-1): #finds the first empty row
        if 'Q' in partial[row]:
            j = row+1
            break
        if j != -1:
            break

    if j == - 1: #if there are no queens on the board
        j = 0
    if j > n: 
        return False    
    
    for row in range(j):
        if partial[row][i] == 'Q':
            return False
        if i+j-row < len(partial):
            if partial[row][i+j-row] == 'Q':
                return False
        if i-j+row >= 0:
            if partial[row][i-j+row] == 'Q':
                return False
    return True



#Returns how many legal chess boards (without dragons) of size N*N can contain
#N queens legally
def queens(N):
    partial = [[' ' for i in range(N)] for i in range(N)]
    return count_legals(N, partial)


def count_legals(N, partial, queens=0):
    
    if queens == N:
        count = 1

    else:
        count = 0
        for i in range(N):
            if legal(partial, i):
                partial[queens][i] = 'Q'
                count += count_legals(N, partial, queens+1)
                partial[queens][i] = ' ' 
    
    return count





########
# Tester
########

def test():
    contains = lambda L, R : all(R.count(r) <= L.count(r) for r in R)
    L = [1, 2, 4, 8, 16]

    R = subset_sum_search(L, 13)
    if R == None or not sum(R) == 13 or not contains(L,R):
        print("Error in subset_sum_search")

    R = subset_sum_search(L, 32)
    if not R == None:
        print("Error in subset_sum_search")

    L = [i for i in range(1, 10)]
    R = subset_sum_search(L, 7)
    if R == None or not sum(R) == 7 or not contains(L,R):
        print("Error in subset_sum_search")    
    
    if had(0) != [[0]]:
        print("Error in had")

    if had(2) != [[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]]:
        print("Error in had")

    n = 5        
    empty_board = [[' ' for i in range(5)] for j in range(5)]
    if queens_dragons(empty_board) != 10:
        print("Error in queens_dragons")
    
    if queens(5) != 10:
        print("Error in queens")
    board = [[' ', ' ', 'Q', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' '], 
            [' ', 'Q ', 'D', 'Q', ' '], 
            [' ', ' ', ' ', ' ', ' '], 
            ['Q', ' ', 'D', ' ', ' ']]

    if legal_dragons(board, 2, 4) or not legal_dragons(board, 4, 4):
        print("Error in legal_dragons")
    
    board8 = [[' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q'],
             ['Q', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
    if legal(board8, 1) or not legal(board8, 3):
        print("Error in legal")

    def mysum(lst):
    	return acc((lambda x, y: x + y), 0, lst)
    
    lst = [i for i in range(1,25)]
    if mysum(lst) != sum(lst):
        print("Error in acc()")

        
