# recurrence relation
# dp[idx]  = dp[idx - 1] * dp[idx -2]
# dp[idx]  = dp[idx - 1] * dp[idx]
# FOLLOWING IS THE CORRECT RECURRENCE
# dp[idx]  = dp[idx - 1] * idx


def factorial(n):
    # build DP table
    dp = [1 for _ in range(n + 1)]
    # base cases
    dp[0] = 1
    # dp[1] = 1
    # iterate from 2 to n + 1
    for idx in range(2, n + 1):
        dp[idx] = dp[idx - 1] * idx

    return dp[n]


print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(10))
