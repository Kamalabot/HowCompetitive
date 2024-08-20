# Given a sorted array of n integers, write a function to search for a target value
# using the Binary Search algorithm. The function should return the index of the target
# if it is found in the array. If the target is not found, return -1.

# Binary Search is an efficient algorithm for finding an item from a sorted list of items.
# It works by repeatedly dividing the portion of the array that could contain the item in
# half until you've narrowed down the possible locations to just one.

# intuition 0: the list has to be sorted for this to work
# intuition 1: two pointers are created at the extremes
# intuition 2: mid value is calculated and value @ mid is checked with target
# intuition 3: left or right is moved towards mid according to above chek


def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid - 1
        else:
            right = mid + 1

    return -1


# Example Input:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8

# Example Output:
index = binary_search(nums, target)
print(
    f"Target {target} is found at index {index}"
)  # Output: Target 7 is found at index 6
