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

print(wlist)

heap_list = []

# pushing the items into the heap_list
[heappush(heap_list, item) for item in wlist]

print(heap_list)

print("Lets see what heapify does?")
heapify(wlist)  # when the list is fully available
# then it is better to use the heapify
print(wlist)

# [10, 25, 45, 70, 35, 50, 55, 70, 80, 100]
# the below must pop 10, which is the lowest element

print("Working on the pop: 1st Element", heappop(heap_list))

# then share the updated heap as below

print(f"Updated heap is : {heap_list}")

# making a negative random numbers

# neglist = [-1 * randrange(10, 106, 5) for _ in range(10)]
# print(neglist)

neglist = [-45, -55, -45, -75, -100, -80, -40, -95, -20, -40]

print(neglist)

neg_heap = []

[heappush(neg_heap, item) for item in neglist]

print(neg_heap)

# popping from the heap will return 100

print(f"the top element is: {-1 * heappop(neg_heap)}")

print(f"the 1st largest, {nlargest(1, heap_list)}")
print(f"the 1st largest, {nsmallest(1, heap_list)}")
# merge returns a generator
print(f"Merge in workin: {list(merge(neglist, heap_list))}")
