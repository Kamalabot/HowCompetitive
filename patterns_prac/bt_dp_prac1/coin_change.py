# Variation of unbounded knapsack
# create dp table of "inf" for amount + 1
# Recurrence relation
# dp[idx] = min(dp[idx], dp[idx - coin] + 1)
# where coin is individual given coins
# Iteration :
# iterate over range of coin to amount + 1


def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)

    dp[0] = 0  # 0 coins for 0 amount

    for coin in coins:
        for idx in range(coin, amount + 1):
            dp[idx] = min(dp[idx], dp[idx - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


print(coin_change([1, 2, 5, 10], 25))
