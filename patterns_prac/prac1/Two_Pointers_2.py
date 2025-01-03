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
        sum = nums[left] + nums[right]
        # check if the sum is equal to tgt
        if sum == target:
            return [left, right]
        if sum > target:
            right -= 1
        else:
            left += 1
    # if not finding, then return empty []
    return []


nums = [1, 2, 3, 4, 6]
target = 6

print(two_pointers(nums, target))
print(two_pointers(nums, 9))

# LeetCode Problems:
# - Two Sum II - Input Array is Sorted (LeetCode #167)
# - 3Sum (LeetCode #15)
# - Container With Most Water (LeetCode #11)
