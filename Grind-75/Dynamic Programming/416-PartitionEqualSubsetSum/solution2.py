from typing import List

# need to review the bitwise operation before
# completing this commenting

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 0:
            return False

        half_sum, bit = total_sum // 2, 1
        for num in nums:
            bit |= bit << num

        return bit & 1 << half_sum
