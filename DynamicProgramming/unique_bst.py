# Find the number of unique binary search trees


def numTrees(n):
    # DP array to store the number of unique BSTs
    dp = [0] * (n + 1)
    # base cases of 0 and 1 nodes,
    # with 1 way to arrange the nodes
    dp[0] = 1
    dp[1] = 1

    # fill the dp table with recurrence
    # catalan number
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    return dp[n]


n = 3
print(numTrees(n))
