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
# intuition 2: start by assuming there are no nextGreaterElements for any element
# intuition 3: enumerate every element, and append it to stack
# intuition 4: use the while loop to work with stack and parallely check
# if current element in for loop iteration is greater to idx present in stack

# Example Implementation:
def nextGreaterElements(nums):
    pass


nums = [2, 1, 2, 4, 3]
print(nextGreaterElements(nums))

# LeetCode Problems:
# - Next Greater Element I (LeetCode #496)
# - Daily Temperatures (LeetCode #739)
# - Largest Rectangle in Histogram (LeetCode #84)
