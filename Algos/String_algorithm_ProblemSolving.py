""" Pattern Matching (KMP Algorithm):

Problem: Given a text string and a pattern string, find all occurrences of the pattern in the text efficiently.

 """
def KMPSearch(text, pattern):
    def computeLPSArray(pattern):
        length = 0
        i = 1
        lps = [0] * len(pattern)
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    m, n = len(pattern), len(text)
    lps = computeLPSArray(pattern)
    i, j = 0, 0
    occurrences = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                occurrences.append(i - j)
                j = lps[j - 1]
        else:
            if j:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences

text = "ABABDABACDABABCABAB"
pattern = "ABAB"
print("Pattern found at positions:", KMPSearch(text, pattern))

""" Regular Expression Matching:

Problem: Determine if a given text string matches a regular expression pattern.
 """

import re

text = "Hello, my email is example@email.com and my phone number is 123-456-7890."
pattern_email = r'\b[\w.-]+@[\w.-]+\.\w+\b'
pattern_phone = r'\d{3}-\d{3}-\d{4}'

email_matches = re.findall(pattern_email, text)
phone_matches = re.findall(pattern_phone, text)

print("Email addresses:", email_matches)
print("Phone numbers:", phone_matches)

""" String Edit Distance (Levenshtein Distance):

Problem: Calculate the minimum number of single-character edits (insertion, deletion, or substitution) required to transform one string into another.

 """
def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[m][n]

str1 = "kitten"
str2 = "sitting"
print("Levenshtein Distance:", levenshtein_distance(str1, str2))