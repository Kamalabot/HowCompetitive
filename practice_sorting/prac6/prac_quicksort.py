from typing import List

# intuition 1: if list is one element or less, just return
# intuition 2: take a pivot variable as the last before element
# intuition 3: enumerate over remaining range of elements, and
# append them to left / right list by checking with pivot
# intuition 4: recursively call left + [pivot] + right lists for sorting


def quick_sort(in_list: List[int]):
    if len(in_list) < 1:
        return in_list

    pivot = in_list[len(in_list) - 1]
    left = []
    right = []

    for i in range(len(in_list) - 1):
        if in_list[i] < pivot:
            left.append(in_list[i])
        else:
            right.append(in_list[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


in_array = [1, 8, 7, 9, 0, 12, 15, 78, 68, 36]
print(quick_sort(in_array))
