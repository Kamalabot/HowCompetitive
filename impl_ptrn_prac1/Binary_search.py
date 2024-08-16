# Given a sorted array of n integers, write a function to search for a target value
# using the Binary Search algorithm. The function should return the index of the target
# if it is found in the array. If the target is not found, return -1.

# Binary Search is an efficient algorithm for finding an item from a sorted list of items.
# It works by repeatedly dividing the portion of the array that could contain the item in
# half until you've narrowed down the possible locations to just one.

# intuition 1: create left and right (two) pointers
# intuition 2: ensure the right doesn't go below left
# intuition 3: check if target below mid or above and
# move the left and right


def binary_search(nums, target):
    # start with left and right pointers
    left, right = 0, len(nums) - 1

    # ensure the right doesn't go below left
    while left <= right:
        # get the mid point
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # check if mid is lesser than target
        if nums[mid] < target:
            # discard the left side and move left to mid
            left = mid + 1
        else:
            # else discard the right side and move right to mid
            right = mid - 1

    return -1


# Example Input:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

# Example Output:
index = binary_search(nums, target)
print(
    f"Target {target} is found at index {index}"
)  # Output: Target 7 is found at index 6
