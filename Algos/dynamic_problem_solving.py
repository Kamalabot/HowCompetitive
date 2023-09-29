""" Fibonacci Sequence:

The Fibonacci sequence is a classic example for introducing dynamic programming. Here, we'll use dynamic programming to efficiently compute Fibonacci numbers:

"""
def fibonacci(n):
    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# Example usage:

print(fibonacci(10))  # Output: 55

""" Longest Common Subsequence (LCS):

The Longest Common Subsequence problem is a classic dynamic programming problem used in text comparison and DNA sequence analysis. Here's an implementation to find the length of the LCS of two sequences:

"""
def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

# Example usage:
s1 = "AGGTAB"
s2 = "GXTXAYB"
print(longest_common_subsequence(s1, s2))  # Output: 4 (LCS: "GTAB")
""" Knapsack Problem:

The Knapsack problem is a classic optimization problem where you need to find the most valuable combination of items to fit into a knapsack with a limited capacity. Here's an implementation to find the maximum value:

python
Copy code
 """
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

""" # Example usage:
weights = [2, 1, 3]
values = [4, 2, 3]
capacity = 4
print(knapsack(weights, values, capacity))  # Output: 7 (items 1 and 2)
 """

""" Other problems that can be solved 

4. Edit Distance (Intermediate):

Given two strings, determine the minimum number of operations (insertion, deletion, or substitution) required to transform one string into the other. Implement a Python function to find the edit distance (Levenshtein distance) between two strings using dynamic programming. This problem is often used in spell-checking, DNA sequence alignment, and text comparison.

5. Coin Change (Intermediate):

You are given an array of coin denominations and a total amount. Find the minimum number of coins needed to make up that amount. Implement a Python function to solve the Coin Change problem using dynamic programming. This problem is commonly encountered in making change for a given amount of money or optimizing coin usage in vending machines.

6. Rod Cutting (Intermediate):

You have a rod of length 'n' and a table that shows the price you can sell each piece of the rod for (different prices for different lengths). Find the maximum revenue you can obtain by cutting the rod into pieces. Implement a Python function to solve the Rod Cutting problem using dynamic programming. This problem is applicable in resource allocation and stock cutting scenarios.

 """