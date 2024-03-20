class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [1] * n  # create a list of n 1s
        for _ in range(1, m):  # iterate over range of m
            for j in range(1, n):
                # iterate over range of n
                memo[j] = memo[j - 1] + memo[j]
                # The visualisation of above math
                # completely different from
                # what is required to be done manually.
        return memo[-1] if m and n else 0
