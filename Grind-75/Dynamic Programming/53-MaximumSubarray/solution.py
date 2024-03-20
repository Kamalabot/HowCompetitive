from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):  # enumerate on the range of elems frm 1
            nums[i] = max(nums[i], nums[i-1] + nums[i])
            # given array itself is updated with max value of curr element
            # or the sum of current & previous element
        print(nums)
        return max(nums)


list_nums = [5, 7, 6, 2, 1, 9]

lsh = Solution()

print(lsh.maxSubArray(list_nums))
