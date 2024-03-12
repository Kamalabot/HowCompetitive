from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1  # set two points

        while left <= right:  # loop until left is less than right
            mid = (left+right) // 2  # get the mid index
            if nums[mid] == target:  # check if mid num is tgt
                return mid  # return
            elif nums[mid] < target:  # if mid num is < tgt
                left = mid + 1  # move the left after mid
            else:
                right = mid - 1  # move the right before mid

        return -1
