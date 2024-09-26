### Problem Statement: Decode Ways

# Given a string `s` containing only digits,
# determine the total number of ways to decode it, where:
# - '1' to '9' map to 'A' to 'I'.
# - '10' to '26' map to 'J' to 'Z'.

# The string cannot contain leading zeros,
# and each digit or pair of digits must
# form a valid character.


def num_decodings(s):
    if not s:
        return 0

    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1 if s[0] != "0" else 0

    for idx in range(2, len(s) + 1):
        if s[idx - 1] != "0":
            dp[idx] += dp[idx - 1]
        if 10 <= int(s[idx - 2 : idx]) <= 26:
            dp[idx] += dp[idx - 2]

    return dp[len(s)]
