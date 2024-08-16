# Pattern: Monotonic Stack
# Introduction: The Monotonic Stack pattern uses a stack to maintain a sequence of elements in a specific order
# (increasing or decreasing).

# Sample Problem: Find the next greater element for each element
# inside the given list
# in an array. Output -1 if the greater element doesn’t exist.
# Input: nums = [2, 1, 2, 4, 3]
# Output indices of the next greater element: [4, 2, 4, -1, -1]
# actual value at the indices [3, 2, 3, -1, -1]
# There is no greater element for 3, as it is in the last
# theer is not greater element for 4, as it is the max

# intuition 1: stack is Implemented with list,
# and the entry, exit happens on right of the list

# Example Implementation:
def nextGreaterElements(nums):
    # create list of -1 equal to length of nums
    result = [-1] * len(nums)
    stack = []  # create empty stack
    for i in range(len(nums)):
        # stack = [0] nums[stack[-1]] = nums[0]
        # nums[0]< num[1]
        while stack and nums[stack[-1]] < nums[i]:
            # append the nums[i] as it is the next greater
            # to the results list
            result[stack.pop()] = nums[i]
        # idx is apppended to stack
        stack.append(i)
    return result


nums = [2, 1, 2, 4, 3]
print(nextGreaterElements(nums))

# LeetCode Problems:
# - Next Greater Element I (LeetCode #496)
# - Daily Temperatures (LeetCode #739)
# - Largest Rectangle in Histogram (LeetCode #84)
