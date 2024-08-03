# Implementation of recursive sum function 
from typing import List


# def sum(arr: List[int]) -> int:
#     if len(arr) == 0:
#         return 0
# 
#     x = arr.pop(0)
#     return x + sum(arr)


# print(sum([5, 8, 6]))# 19
# print(sum([55, 7, 86, 90, 88, 68]))# 394
# print(sum([55, 7, 86, 90, 88, 68, 57, 98, 62]))# 611


def sum(arr: List[int]) -> int:
    return _sum(arr, 0)


def _sum(arr, ind):

    if (ind == len(arr)):
        return 0
    
    return arr[ind] + _sum(arr, ind + 1)


print(sum([5, 8, 6])) # 19
print(sum([55, 7, 86, 90, 88, 68])) # 394
print(sum([55, 7, 86, 90, 88, 68, 57, 98, 62])) # 394
