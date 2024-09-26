# Recurrence relation is
# dp[i] = dp[i - 1] + dp[i - 2]


def fib(n: int):
    # Create table where nth fib no
    # is stored
    dp = [0] * (n + 1)
    # update the base case
    dp[0] = 0
    dp[1] = 1
    # iteratively fill the dp table from 2
    for idx in range(2, n + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]

    return dp[n]
    # we are returning n here, since dp[0]
    # is not considered at all


print(fib(5))
print(fib(10))
