# Given an array of integers nums and an integer sum, determine if there is
# a subset of nums with a sum equal to sum.


def subset_sum(nums, sum):
    dp = [False] * (sum + 1)
    dp[0] = True
    for num in nums:
        for i in range(sum, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[sum]


# Example Input:
nums = [3, 34, 4, 12, 5, 2]
sum = 9

# Example Output:
print(subset_sum(nums, sum))  # Output: True
