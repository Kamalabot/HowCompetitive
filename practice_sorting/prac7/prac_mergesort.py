from typing import List

# intuition 1: do sorting if list len is greate than 1, else return list
# intuition 2: divide the list into left and right at the mid point, recursively sort
# intuition 3: while left and right lists have elements to sort,
# compare each element, and assign the smallest to original array
# above intuition is checked by creating i, j, k = 0 and incremementing them after
# every comparison operator
# intuition 4: while there are more elements present in left / right list, then
# assign them individually to original array


def merge_sort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        left = mylist[:mid]
        right = mylist[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                mylist[k] = left[i]
                i += 1
            else:
                mylist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            mylist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            mylist[k] = right[j]
            j += 1
            k += 1
    return mylist


in_array = [1, 8, 7, 9, 0, 12, 15, 78, 68, 36]

print(merge_sort(in_array))
