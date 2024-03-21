from typing import List

# solution is tested & works


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)  # get sum of given list elements
        if total_sum % 2 == 1:  # if odd then cannot proceed, and false
            return False

        half_sum = total_sum // 2  # get half sum
        memo = [True] + [False]*half_sum  # create memo
        for num in nums:
            for j in range(half_sum, num-1, -1):
                memo[j] |= memo[j-num]  
                # what does | do?? acting as comparison operator not bitwise not operator
                # however the elements are boolean T/F so it becomes logical not
            print(f"For {num} : {memo}")
        """The |= operator in Python is the bitwise OR
        assignment operator. It performs a bitwise OR
        operation on the operands and assigns the result
        to the left operand."""
        """I think the |= is a not operator here. """

        return memo[half_sum]


nums = [1, 5, 11, 5]
sol = Solution()
print(sol.canPartition(nums))