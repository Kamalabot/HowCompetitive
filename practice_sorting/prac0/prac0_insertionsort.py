from typing import List

# intuition 1: key is going to from the 2nd element in the list
# intuition 2: use j to check if val at j is less than key, and
# assign that to j + 1 idx in list
# intuition 3+ assign val at  j + 1 to key


def insertion_sort(in_list: List[int]):
    # key is to traverse 1 to len(list)
    for i in range(1, len(in_list)):
        key = in_list[i]

        j = i - 1  # another idx

        # loop while the condition is tru
        while j >= 0 and key < in_list[j]:
            # here the sorting is happening
            in_list[j + 1] = in_list[j]
            # dec j
            j -= 1

        in_list[j + 1] = key

    return in_list


int_list = [5, 6, 1, 10, 7, 8, 9, 12, 15, 4]
# changing the last elm to be small

print(insertion_sort(int_list))
