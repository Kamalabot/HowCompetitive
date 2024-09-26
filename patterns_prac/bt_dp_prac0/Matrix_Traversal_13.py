# Pattern: Matrix Traversal
# Introduction:
# Involves traversing elements in a matrix using different techniques (DFS, BFS, etc.).

# Sample Problem:
# Perform flood fill on a 2D grid. Change all the cells connected to the starting cell to a new color.
# (starting cell, sr, sc)


def flood_fill(image, sr, sc, new_color):
    original_color = image[sr][sc]
    # why return when original color is same
    # as nc, other cells still might be diff
    if original_color == new_color:
        return image

    def dfs(r, c):
        if (
            0 <= r < len(image)
            and 0 <= c < len(image[0])
            and image[r][c] == original_color
        ):
            image[r][c] = new_color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

    dfs(sr, sc)
    return image


print(flood_fill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, new_color=2))

# Output: [[2,2,2],[2,2,0],[2,0,1]]

# LeetCode Problems:
# 1. Flood Fill (LeetCode #733)
# 2. Number of Islands (LeetCode #200)
# 3. Surrounded Regions (LeetCode #130)
