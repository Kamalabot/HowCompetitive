from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)  # get sum of given list elements
        if total_sum % 2 == 1:  # if odd then cannot proceed, and false
            return False

        half_sum = total_sum // 2  # get half sum
        memo = [True] + [False]*half_sum  # create memo
        for num in nums:
            for j in range(half_sum, num-1, -1):
                memo[j] |= memo[j-num]  # what does | do??

        """The |= operator in Python is the bitwise OR
        assignment operator. It performs a bitwise OR
        operation on the operands and assigns the result
        to the left operand."""

        return memo[half_sum]
