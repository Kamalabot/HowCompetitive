### Problem Statement: Decode Ways

# Given a string `s` containing only digits,
# determine the total number of ways to decode it, where:
# - '1' to '9' map to 'A' to 'I'.
# - '10' to '26' map to 'J' to 'Z'.

# The string cannot contain leading zeros,
# and each digit or pair of digits must
# form a valid character.

# ### Example to Understand the Problem:

# **Input**: `s = "226"`

# **Explanation**:
# 1. Possible decodings:
#    - "2" -> 'B', "2" -> 'B', "6" -> 'F' (`"BBF"`)
#    - "2" -> 'B', "26" -> 'Z' (`"BZ"`)
#    - "22" -> 'V', "6" -> 'F' (`"VF"`)
#
# 2. Total decodings: 3.

# **Output**: `3`

# The goal is to find the number of ways to decode the string using the given mappings.
def numDecodings(s):
    # Base case: If the string is empty, there's one way to decode it (doing nothing)
    if not s:
        return 0

    # DP array where dp[i] represents the number of ways to decode s[:i]
    dp = [0] * (len(s) + 1)
    dp[0] = 1  # Base case: There's one way to decode an empty string
    dp[1] = 1 if s[0] != "0" else 0  # Single-character decoding

    # Fill the dp array
    for i in range(2, len(s) + 1):
        # Check if the current character can be
        # decoded as a single digit
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]
        # Check if the last two
        # characters can be decoded as a valid two-digit number
        if 10 <= int(s[i - 2 : i]) <= 26:
            dp[i] += dp[i - 2]

    return dp[len(s)]


# Example check
s = "226"
print(numDecodings(s))
