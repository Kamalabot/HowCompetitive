# Longest increasing subset


def lengthLIS(nums):
    # create the dp table
    dp = [1] * len(nums)
    # start filling the dp table
    # the problem is divided into
    # subsets
    for idx in range(1, len(nums)):
        # create inner loop to check
        # all elements till idx
        for jdx in range(idx):
            # elm till idx is bigger than prev elm
            if nums[idx] > nums[jdx]:
                # increment the dp[jdx]
                dp[idx] = max(dp[idx], dp[jdx] + 1)
    return max(dp)


print(lengthLIS([10, 9, 2, 5, 3, 7, 101, 18]))
