# Pattern: Backtracking
# Introduction:
# Explores all possible solutions and backtracks when a solution path fails.

# Sample Problem:
# Generate all permutations of a given list of numbers.

# Backtracking Algo : Need to review


def permute(nums):
    result = []

    def backtrack(path, options):
        if not options:
            result.append(path)
            return
        for i in range(len(options)):
            backtrack(path + [options[i]], options[:i] + options[i + 1 :])

    backtrack([], nums)
    return result


print(permute([1, 2, 3]))
# Output: [[1,2,3], [1,3,2], [2,1,3], [2
# LeetCode Problems:
# 1. Permutations (LeetCode #46)
# 2. Subsets (LeetCode #78)
# 3. N-Queens (LeetCode #51)
