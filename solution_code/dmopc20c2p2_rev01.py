#the longest scarf dmopc20c2p2

"""There is still error in the test cases when run in the judge"""

import sys

from typing import List

lst = input().split()

n = int(lst[0])

m = int(lst[1])

scarf = input().split()

for i in range(n):

    scarf[i] = int(scarf[i])
    
leftmost_index = {}
    
rightmost_index = {}
    
for i in range(n):

    color = scarf[i]

    if not color in leftmost_index:
        
        leftmost_index[color] = i
        
        rightmost_index[color] = i
    
    else:

        rightmost_index[color] = i
    
max_length = 0

for i in range(m):

    relative = input().split()

    first = int(relative[0])

    last = int(relative[1])

    if first in leftmost_index and last in leftmost_index:

        length = rightmost_index[last] - leftmost_index[first] + 1

    if length > max_length:
        
        max_length = length

print(max_length)