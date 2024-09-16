# Pattern: Top ‘K’ Elements
# Introduction: The Top 'K' Elements pattern finds the top k largest or smallest elements in an array or stream of data
# using heaps or sorting.

# Sample Problem: Find the k-th largest element in an unsorted array.
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5

# intuition 1: can use heapq to get the nlargest elements
# intution 2: can use sorting and then get the elements
# information 1: heapq is an array where a[idx] < a[2 * idx + 1] and
# a[idx] < a[2 * idx + 2]


# Example Implementation:
import heapq


def findKthLargest(nums, k):
    pass


nums = [3, 2, 1, 5, 6, 4]
k = 3
print(findKthLargest(nums, k))

# LeetCode Problems:
# - Kth Largest Element in an Array (LeetCode #215)
# - Top K Frequent Elements (LeetCode #347)
# - Find K Pairs with Smallest Sums (LeetCode #373)
