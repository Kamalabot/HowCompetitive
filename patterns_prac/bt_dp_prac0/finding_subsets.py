def backtrack(start, path, result, nums):
    # Add the current subset (path) to the result
    result.append(list(path))

    # Explore further decisions
    for i in range(start, len(nums)):
        # Include nums[i] in the current subset
        path.append(nums[i])

        # Move to the next element and make further decisions
        backtrack(i + 1, path, result, nums)

        # Backtrack: remove the last element and try the next possibility
        path.pop()


def subsets(nums):
    result = []
    backtrack(0, [], result, nums)
    return result


# Example usage
nums = [1, 2, 3]
output = subsets(nums)
print(output)

# Initial Call:
# Start with an empty subset (path = []) and start index (start = 0).

# Adding Subsets:
# For each element, decide to include it in the current subset (path.append(nums[i])).

# Recursively explore further by calling backtrack(i + 1, path, result, nums).

# Backtracking:
# After exploring all subsets that include the current element, backtrack by removing
# it (path.pop()) and try the next element.

# Base Case:
# Each time we reach the end of the list, the current subset is added to the result.

# Start with [].
# Add 1 → [1].
# Add 2 → [1, 2].
# Add 3 → [1, 2, 3].
# Backtrack to [1, 2] (remove 3), try adding 3 again.
# Backtrack to [1] (remove 2), try adding 2, then 3.
# Repeat for [2] and [3] subsets.
