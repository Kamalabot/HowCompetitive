from typing import List


# intuition 1: loops over the entire list twice
# intuition 2: 2nd loop leaves the last element, from where
# the actual sorting / bubbling starts to occur
# intuition 3: swapped if next element is smaller than current


def bubble_sort(in_list: List[int]):
    n = len(in_list)
    for i in range(n):
        print(f"i: {i}")
        # range has to be positive, else the loop will not start
        for j in range(n - i - 1):
            print(f"j: {j}")
            if in_list[j] > in_list[j + 1]:
                in_list[j], in_list[j + 1] = in_list[j + 1], in_list[j]
    print(len(in_list))
    return in_list


in_array = [1, 8, 7, 9, 0, 12, 15, 78, 68, 36]
print(bubble_sort(in_array))
