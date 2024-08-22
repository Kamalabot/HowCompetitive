from typing import List

# intuition 1: do sorting if list len is greate than 1, else return list
# intuition 2: divide the list into left and right at the mid point, recursively sort
# intuition 3: while left and right lists have elements to sort,
# compare each element, and assign the smallest to original array
# above intuition is checked by creating i, j, k = 0 and incremementing them after
# every comparison operator
# intuition 4: while there are more elements present in left / right list, then
# assign them individually to original array


def merge_sort(in_list: List[int]):
    if len(in_list) > 1:
        mid = len(in_list) // 2
        arleft = in_list[:mid]
        arright = in_list[mid:]
        merge_sort(arleft)
        merge_sort(arright)
        i = j = k = 0

        while i < len(arleft) and j < len(arright):
            if arleft[i] > arright[j]:
                in_list[k] = arleft[i]
                i += 1
            else:
                in_list[k] = arright[j]
                j += 1
            k += 1

        while i < len(arleft):
            in_list[k] = arleft[i]
            i += 1
            k += 1

        while j < len(arright):
            in_list[k] = arright[j]
            j += 1
            k += 1

    return in_list


in_array = [1, 8, 7, 9, 0, 12, 15, 78, 68, 36]
print(merge_sort(in_array))
