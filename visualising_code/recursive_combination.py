# This code implements finding the combinations of a given array 
from typing import List


def combine_00(arr: List[int]) -> List[List[int]]:

    if len(arr) == 0:
        return [arr]

    firstEl = arr.pop(0)

    combWOFirst = combine_00(arr)

    combWFirst = []

    for comb in combWOFirst:
        comb.append(firstEl)
        combWFirst.append(comb)
    
    return [combWOFirst, combWFirst]


# print(combine_00(['a', 'y', 'z']))

def combination(arr):

    if not arr:
        return [[]]

    first, rest = arr[0], arr[1:]
    with_first = [[first] + comb for comb in combination(rest)]
    without_first = combination(rest)
    return with_first + without_first

    
print(combination(['a', 'y', 'z']))