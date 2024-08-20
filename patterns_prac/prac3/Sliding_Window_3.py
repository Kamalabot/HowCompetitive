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
    sum_c = sum(nums[:k])
    max_s = sum_c
    for idx in range(k, len(nums)):
        sum_c += nums[idx] - nums[idx - k]
        max_s = max(sum_c, max_s)
    return max_s


nums = [2, 1, 5, 1, 3, 2]
k = 3

print(sliding_window(nums, k))
print(sliding_window([5, 6, 2, 3, 5, 1, 2, 9], 4))
# LeetCode Problems:
# - Maximum Average Subarray I (LeetCode #643)
# - Longest Substring Without Repeating Characters (LeetCode #3)
# - Minimum Window Substring (LeetCode #76)
