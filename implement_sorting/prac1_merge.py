from typing import List


def sort_me(in_arr: List[int]):
    if len(in_arr) > 1:
        mid = len(in_arr) // 2
        left = in_arr[:mid]
        right = in_arr[mid:]
        sort_me(left)
        sort_me(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:  # ascending or descending is controlled here
                in_arr[k] = left[i]
                i += 1
            else:
                in_arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            in_arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            in_arr[k] = right[j]
            j += 1
            k += 1
    return in_arr


int_list = [5, 7, 6, 9, 3, 1, 4, 8, 0, 11, 76, 98]
print(sort_me(int_list))
