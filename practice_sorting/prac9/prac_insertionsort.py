from typing import List

# intuition 1: key is going to from the 2nd element in the list
# intuition 2: use j to check if val at j is less than key, and
# assign that to j + 1 idx in list
# intuition 3+ assign val at  j + 1 to key


def insertion_sort(in_list: List[int]):
    for idx in range(1, len(in_list)):
        key = in_list[idx]
        jdx = idx - 1
        while jdx >= 0 and in_list[jdx] < key:
            in_list[jdx + 1] = in_list[jdx]
            jdx -= 1
        in_list[jdx + 1] = key

    return in_list


int_list = [5, 6, 1, 10, 7, 8, 9, 12, 15, 4]
# changing the last elm to be small

print(insertion_sort(int_list))
