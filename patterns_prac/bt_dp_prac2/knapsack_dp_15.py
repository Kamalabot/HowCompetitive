# Need a 2D array to maintain the weights
# value of the items

# recurrence relation is
# dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w- wt[i - 1]])

# you can take only one of each item


def knapsack(weights, values, W):
    n = len(weights)  # w and v will be same length
    # create the dp table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    # dp[0][0] = 0 as there is no weight and value
    # go through the filling process from "1, 1"
    # with above recurrence relation
    for idx in range(1, n + 1):
        # we are solving 1kg to Wkg knapsack
        for wdx in range(1, W + 1):
            # chek if current weight can match
            # current knapsack weight
            if weights[idx - 1] <= wdx:
                dp[idx][wdx] = max(
                    dp[idx - 1][wdx],
                    dp[idx - 1][wdx - weights[idx - 1]] + values[idx - 1],
                )
            else:
                dp[idx][wdx] = dp[idx - 1][wdx]

    print("Filled up DP:\n")
    # printing the filled dp
    for wdx in dp:
        print(wdx, end="\n")
    # return the lower right corner element
    return dp[n][W]


weights = [1, 2, 3, 4]
values = [10, 15, 40, 25]

print(knapsack(weights, values, 8))  # 75
print(knapsack(weights, values, 2))  # 15
# there will be 8 columns in the DP table
