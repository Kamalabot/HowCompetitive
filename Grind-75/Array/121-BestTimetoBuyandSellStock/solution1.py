from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxGap = 0  # initialize maxgap variable
        left, right = 0, 1  # initialize left and right 0, 1
        while right < len(prices):  # while the right is less than list
            if prices[left] < prices[right]:
                # check if price @ left < price @ right
                maxGap = max(maxGap, prices[right] - prices[left])
                #  get the max of maxGap & diff of right - left
                right += 1  # increment the right by one
            else:
                # price @ left > price @ right
                left, right = right, right + 1
                # shift to the next pair

        return maxGap
