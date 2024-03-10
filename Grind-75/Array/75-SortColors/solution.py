from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, mid, right = 0, 0, len(nums)-1  # three pointers created
        while mid <= right:  # until mid is less than right
            if nums[mid] == 0:  # value in mid is 0
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
                # swap the mid and left, initially this seems redundant
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                # if mid value is 2, then push it to the end
                right -= 1
                # move the right one step to left
            else:  # mid is 1 then jus increment mid
                mid += 1
