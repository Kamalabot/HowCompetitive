class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        # uses two pointers 
        while left < right:
            # checks char on rt/lt idx is alphanum
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            # if above conditions fail, (they have to for checking chars)
            else:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1

        return True


text = 'nona'
sol = Solution()
print(sol.isPalindrome(text))
