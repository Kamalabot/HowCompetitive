def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])

    # Initialize the DP table
    dp = [[0] * n for _ in range(m)]

    # Starting position
    dp[0][0] = 1

    # Fill the first row
    for j in range(1, n):
        # check if the grid is having obstacle make dp cell to 0
        dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0

    # Fill the first column
    for i in range(1, m):
        # check if the grid is having obstacle make dp cell to 0
        dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0

    # Fill the rest of the DP table
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = 0

    return dp[m - 1][n - 1]


# Example usage
obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePathsWithObstacles(obstacleGrid))  # Output: 2
