class Solution:
    def isPalindrome(self, s: str) -> bool:
        # checks if char is alpha-num and lowercases it
        s = "".join(char for char in s if char.isalnum()).lower()
        return s == s[::-1]
        # checks and returns forward & reverse string equality
