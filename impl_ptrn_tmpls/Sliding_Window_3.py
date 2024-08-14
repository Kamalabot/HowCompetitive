# Pattern: Sliding Window
# Introduction: The Sliding Window pattern is used to find a subarray or substring that satisfies a specific condition, 
# optimizing the time complexity by maintaining a window of elements.

# Sample Problem: Find the maximum sum of a subarray of size k.
# Input: nums = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9

# Example Implementation:
def sliding_window(nums, k):
    max_sum = sum(nums[:k])
    current_sum = max_sum
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum

# LeetCode Problems:
# - Maximum Average Subarray I (LeetCode #643)
# - Longest Substring Without Repeating Characters (LeetCode #3)
# - Minimum Window Substring (LeetCode #76)
