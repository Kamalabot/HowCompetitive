# Problem: Coin Change (LeetCode 322)
# This is a variation of the Unbounded Knapsack
# problem where we want to minimize
# the number of coins to make up a given amount.
from typing import List


def coinChange(coins: List[int], amount: int) -> float:
    # dp[i] reps the minimum coins needed
    dp = [float("inf")] * (amount + 1)
    # tabulation dp is used
    dp[0] = 0  # 0 coins reqd for 0 amount

    # process each coin, (this is recurring)
    for coin in coins:
        # iterate over curr coin to range of amount + 1
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


print(coinChange([1, 2, 5], 11))
