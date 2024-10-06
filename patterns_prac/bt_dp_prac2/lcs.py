# longest common subsequence between two
# strings


def lcs(text1, text2):
    m, n = len(text1), len(text2)
    # creates a 2d array DP
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # there seems to be no base case
    for idx in range(1, m + 1):
        for jdx in range(1, n + 1):
            # check if chars match between texts
            if text1[idx - 1] == text2[jdx - 1]:
                dp[idx][jdx] = dp[idx - 1][jdx - 1] + 1
            else:
                # take the max of adj cells
                dp[idx][jdx] = max(dp[idx - 1][jdx], dp[idx][jdx - 1])
    return dp[m][n]


print(lcs("abcde", "ace"))
