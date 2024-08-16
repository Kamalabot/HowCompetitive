# start by dividing the array into halves
# sort each half, and then merge them back
def merge_sort(arr):
    # check length of array is > 1
    # this condition break the recursion
    if len(arr) > 1:
        mid = len(arr) // 2

        left_half = arr[:mid]
        right_half = arr[mid:]

        # recursivel sort each half
        merge_sort(left_half)
        # when this is returned,
        # the processed left half comes back
        print(f"Processed left half: {left_half}")

        merge_sort(right_half)
        print(f"Processed right half: {right_half}")

        # During the 1st call, the stack will be
        # first filled with left_half of the tree
        i = j = k = 0
        # i tracks left half,
        # j tracks right half
        # k tracks the main array

        # Below itself the sorting of the array is completed
        while i < len(left_half) and j < len(right_half):
            # start assigning the lowest value to
            # initial locations in arr
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        # why are we doing this part?

        # to check if there are any element is left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # to check if there are any element is right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    # when reaching the bottom of tree
    # there will be one element on each
    # side of the tree.
    return arr


int_list = [5, 6, 1, 10, 7, 8, 9, 12, 15, 4]
# changing the last elm to be small

print(merge_sort(int_list))
