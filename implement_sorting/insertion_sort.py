def insertion_sort(arr):
    # traverse 1 through arr_length
    for i in range(1, len(arr)):
        # curr element inserted in sorted portion
        key = arr[i]  # here the i = 1
        # move the element that are greater than
        # key to the right
        # i = 1, j = 0
        # i = 2, j = 1
        j = i - 1
        # movin the elements
        # j = 0 and key is compared to earlier elm
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            # reducing j
            j -= 1
        # if the while loop is bypassed
        arr[j + 1] = key

        print(f"loop :{i}")
        print(f"Array Status: {arr}")

    return arr


int_list = [5, 6, 1, 10, 7, 8, 9, 12, 15, 4]
# changing the last elm to be small

print(insertion_sort(int_list))
