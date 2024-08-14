from typing import List


def sort_me(in_arr: List[int]):
    if len(in_arr) < 1:
        return in_arr

    left = []
    right = []

    # take a pivot, the last but one elem
    pivot = in_arr[len(in_arr) - 1]

    for i in range(len(in_arr) - 1):
        if in_arr[i] < pivot:
            left.append(in_arr[i])
        else:
            right.append(in_arr[i])

    return sort_me(left) + [pivot] + sort_me(right)


int_list = [5, 7, 6, 9, 3, 1, 4, 8, 0, 11, 76, 98]
print(sort_me(int_list))
