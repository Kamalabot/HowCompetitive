# Pattern: Sliding Window
# Introduction: The Sliding Window pattern is used to find a subarray or substring that satisfies a specific condition,
# optimizing the time complexity by maintaining a window of elements.

# Sample Problem: Find the maximum sum of a subarray of size k.
# Input: nums = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9

# intuition 1: create a sub array of k size
# intuition 2: append and pop from the sub array
# intuition 3: since you are getting sum, subtract and add
# intuition 4: you are subtracting element in front of subarray

# Example Implementation:
def sliding_window(nums, k):
    pass


nums = [2, 1, 5, 1, 3, 2]
k = 3

print(sliding_window(nums, k))
# LeetCode Problems:
# - Maximum Average Subarray I (LeetCode #643)
# - Longest Substring Without Repeating Characters (LeetCode #3)
# - Minimum Window Substring (LeetCode #76)
