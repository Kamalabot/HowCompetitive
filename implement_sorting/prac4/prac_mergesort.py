from typing import List

# intuition 1: do sorting if list len is greate than 1, else return list
# intuition 2: divide the list into left and right at the mid point, recursively sort
# intuition 3: while left and right lists have elements to sort,
# compare each element, and assign the smallest to original array
# above intuition is checked by creating i, j, k = 0 and incremementing them after
# every comparison operator
# intuition 4: while there are more elements present in left / right list, then
# assign them individually to original array


def merge_sort(in_list: List[int]):
    pass


in_array = [1, 8, 7, 9, 0, 12, 15, 78, 68, 36]
print(merge_sort(in_array))
