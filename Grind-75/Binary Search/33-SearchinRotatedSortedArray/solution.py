from typing import List

listn = [4, 5, 6, 7, 0, 1, 2, 3]
tgt = 4


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1  
        # objective is to have the search done in O(n) complexity 
        while left <= right:
            mid = left + (right-left) // 2  # only the unsorted part of the array is concentrated
            if nums[mid] == target:
                return mid  # found target then return mid

            if nums[mid] >= nums[left]:  # mid val is gt left val
                if nums[left] <= target < nums[mid]:  # left val is lte tgt and lt mid val
                    right = mid - 1  # move right by 1 step before the mid towards left
                else:
                    left = mid + 1  # else move left 1 step after mid, towards right
            else:  # mid val is lt left val
                if nums[mid] < target <= nums[right]:  # commenting this is not providing the
                    # necessary visualisation, which helps in intuition of problem being solved.
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


tl = Solution()
print(tl.search(listn, tgt))
