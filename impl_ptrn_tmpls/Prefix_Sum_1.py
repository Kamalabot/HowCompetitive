# Pattern: Prefix Sum
# Introduction: Prefix Sum involves preprocessing an array to create a new array where each element at index i 
# represents the sum of the array from the start up to i. This allows for efficient sum queries on subarrays.

# Sample Problem: Given an array nums, answer multiple queries about the sum of elements within a specific range [i, j].
# Input: nums = [1, 2, 3, 4, 5, 6], i = 1, j = 3
# Output: 9

# Example Implementation:
def prefix_sum(nums, i, j):
    P = [0] * len(nums)
    P[0] = nums[0]
    for k in range(1, len(nums)):
        P[k] = P[k-1] + nums[k]
    return P[j] - P[i-1]

# LeetCode Problems: 
# - Range Sum Query - Immutable (LeetCode #303)
# - Contiguous Array (LeetCode #525)
# - Subarray Sum Equals K (LeetCode #560)
