# Its a Backtracking algorithm
# Get all the possible path from top left
# corner to the bottom right, and store the
# path. (Not just count like the grid_traveller)

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def dfs(grid, row, col, path, result):
    # include the current cell
    path.append(grid[row][col])

    # reached bottom end, add path to result
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        result.append(list(path))

    else:
        if col + 1 < len(grid[0]):
            dfs(grid, row, col + 1, path, result)

        if row + 1 < len(grid):
            dfs(grid, row + 1, col, path, result)

    # exclude the current cell
    path.pop()
