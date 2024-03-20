from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # get the combination between m + n - 2
        # and n - 1
        return comb(m + n - 2, n-1)
