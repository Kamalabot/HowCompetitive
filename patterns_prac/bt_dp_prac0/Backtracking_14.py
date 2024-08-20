# Pattern: Backtracking
# Introduction:
# Explores all possible solutions and backtracks when a solution path fails.

# Sample Problem:
# Generate all permutations of a given list of numbers.
def permute_01(nums):
    "This is a function that was bit more complex"
    result = []

    def backtrack(path, options):
        if not options:
            result.append(path)
            return
        for i in range(len(options)):
            backtrack(path + [options[i]], options[:i] + options[i + 1 :])

    backtrack([], nums)
    return result


# pick an element from the list, and put it in current position
# explore the permuation of the remaining element
# Undo the element in the list
# Why undo the element in the list


def permute(nums):
    "Diving into BT, based on the idea that we are traversing the Decision Tree"

    def backtrack(start, end):
        # If we've reached the end of the list, add the current permutation to the result
        if start == end:  # this is the place to break out of the permutation
            result.append(nums[:])  # Make a copy of the current permutation
        for i in range(start, end):
            # Swap the current element with the starting element
            nums[start], nums[i] = nums[i], nums[start]

            # Recurse on the remaining elements
            backtrack(start + 1, end)

            # Backtrack (swap back to restore the original list)
            nums[start], nums[i] = nums[i], nums[start]

    # calling backtact(0, 3) in the permute function
    # for i in range(0, 3):
    # nums[0] , nums[0] = nums[0] ,nums[0]
    # backtrack(1, 3)
    # for i in range(1, 3):
    # nums[1] , nums[0] = nums[0] ,nums[1]
    # backtrack(2, 3)
    # for i in range(2, 3):
    # nums[2] , nums[0] = nums[0] ,nums[2]
    # backtrack(3, 3)
    # this will append nums [3, 2, 1] to result
    result = []
    # The result variable is accessed inside the backtrack
    backtrack(0, len(nums))
    #
    # above is the first call to the backtrack
    return result


print(permute([1, 2, 3]))

# Output: [[1,2,3], [1,3,2], [2,1,3], [2
# LeetCode Problems:
# 1. Permutations (LeetCode #46)
# 2. Subsets (LeetCode #78)
# 3. N-Queens (LeetCode #51)
