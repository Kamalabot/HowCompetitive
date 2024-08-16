# Pattern: Modified Binary Search
# Introduction:
# Adapts binary search to solve a wider range of problems, such as finding elements in rotated sorted arrays.
# Use this pattern for problems involving sorted or rotated arrays where you need to find a specific element.

# Sample Problem:
# Find an element in a rotated sorted array.

# intuition 1: Two pointer approach, and get the mid value
# Intuition 2: As the array is sorted, we can check if target is less than mid
# Intuition 3: Move the left and right pointers depending on the target status
# in modified there is addition check if target is between mid in left / mid and right


def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[right] >= target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


print(search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
print(search_rotated_array([4, 5, 6, 7, 0, 1, 2], 4))  # Output: 0
print(search_rotated_array([4, 5, 6, 7, 0, 1, 2], 10))  # Output: -1

# LeetCode Problems:
# 1. Search in Rotated Sorted Array (LeetCode #33)
# 2. Find Minimum in Rotated Sorted Array (LeetCode #153)
# 3. Search a 2D Matrix II (LeetCode #240)
