# variant of fibonacci


def climbing_stairs(n):
    if n == 1:
        return 1
    # dp table
    dp = [0] * (n + 1)
    # base case using the problem statement
    dp[1] = 1
    dp[2] = 2
    # iterate over 3 till n + 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # return the nth dp value
    return dp[n]


print(climbing_stairs(4))
print(climbing_stairs(5))
