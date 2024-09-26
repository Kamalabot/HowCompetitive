# recurrence relation here doesn't look at
# more than one step from the current cell
# so cannot get islands of connected buildings

# dp[idx][jdx] = 1 + min(dp[idx - 1][jdx], min(dp[idx][jdx - 1], dp[idx - 1][jdx - 1]))


def lgst_building(grid):
    rows = len(grid)
    cols = len(grid[0])

    # creating dp table
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # assign max_blk_size
    max_blk_size = 0

    for idx in range(0, rows):
        for jdx in range(0, cols):
            if grid[idx][jdx] == 1:
                if idx == 0 or jdx == 0:
                    dp[idx][jdx] = (
                        1  # first row / col has no                 dp[idx][jdx] = 1; # first row /dev
                    )
                else:
                    dp[idx][jdx] = 1 + min(
                        dp[idx - 1][jdx], min(dp[idx][jdx - 1], dp[idx - 1][jdx - 1])
                    )
                max_blk_size = max(dp[idx][jdx], max_blk_size)
    print("DP table:\n")
    for d in dp:
        print(d, end="\n")
    return max_blk_size


grid = [[1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]]

print(lgst_building(grid))
