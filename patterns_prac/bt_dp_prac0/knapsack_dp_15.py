# Given weights and values of n items, put these items in a knapsack of capacity W
# to get the maximum total value in the knapsack. You can only take one of each item (0/1 knapsack).

# You can take one of each item, that is the key


def knapsack(weights, values, W):
    n = len(weights)
    # creating a 2d array, where the row is W+1 length and col is n+1 length
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    # enumerate each row
    for i in range(1, n + 1):
        # enumerate each weight val in the row
        # as the weights are increasing by 1
        for w in range(1, W + 1):
            # chk if current weight is can match the weight value
            if weights[i - 1] <= w:
                # below the dp array is filled by taking the
                # the max as shown below
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                # else use the value in earlier row's column
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]


# Example Input:
weights = [1, 2, 3]
values = [10, 15, 40]
W = 5

# Example Output:
print(knapsack(weights, values, W))  # Output: 55
