# this is dp based grid traveller

# Given a n x n grid starting at top left
# find how many ways you can reach the
# bottom right corner. You can move right & down


def gt(m, n):
    # Initialize a 2D DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Base case
    dp[1][1] = 1

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                continue  # Skip the base case
            dp[i][j] = (dp[i - 1][j] if i > 1 else 0) + (
                dp[i][j - 1] if j > 1 else 0
            )  # Recurrence relation
            # number of ways to reach the cell above curr
            # number of ways to reach the cell left of curr

    return dp[m][n]
