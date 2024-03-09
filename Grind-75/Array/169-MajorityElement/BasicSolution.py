from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # iterate over range of array length
            counter = sum(1 for number in nums if number == nums[i])
            # run a loop over all elems, and count occurence
            if counter > len(nums) // 2:
                # return the majority value
                return nums[i]
