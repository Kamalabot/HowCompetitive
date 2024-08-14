from typing import List


def bubble_sort(in_list: List[int]):
    # print(in_list)
    # get length of list
    n = len(in_list)
    # use i to loop over the list till end
    for i in range(n):
        # use j to loop over
        for j in range(n - i - 1):
            # check if adjacent value is bigger than curr value
            if in_list[j] > in_list[j + 1]:
                # swap them
                in_list[j], in_list[j + 1] = in_list[j + 1], in_list[j]
    return in_list


in_array = [1, 8, 7, 9, 0, 12, 15, 78, 68, 36]
print(bubble_sort(in_array))