from typing import List

# intuition 1: if list is one element or less, just return
# intuition 2: take a pivot variable as the last before element
# intuition 3: enumerate over remaining range of elements, and
# append them to left / right list by checking with pivot
# intuition 4: recursively call left + [pivot] + right lists for sorting


def quick_sort(in_list: List[int]):
    pass


in_array = [1, 8, 7, 9, 0, 12, 15, 78, 68, 36]
print(quick_sort(in_array))
