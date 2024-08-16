from typing import List


def sort_me(in_arr: List[int]):
    for i in range(1, len(in_arr)):
        key = in_arr[i]

        j = i - 1  # this makes j to trail i

        while j >= 0 and key < in_arr[j]:
            in_arr[j + 1] = in_arr[j]
            j -= 1

        in_arr[j + 1] = key

    return in_arr


int_list = [5, 7, 6, 9, 3, 1, 4, 8, 0, 11, 76, 98]
print(sort_me(int_list))
