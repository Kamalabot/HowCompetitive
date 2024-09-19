# Problem: Partition Equal Subset Sum (LeetCode 416)
# We use dynamic programming to check if we can
# partition the array into two subsets
# with equal sum.
from typing import List

# intu1: total_sum has to be even to find equal subset
# intu2: no need to find the actual sum


def can_partition(nums: List[int]) -> bool:
    total_sum = sum(nums)
    # if the total_sum is odd
    # then cannot partition
    if total_sum % 2 != 0:
        return False
    # choose the target by doing
    # integer division and discarding
    # reminder. Anyway, there wont
    # be reminder rite!!!
    target = total_sum // 2
    # creating list with False elements
    dp = [False] * (target + 1)
    # make the first true
    dp[0] = True
    # enumerate the elms in the list
    for num in nums:
        # enumerate in the range of tgt
        # to num - 1 in reverse
        for i in range(target, num - 1, -1):
            # check if i or i - num have
            # True value
            dp[i] = dp[i] or dp[i - num]

    return dp[target]
    # return value of dp @ target


print(can_partition([1, 5, 11, 5]))
