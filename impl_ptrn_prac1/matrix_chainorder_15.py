# Given a sequence of matrices, find the most efficient way to multiply these
# matrices together. The problem is not to perform the multiplications but merely
# to decide the order in which to perform the multiplications.

import sys


def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]


# Example Input:
p = [1, 2, 3, 4]

# Example Output:
print(matrix_chain_order(p))  # Output: 18
