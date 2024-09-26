def combinations_dp(n, k):
    dp = [[] for _ in range(k + 1)]
    dp[0] = [[]]  # Base case: One way to choose 0 items

    for i in range(1, n + 1):
        for j in range(min(k, i), 0, -1):  # Iterate backwards to avoid overwriting
            dp[j] += [
                comb + [i] for comb in dp[j - 1]
            ]  # Add the current number to all (j-1) combinations

    return dp[k]


print("DP based combinations...\n")
# Example usage
print(combinations_dp(4, 2))  # Combinations of 4 choose 2


def permutations_dp(nums):
    dp = [[]]  # Base case: one way to permute 0 elements

    for num in nums:
        new_dp = []
        for perm in dp:
            for i in range(len(perm) + 1):
                new_dp.append(
                    perm[:i] + [num] + perm[i:]
                )  # Insert the number at every position
        dp = new_dp

    return dp


print("DP based Permutations...\n")

# Example usage
print(permutations_dp([1, 2, 3]))  # Permutations of [1, 2, 3]


def subsets_dp(nums):
    dp = [[]]  # Base case: one way to create an empty subset

    for num in nums:
        dp += [
            subset + [num] for subset in dp
        ]  # Add the current number to all existing subsets

    return dp


# Example usage
print("DP based subsets...\n")
print(subsets_dp([1, 2, 3]))  # Subsets of [1, 2, 3]
