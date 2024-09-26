# Given a sequence of matrices, find the most efficient way to multiply these
# matrices together. The problem is not to perform the multiplications but merely
# to decide the order in which to perform the multiplications.
# recurrence reln explainer
# The number of scalar multiplications required for the left subchain (dp[i][k]),
# The number of scalar multiplications required for the right subchain (dp[k+1][j]),
# The "cost to multiply" the two resulting matrices (determined by the dimensions p[i], p[k+1], and p[j+1]).

import sys


def matrix_chain_order(p):
    n = len(p) - 1
    # n considered is one less than actual length
    dp = [[0] * n for _ in range(n)]
    # there seems to be no base case
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            # Initialization: By setting dp[i][j] to sys.maxsize, the
            # algorithm ensures that any calculated cost will be smaller,
            # allowing the min function to correctly update dp[i][j] wih
            # min cost from calculation
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]


# The **cost** refers to the number of **scalar multiplications** required to
# multiply two matrices. The cost of multiplying two matrices of dimensions
# `a x b` and `b x c` is `a * b * c`. The goal of the problem is to minimize
# the total number of such scalar multiplications for multiplying the
# entire chain of matrices.

# Example Input:
p = [1, 2, 3, 4]

# If you have matrices with dimensions 10x20, 20x30, and 30x40, then `p = [10, 20, 30, 40]`.
# The algorithm finds the optimal way to group these
# matrices to minimize the total cost of multiplication.

# Example Output:
print(matrix_chain_order(p))  # Output: 18
