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
    # check if the in_list has more than 1 elem
    if len(in_list) > 1:
        # get the mid of the list
        mid = len(in_list) // 2

        # split the list into 2 halves
        right_list = in_list[mid:]
        left_list = in_list[:mid]

        # call merge_sort on both of them
        merge_sort(left_list)
        merge_sort(right_list)

        # define 3 indices
        i = j = k = 0

        # while len of left and right half are not less than i & j
        while i < len(left_list) and j < len(right_list):
            # check value on right and left half @ i and j
            if left_list[i] < right_list[j]:
                # assign lower value to arr[k]
                in_list[k] = left_list[i]
                # increment i
                i += 1
            else:
                in_list[k] = right_list[j]
                j += 1
            # move the k to next step
            k += 1

        # need to increment i, j and k when above while loop doesn't exec
        while i < len(left_list):
            in_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            in_list[k] = right_list[j]
            j += 1
            k += 1

    return in_list


in_array = [1, 8, 7, 9, 0, 12, 15, 78, 68, 36]
print(merge_sort(in_array))
