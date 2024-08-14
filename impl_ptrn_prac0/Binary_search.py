# Given a sorted array of n integers, write a function to search for a target value
# using the Binary Search algorithm. The function should return the index of the target
# if it is found in the array. If the target is not found, return -1.

# Binary Search is an efficient algorithm for finding an item from a sorted list of items.
# It works by repeatedly dividing the portion of the array that could contain the item in
# half until you've narrowed down the possible locations to just one.


def binary_search(nums, target):
    # start by creating 2 pointers
    left, right = 0, len(nums) - 1
    # while the right doesn't cross the left
    while left <= right:
        # get the mid value of the range
        mid = left + (right - left) // 2

        # Check if target is present at mid
        if nums[mid] == target:
            return mid

        # If target is greater, ignore the left half
        elif nums[mid] < target:
            # move the left to mid + 1
            left = mid + 1

        # If target is smaller, ignore the right half
        else:
            # move the right to mid -1
            right = mid - 1

    # Target is not present in the array
    return -1


# Example Input:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

# Example Output:
index = binary_search(nums, target)
print(
    f"Target {target} is found at index {index}"
)  # Output: Target 7 is found at index 6
