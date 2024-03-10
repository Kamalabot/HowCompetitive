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
        # is empty array then
        return [[]]
    # split first and rest
    first, rest = arr[0], arr[1:]
    print(f'1st First: {first}')
    print(f'1st rest: {rest}')
    # enumerate elems of self-called-on(rest) n combine
    # how to visualise this? <<
    with_first = [[first] + comb for comb in combination(rest)]
    print("with first: ", with_first)
    # call self on rest
    without_first = combination(rest)
    print("without first: ", without_first)
    # return with and without first
    return with_first + without_first

# The solution has a completely different visualisation compared 
# the visualisation humans come up with mechanically.
# Visualisation will lead me to think from  

print(combination(['a', 'b', 'c']))