# the dp table is going to be different
# dp[wt] = max(dp[wt], dp[wt - weights[idx]] + values[idx])
# wt is going to increment by 1 upto target


def unbounded_ks(weights, values, target):
    n = len(weights)

    dp = [0 for _ in range(target + 1)]

    # iterate over all weights 1 to target + 1
    for wt in range(1, target + 1):
        for idx in range(n):  # iterate over items
            if weights[idx] <= wt:
                dp[wt] = max(dp[wt], dp[wt - weights[idx]] + values[idx])
    print(f"Dp Table is: {dp}")
    return dp[target]


weights = [1, 2, 3, 4]
values = [10, 15, 30, 25]

print(unbounded_ks(weights, values, 2))
