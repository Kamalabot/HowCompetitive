# A palindromic subsequence is a sequence of characters that reads the same
# forwards and backwards. In this case, we need to find the longest
# subsequence that is a palindrome within the string "bbbab".

# bbbb is longest subseq, and it need not be contiguous


def longestPalinSubseq(s):
    n = len(s)
    # dp table where dp[i][j]
    # represents the longestPalinSubseq

    dp = [[0] * n for _ in range(n)]

    # single chars are palins of length 1
    for i in range(n):
        dp[i][i] = 1  # fills diagonal

    # fill the table in bottom up manner
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # if i and j chars are same
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


s = "bbbab"
print(longestPalinSubseq(s))
