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
    print("................\n")
    for d in dp:
        print(d, end="\n")
    print(".................\n")
    return dp[0][n - 1]


nums = [3, 1, 5, 8]

print(maxCoins(nums))
