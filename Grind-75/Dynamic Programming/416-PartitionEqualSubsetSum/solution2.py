from typing import List

# need to review the bitwise operation before
# completing this commenting

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)  # get the total sum
        if total_sum % 2 != 0:  # check if it is even
            return False  # if not, then cannot partition
        # 
        half_sum, bit = total_sum // 2, 1
        for num in nums:
            bit |= bit << num

        return bit & 1 << half_sum  # The return answer is wrong


nums = [1, 5, 11, 5]
sol = Solution()
print(sol.canPartition(nums))