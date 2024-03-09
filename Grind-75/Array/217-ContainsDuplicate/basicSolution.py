from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Using 2 pointer 
        for i in range(len(nums)):
            # enumerate elems in 2nd pointer till the end
            for j in range(i + 1, len(nums)):
                # check the nums match
                if nums[i] == nums[j]:
                    return True

        return False