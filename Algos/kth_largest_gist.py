# 1st approach:
def kth_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)


# 2nd approach:
def kth_largest(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k]


# 3rd approach:
import heapq

def kth_largest(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)