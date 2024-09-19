def wordBreak(s, wordDict):
    word_set = set(wordDict)
    # DP array where dp[i] means s[:i]
    # can be segmented into words in
    # wordDict
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Empty string can be segmented

    # Fill the dp array
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]


s = "leetcode"
worddict = ["leet", "code"]
print(wordBreak(s, worddict))
