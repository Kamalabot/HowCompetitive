# problem statement: Recursively get the sum of the given array

from typing import List

# intuition 0: if no elements, find that using len(in_list) and return 0
# intuition 1: if one element, then send the value of the element
# intuition 2: return first_element + call sum_r on rest of list elments


def sum_r(in_list: List[int]):
    if len(in_list) == 0:
        return 0
    if len(in_list) == 1:
        return in_list[0]

    return in_list[0] + sum_r(in_list[1:])


print(sum_r([5, 2, 1, 8]))
print(sum_r([5, -2, 1, 8]))
print(sum_r([6, 3, 1]))
