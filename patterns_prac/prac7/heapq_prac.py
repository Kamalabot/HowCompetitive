# script is exploration of the heapq module
from heapq import (
    heapify,
    heappop,
    heappush,
    nlargest,
    nsmallest,
    merge,  # multiple sorted inputs one one sorted output
)
from random import randrange

## idea is to a take a random list of numbers
# and then push into the heap, and see
# how the work

# wlist = [randrange(10, 106, 5) for _ in range(10)]
wlist = [80, 35, 45, 70, 10, 50, 55, 25, 70, 100]

# create a heap_list
heap_list = []

# pushing the items into the heap_list
[heappush(heap_list, elm) for elm in wlist]
print("Printing heaped list:", heap_list)
# heapify a given list inplace and check
heapify(wlist)
# pop the top element
print(f"Popping from the heapified list: {heappop(wlist)}")
# check the update list
print(wlist)

neglist = [-45, -55, -45, -75, -100, -80, -40, -95, -20, -40]

# do the above for a negative list
neg_heap = []
[heappush(neg_heap, elm) for elm in neglist]
print(neg_heap)

# merge the lists and checkrint(wlist)
merge_heap = merge(neg_heap, wlist)

print("Merged heap", list(merge_heap))

print(type(merge_heap))
