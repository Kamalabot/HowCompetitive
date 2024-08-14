# Pattern: Monotonic Stack
# Introduction: The Monotonic Stack pattern uses a stack to maintain a sequence of elements in a specific order 
# (increasing or decreasing).

# Sample Problem: Find the next greater element for each element in an array. Output -1 if the greater element doesn’t exist.
# Input: nums = [2, 1, 2, 4, 3]
# Output: [4, 2, 4, -1, -1]

# Example Implementation:
def nextGreaterElements(nums):
    result = [-1] * len(nums)
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result

# LeetCode Problems:
# - Next Greater Element I (LeetCode #496)
# - Daily Temperatures (LeetCode #739)
# - Largest Rectangle in Histogram (LeetCode #84)
