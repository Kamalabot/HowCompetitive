# Perform flood fill on a 2D grid.
# Change all the cells connected to the starting
# cell to a new color. (starting cell, sr, sc)


def flood_fill(image, sr, sc, nc):
    org_color = image[sr][sc]
    # seems like the base case
    if org_color == nc:
        return image

    def dfs(r, c):
        if 0 <= r < len(image) and 0 <= c < len(image) and image[r][c] == org_color:
            # above checks if the last cell has been
            # reached, and checks if color is org_color
            image[r][c] = nc
            # changes the color
            dfs(r + 1, c)
            # why the r + 1 is done?
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

    dfs(sr, sc)
    return image


print(flood_fill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, nc=2))
