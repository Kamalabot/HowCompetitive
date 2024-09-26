# using the stack to store tuple of path list, and curr position (r, c)
def dfs_iterative(grid):
    result = []
    stack = [([grid[0][0]], 0, 0)]  # Stack holds tuples (current path, row, col)

    while stack:
        path, row, col = stack.pop()
        # reached the end of the grid
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            result.append(list(path))
        else:
            # check if there is cell on right
            if col + 1 < len(grid[0]):
                # append it to stack and path
                stack.append((path + [grid[row][col + 1]], row, col + 1))
            # check if there is cell row below
            if row + 1 < len(grid):
                # append it to stack and path
                stack.append((path + [grid[row + 1][col]], row + 1, col))

    return result


# This approach uses a stack to keep
# track of the current path and grid position,
# simulating the recursive DFS
# traversal in an iterative manner.
