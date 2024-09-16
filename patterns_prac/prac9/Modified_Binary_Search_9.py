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

# intuition 4: Need to check if the left is smaller than mid
# intuition 4: Need to check if the left is smaller than mid
# to understand about the left and right side
# to understand about the left and right side
# intuition 4: Need to check if the left is smaller than mid
# to understand about the left and right side


def search_rotated_array(nums, target):
    pass


print(search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4

# LeetCode Problems:
# 1. Search in Rotated Sorted Array (LeetCode #33)
# 2. Find Minimum in Rotated Sorted Array (LeetCode #153)
# 3. Search a 2D Matrix II (LeetCode #240)
