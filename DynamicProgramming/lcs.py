# Problem: Longest Common Subsequence
# (LeetCode 1143)
# We use dynamic programming to find
# the longest subsequence common between two strings.


def lcs(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # building the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                # if char matches take the idx
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # else take the max of the adj cells
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


print(lcs("abcde", "ace"))
