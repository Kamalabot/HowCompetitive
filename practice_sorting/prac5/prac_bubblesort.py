from typing import List


# intuition 1: loops over the entire list twice
# intuition 2: 2nd loop leaves the last element, from where
# the actual sorting / bubbling starts to occur
# intuition 3: swapped if next element is smaller than current
def bubble_sort(in_list: List[int]):
    n = len(in_list)
    for i in range(n):
        for j in range(n - i - 1):
            if in_list[j] > in_list[j + 1]:
                in_list[j], in_list[j + 1] = in_list[j + 1], in_list[j]
    return in_list


in_array = [1, 8, 7, 9, 0, 12, 15, 78, 68, 36]
print(bubble_sort(in_array))
