# Longest increasing subset


def lengthLIS(nums):
    dp = [1] * len(nums)

    # iterating over array to build dp array
    for i in range(1, len(nums)):
        for j in range(i):
            # curr elm is bigger than prev elm
            if nums[i] > nums[j]:
                # take the max of the element
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


print(lengthLIS([10, 9, 2, 5, 3, 7, 101, 18]))
