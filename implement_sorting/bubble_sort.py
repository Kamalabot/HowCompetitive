def bubble_sort(arr):
    # get len of array
    n = len(arr)
    # create nested for loop
    for i in range(n):
        # last i elements are sorted
        # 0, 10 - 0 - 1
        # 0, 10 - 1 - 1
        # 0, 10 - 2 - 1
        print(f"loop I: {i}\n")
        for j in range(0, n - i - 1):
            # look at adj element
            # if elem found is greater than next
            # observe the j+1 below, it takes care
            # of the last element
            if arr[j] > arr[j + 1]:
                # swap it
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(f"loop J: {j}\n")
        # check the array each time its run
        # through inner loop
        print(arr[0 : n - i - 1])

    return arr


int_list = [5, 6, 1, 10, 7, 8, 9, 12, 15, 4]
# changing the last elm to be small

print(bubble_sort(int_list))
