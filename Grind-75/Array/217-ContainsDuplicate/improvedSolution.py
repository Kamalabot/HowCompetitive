from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Check if all values are unique"""
        nums.sort()  # sort the array in place
        # sorting process ensures that same numbers 
        # next to each other.
        print(nums)
        left, right = 0, 1  # Initiate adj pair index
        while right < len(nums):  # loop till array end
            if nums[left] == nums[right]:
                # check if elem as index are same 
                return True  # if so then true
            else:
                left, right = right, right + 1
                # else keep moving to the next pair

        return False


x = [1, 2, 5, 1, 6, 5]
soln = Solution()
print(soln.containsDuplicate(x))
