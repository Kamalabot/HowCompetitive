def edit_distance(word1, word2):
    m, n = len(word1), len(word2)

    # instantiate the dp table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # transforming word1 to empty word
    for idx in range(m + 1):
        dp[idx][0] = idx
    # updating the empty word2 to with word2 chars
    for jdx in range(n + 1):
        dp[0][jdx] = jdx

    # print("after initial update, dp table:\n")
    # for d in dp:
    #     print(d, end="\n")
    # print(".................................")

    for idx in range(1, m + 1):
        for jdx in range(1, n + 1):
            if word1[idx - 1] == word2[jdx - 1]:
                # no cost incurred
                dp[idx][jdx] = dp[idx - 1][jdx - 1]
            else:
                dp[idx][jdx] = min(
                    dp[idx - 1][jdx] + 1, dp[idx][jdx - 1] + 1, dp[idx - 1][jdx - 1] + 1
                )

    # print("after the final update...............\n")
    # for d in dp:
    #     print(d, end="\n")
    # print("........................................")

    return dp[m][n]

// observe the inputs you are giving
print(edit_distance("horse", "ros"))
