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
    # distance of transforming empty word to word2[:j]
    # fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
    print(dp)
    return dp[m][n]


# answer returned is wrong, need to
# debug the code

word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))
