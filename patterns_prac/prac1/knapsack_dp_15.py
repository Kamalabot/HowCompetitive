# Given weights and values of n items, put these items in a knapsack of capacity W
# to get the maximum total value in the knapsack. You can only take one of each item (0/1 knapsack).


def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]


# Example Input:
weights = [1, 2, 3]
values = [10, 15, 40]
W = 5

# Example Output:
print(knapsack(weights, values, W))  # Output: 55
