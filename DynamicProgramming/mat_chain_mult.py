### Problem Statement: Burst Balloons

# You are given `n` balloons, each balloon is painted with
# a number on it represented by an array `nums`.
# You are asked to burst all the balloons. If you
# burst the `i-th` balloon, you will get
# `nums[i-1] * nums[i] * nums[i+1]` coins. If
# `i-1` or `i+1` goes out of bounds of the array,
# consider it as 1. Return the maximum coins you
# can collect by bursting the balloons wisely.

### Example to Understand Burst Balloons Problem:

# **Input**: `nums = [3, 1, 5, 8]`

# **Explanation**:
# 1. Add virtual balloons with value `1` at both ends: `[1, 3, 1, 5, 8, 1]`.
# 2. Burst balloons strategically:
#    - Burst `1` (index 1): Coins = `1 * 3 * 1 = 3`. Remaining: `[1, 1, 5, 8, 1]`.
#    - Burst `5` (index 3): Coins = `1 * 5 * 8 = 40`. Remaining: `[1, 1, 8, 1]`.
#    - Burst `1` (index 2): Coins = `1 * 1 * 8 = 8`. Remaining: `[1, 8, 1]`.
#    - Burst `8` (index 1): Coins = `1 * 8 * 1 = 8`. Remaining: `[1, 1]`.
# 3. Total Coins: `3 + 40 + 8 + 8 = 59`.

# **Output**: `59`

# The goal is to maximize the coins collected by choosing the best order to burst the balloons.


def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for k in range(left + 1, right):
                dp[left][right] = max(
                    dp[left][right],
                    nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right],
                )
    return dp[0][n - 1]


nums = [3, 1, 5, 8]
print(maxCoins(nums))
