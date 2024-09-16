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

# create a heap_list

# pushing the items into the heap_list

# heapify a given list inplace and check

# pop the top element

# check the update list

neglist = [-45, -55, -45, -75, -100, -80, -40, -95, -20, -40]

# do the above for a negative list

# merge the lists and check
