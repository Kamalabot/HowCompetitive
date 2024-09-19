from typing import List


# Given an array of integers, return a new array such that each element at index i of
# the new array is the product of all the numbers in the original array except
# the one at i, without using division.


def array_multiplier(numlist: List[int]) -> List[int]:
    """Greedy Algorithm"""
    # Create a main result array
    result = [1] * len(numlist)

    # create empty result_before array
    result_before = [1] * len(numlist)
    pdt_so_far = 1

    # loop over the given list:
    for ind, num in enumerate(numlist):
        # 	assign the product of element multiplied so far to result_before list, at "ind" index
        result_before[ind] = pdt_so_far  # result_before = 1, 5, 40, 240
        #   Multiply the current element to pdt_so_far
        pdt_so_far *= num  # pdt_so_far = 5 | 40 | 240 | 360 < last 360 wont enter into result_before

    # create empty result_after array
    result_after = [1] * len(numlist)
    pdt_after = 1

    # loop over the given list in reverse:
    for i in range(len(numlist), 0, -1):
        # 	assign the product of element multiplied so far to result_after list, at "i" index
        result_after[i - 1] = pdt_after  # result_after =  432, 54, 9, 1
        # 	calculate product
        pdt_after *= numlist[i - 1]  # num_list = 9 | 54 | 432 | 2160

    print("before: ", result_before)
    print("after: ", result_after)

    # loop over the range of array elements
    for i in range(len(numlist)):
        # 	multiply the before, after product place the it in result[i]
        result[i] = result_before[i] * result_after[i]
    # return result
    return result
