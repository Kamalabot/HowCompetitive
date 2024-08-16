from typing import List


def sort_me(in_arr: List[int]):
    if len(in_arr) > 1:
        mid = len(in_arr) // 2
        left = in_arr[:mid]
        right = in_arr[mid:]

        sort_me(left)
        sort_me(right)

        i = j = k = 0

        while len(left) > i and len(right) > j:
            if left[i] > right[j]:
                in_arr[k] = left[i]
                i += 1
            else:
                in_arr[k] = right[j]
                j += 1
            k += 1

        while len(left) > i:
            in_arr[k] = left[i]
            i += 1
            k += 1

        while len(right) > j:
            in_arr[k] = right[j]
            j += 1
            k += 1

    return in_arr


int_list = [5, 7, 6, 9, 3, 1, 4, 8, 0, 11, 76, 98]
print(sort_me(int_list))
