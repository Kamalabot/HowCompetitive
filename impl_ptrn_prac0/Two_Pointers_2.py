# Pattern: Two Pointers
# Introduction: The Two Pointers pattern involves using two pointers to iterate through an array or list, often used 
# to find pairs or elements that meet specific criteria.

# Sample Problem: Find two numbers in a sorted array that add up to a target value.
# Input: nums = [1, 2, 3, 4, 6], target = 6
# Output: [1, 3]

# Example Implementation:
def two_pointers(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return []

# LeetCode Problems:
# - Two Sum II - Input Array is Sorted (LeetCode #167)
# - 3Sum (LeetCode #15)
# - Container With Most Water (LeetCode #11)
