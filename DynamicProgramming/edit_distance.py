# Edit or Levenshtein Distance


def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    # dp table, where dp[i][j] reps the edit distance

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # initialize the table
    for i in range(m + 1):
        dp[i][0] = i
    # distance of transforming word1[:i] to empty word
    for j in range(n + 1):
        dp[0][j] = j
    # distance of transforming empty word to
    # word2[:j]
    # fill the table
    for idx in range(1, m + 1):
        for jdx in range(1, n + 1):
            if word1[idx - 1] == word2[jdx - 1]:
                # no cost incurred
                dp[idx][jdx] = dp[idx - 1][jdx - 1]
            else:
                dp[idx][jdx] = min(
                    dp[idx - 1][jdx] + 1, dp[idx][jdx - 1] + 1, dp[idx - 1][jdx - 1] + 1
                )
                # insertion, deletion, replacement
    print(dp)
    return dp[m][n]


# answer returned is wrong, need to
# debug the code

word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))
