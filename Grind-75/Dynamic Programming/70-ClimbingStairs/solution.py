def memoization(func):
    memo = {}

    def helper(self, x):
        if x not in memo:
            memo[x] = func(self, x)
        return memo[x]
    return helper


class Solution:
    @memoization
    def climbStairs(self, n: int) -> int:
        if n == 1:  # can climb one step
            return 1  # return 1 as only one way 
        elif n == 2:  # can climb 2 step
            return 2  # there are 2 ways, 1 n 2 steps 
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


lsn = Solution()

print(lsn.climbStairs(5))
print(lsn.climbStairs(3))