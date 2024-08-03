1. N-Queens Problem:
The N-Queens problem is a classic example of using backtracking to find all possible solutions for placing N queens on an N×N chessboard such that no two queens threaten each other.

def solve_nqueens(n):
    def is_safe(board, row, col):
        # Check if it's safe to place a queen at (row, col)
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                return False
        return True

    def backtrack(row):
        if row == n:
            results.append([''.join(row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    results = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0)
    return results

# Example usage for solving the 4-Queens problem
solutions = solve_nqueens(4)
for solution in solutions:
    for row in solution:
        print(row)
    print()

2. Sudoku Solver:
The Sudoku solver uses backtracking to find a valid solution for a Sudoku puzzle.

def solve_sudoku(board):
    def is_valid(board, row, col, num):
        # Check if it's valid to place 'num' at (row, col)
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in map(str, range(1, 10)):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = '.'
                    return False
        return True

    backtrack()

# Example usage for solving a Sudoku puzzle (represented as a 9x9 list)
sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solve_sudoku(sudoku_board)
for row in sudoku_board:
    print(row)

3. Subset Sum Problem:
The subset sum problem uses backtracking to find a subset of numbers from a given set that sums to a specified target.

def subset_sum(nums, target):
    def backtrack(start, path_sum, path):
        if path_sum == target:
            results.append(path[:])
            return
        for i in range(start, len(nums)):
            if path_sum + nums[i] <= target:
                path.append(nums[i])
                backtrack(i + 1, path_sum + nums[i], path)
                path.pop()

    results = []
    backtrack(0, 0, [])
    return results

# Example usage for finding subsets that sum to a target
numbers = [1, 2, 3, 4, 5]
target_sum = 7
subsets = subset_sum(numbers, target_sum)
for subset in subsets:
    print(subset)

