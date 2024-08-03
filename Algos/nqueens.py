def is_safe(board, i, j):
    n = len(board)
    j_left = j
    j_right = j
    while i >= 0:
        if (j_left >= 0 and board[i][j_left] == 1) or board[i][j] == 1 or (j_right < n and board[i][j_right] == 1):
            return False
        i -= 1
        j_left -= 1
        j_right += 1
    return True


def rec(board, i):
    n = len(board)
    if i == n:
        return 1
    else:
        nb_solutions = 0
        for j in range(n):
            if is_safe(board, i, j):
                board[i][j] = 1
                nb_solutions += rec(board, i+1)
                board[i][j] = 0
        return nb_solutions
    
    
def n_queens(n):
    board = [[0]*n for _ in range(n)]
    return rec(board, 0)


print(n_queens(8)) # Output: 92