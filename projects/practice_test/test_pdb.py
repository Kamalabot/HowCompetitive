# implementing logic in python code and debugging them
from typing import Dict

def logic(a, b):
    low = a < b
    # breakpoint()
    high = a > b
    if high:
        return high
    else:
        return low

def recurse(one):
    if one == 0:
        print(0)
        return
    print(one)
    return recurse(one - 1)

import sys
sys.setrecursionlimit(1500)

def fibo_recurse(idx: int, cache: Dict = dict()):
    # check if the number calculated is in cache
    if idx in cache:
        # then return the value from the cache
        return cache[idx]
    # edge cases
    if idx == 0:
        return 0
    if idx == 1:
        return 1
    # print(idx)
    # save the result in temp variable
    temp = fibo_recurse(idx - 1, cache) + fibo_recurse(idx - 2, cache)
    # update the cache table
    cache[idx] = temp
    # return the value from the cache table
    return cache[idx]

inp1 = int(input('get a: '))
# inp2 = int(input('get b: '))
# import pdb; pdb.set_trace()
# print(logic(inp1, inp2))
print(fibo_recurse(inp1))
