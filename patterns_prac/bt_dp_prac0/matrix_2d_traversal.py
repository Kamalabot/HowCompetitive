# This is a backtracking algorithm
# Given a 2D grid of integers, traverse the grid in a depth-first manner and return all
# possible paths from the top-left corner to the bottom-right corner.

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def dfs(grid, row, col, path, result):
    # Add the current cell to the path
    path.append(grid[row][col])

    # If we've reached the bottom-right corner, add the path to the result
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        result.append(list(path))
    else:
        # If we can move right, move to the next column
        if col + 1 < len(grid[0]):
            dfs(grid, row, col + 1, path, result)

        # If we can move down, move to the next row
        if row + 1 < len(grid):
            dfs(grid, row + 1, col, path, result)

    # Backtrack: remove the last element added to the path
    path.pop()


def find_paths(grid):
    result = []
    dfs(grid, 0, 0, [], result)
    return result


# Example usage
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

output = find_paths(grid)

print(output)
