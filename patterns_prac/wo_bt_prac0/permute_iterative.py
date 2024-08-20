# we want have list of lists, as that is permutation

# intuition 0: There will 3 iterations, one on nums, and other on variations of results
# Intuition 1: iterate over all the elements of the given list
# intuition 2: create empty list of lists called results for storing the lists


def permute_iterative(nums):
    # Start with an empty permutation set
    result = [[]]
    # len(result) = 1
    # len([]) = 0

    for num in nums:
        new_result = []
        for perm in result:
            # Insert the current number into all possible positions
            for i in range(len(perm) + 1):
                new_result.append(perm[:i] + [num] + perm[i:])
                print(new_result)
                # first time [[1]]
        result = new_result

    return result


# Example usage
nums = [1, 2, 3]
output = permute_iterative(nums)
print(output)
