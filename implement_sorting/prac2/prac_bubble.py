from typing import List


def sort_me(in_arr: List[int]):
    n = len(in_arr)
    for i in range(n):
        for j in range(n - i - 1):
            if in_arr[j] > in_arr[j + 1]:
                in_arr[j], in_arr[j + 1] = in_arr[j + 1], in_arr[j]
    return in_arr


int_list = [5, 7, 6, 9, 3, 1, 4, 8, 0, 11, 76, 98]
print(sort_me(int_list))
