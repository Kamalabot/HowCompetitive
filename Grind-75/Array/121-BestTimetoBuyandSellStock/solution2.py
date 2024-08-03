from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice, maxGap = float("inf"), 0
        for price in prices:  # for each given price
            buyPrice, maxGap = min(buyPrice, price), max(maxGap,
                                                         price - buyPrice)
            # get the min of the prices and make it buy price
            # get the max of the profit between price and buyprice

        return maxGap
