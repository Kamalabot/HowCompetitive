# Maximal Square Problem Statement
# You are given a 2D binary matrix (i.e., a matrix where each cell contains either 0 or 1), and your task is to find the largest square containing only 1s and return its area.

# Problem Breakdown:
# The input is a matrix of size m x n where each element is either 0 or 1.
# A square is defined as a region where every element inside is 1.
# You need to find the largest possible square (in terms of side length) that contains only 1s.
# Return the area of that square (side length squared).
# Example 1:
# plaintext
# Copy code
# Input:
# matrix = [
#   ["1", "0", "1", "0", "0"],
#   ["1", "0", "1", "1", "1"],
#   ["1", "1", "1", "1", "1"],
#   ["1", "0", "0", "1", "0"]
# ]

# Output: 4

# Explanation:
# The largest square has a side length of 2, so the area is 2 * 2 = 4.
# The square is formed at the bottom-right portion of the matrix:
# [
#   ["1", "1"],
#   ["1", "1"]
# ]


def maximalSquare(matrix):
    if not matrix:
        return 0

    # Dimensions of the matrix
    m, n = len(matrix), len(matrix[0])
    # DP table where dp[i][j] represents the size of the square with the bottom-right corner at (i, j)
    dp = [[0] * n for _ in range(m)]
    max_side = 0  # Track the maximum side length of the square

    # Fill the dp array
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                # If we're not in the first row or first column, take the min of three neighboring cells
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 1  # If we're at the border, the max square is 1
                max_side = max(max_side, dp[i][j])

    # The result is the area of the maximal square
    return max_side * max_side


# Example check
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(maximalSquare(matrix))  # Output: 4 (2x2 square)
