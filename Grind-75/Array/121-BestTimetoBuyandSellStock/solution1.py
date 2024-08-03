from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxGap = 0  # initialize maxgap variable
        left, right = 0, 1  # initialize left and right 0, 1
        while right < len(prices):
            # while right idx is less than list length
            # move to the right as long as values in right have bigger
            # numbers
            if prices[left] < prices[right]:
                # check if price to the right is bigger
                gap = prices[right] - prices[left]
                # calculate the profit gap
                maxGap = max(maxGap, gap)
                #  get the max of maxGap & diff of right - left
                right += 1  # increment the right by one
            else:
                # shift to the next pair
                left, right = right, right + 1
                # shift to the next pair

        return maxGap
