# Pattern: Top ‘K’ Elements
# Introduction: The Top 'K' Elements pattern finds the top k largest or smallest elements in an array or stream of data 
# using heaps or sorting.

# Sample Problem: Find the k-th largest element in an unsorted array.
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5

# Example Implementation:
import heapq

def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# LeetCode Problems:
# - Kth Largest Element in an Array (LeetCode #215)
# - Top K Frequent Elements (LeetCode #347)
# - Find K Pairs with Smallest Sums (LeetCode #373)
