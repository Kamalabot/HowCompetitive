# Pattern: Two Pointers
# Introduction: The Two Pointers pattern involves using two pointers to iterate through an array or list, often used
# to find pairs or elements that meet specific criteria.

# Sample Problem: Find two numbers in a sorted array that add up to a target value.
# Input: nums = [1, 2, 3, 4, 6], target = 6
# Output: [1, 3]

# intuition 1: right end pointer is at len(array) - 1
# intuition 2: left ptr will have smaller values compared to
#               right as the array is sorted
# intuition 3: moving the ptrs depend on intuition 2

# Example Implementation:
def two_pointers(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if target < nums[mid]:  # if target is less than mid element
            # if nums[mid] < target:  # if mid element is less than target
            right = mid - 1
        else:
            left = mid + 1
    return -1


nums = [1, 2, 3, 4, 6]
target = 6

print(two_pointers(nums, target))

# LeetCode Problems:
# - Two Sum II - Input Array is Sorted (LeetCode #167)
# - 3Sum (LeetCode #15)
# - Container With Most Water (LeetCode #11)
