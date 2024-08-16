def quick_sort(arr):
    if len(arr) <= 1:
        # if arr is less than 2 elems,
        # which means its a single elem array
        # the array is sorted
        return arr
    # choose a arbitrary pivot
    pivot = arr[len(arr) - 1]

    # initialize left and right array
    left = []
    right = []

    # loop through all the elements except pivot
    for i in range(len(arr) - 1):
        # if less than pivot append to left
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            # else append to right
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


int_list = [5, 6, 1, 10, 7, 8, 9, 12, 15, 4]
# changing the last elm to be small

print(quick_sort(int_list))
