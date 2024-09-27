# recurrence relation to find the max treasure
# dp[i][j] = treasure[i][j] + max(dp[i - 1][j], dp[i][j - 1])
# max treasure from above, below and curr cell


def max_treasure(treasure_map):
    # get dimensions of the given map
    rows = len(treasure_map)
    cols = len(treasure_map[0])

    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    # base case is starting point
    dp[0][0] = treasure_map[0][0]
    # fill first row of dp, only left side value
    for jdx in range(1, cols):
        dp[0][jdx] = dp[0][jdx - 1] + treasure_map[0][jdx]

    # fill for the 1st col
    for idx in range(1, rows):
        dp[idx][0] = dp[idx - 1][0] + treasure_map[idx][0]

    # fill for the rest of Dp cells
    for idx in range(1, rows):
        for jdx in range(1, cols):
            dp[idx][jdx] = treasure_map[idx][jdx] + max(
                dp[idx - 1][jdx], dp[idx][jdx - 1]
            )

    return dp[rows - 1][cols - 1]


tmap = [[0, 2, 2, 1], [3, 1, 1, 2], [4, 0, 2, 1], [2, 3, 2, 0]]

print(max_treasure(tmap))
