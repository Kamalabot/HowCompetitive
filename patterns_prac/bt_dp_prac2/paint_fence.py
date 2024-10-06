### Problem Statement: Paint Fence

# You are given `n` posts to paint and `k` different colors.
# You need to paint all the posts such that no more than
# two adjacent posts have the same color. Find the total number
# of ways to paint the fence.

# ### Example to Understand the Problem:

# **Input**:
# `n = 3` (number of posts), `k = 2` (number of colors)

# **Explanation**:
# - Possible ways to paint:
#   - Post 1: Color A, Post 2: Color B, Post 3: Color A (`ABA`)
#   - Post 1: Color A, Post 2: Color B, Post 3: Color B (`ABB`)
#   - Post 1: Color B, Post 2: Color A, Post 3: Color B (`BAB`)
#   - Post 1: Color B, Post 2: Color A, Post 3: Color A (`BAA`)

# **Output**: `4`

# The goal is to calculate the number of valid ways to paint
# the fence posts while ensuring no more than two consecutive
# posts are painted the same color.


def numWays(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k

    # # Base cases
    # same, diff = 0, k
    # total = same + diff

    # # Fill the dp array
    # for i in range(2, n + 1):
    #     same = diff
    #     diff = total * (k - 1)
    #     total = same + diff

    # return total
    dp = [0] * (n + 1)
    # base case
    dp[1] = k
    # filling the dp
    for idx in range(2, n + 1):
        dp[idx] = (k - 1) * (dp[idx - 1] + dp[idx - 2])

    return dp[n]


# Example check
n = 3
k = 2
print(numWays(n, k))  # Output: 6
