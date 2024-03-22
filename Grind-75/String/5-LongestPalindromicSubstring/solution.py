# challenge is to build a longest palindrome and return it
# not just check if there is a longest palindrome


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = s[0]  # start by considering start char as palindrome
        memo = [[False] * len(s) for _ in range(len(s))]
        # create memo of nested list with False equal to length of string 
        # and it propagates to range of length

        for i in range(len(s)):
            memo[i][i] = True
            # make the diagonal as True

        # starting to build the palindrome
        for i in range(len(s)):
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    if i == j+1 or memo[i-1][j+1]:
                        memo[i][j] = True
                        if i-j+1 > len(longest_palindrome):
                            longest_palindrome = s[j:i+1]

        return longest_palindrome
