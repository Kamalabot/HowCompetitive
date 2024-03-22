class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memo = {}  # create a dict
        for token in s:  # enumerate chars in s
            try:
                memo[token] += 1  # inc count of char by 1
            except KeyError:
                memo[token] = 1  # else assign value of 1 to the key
        
        for token in t:
            try:
                memo[token] -= 1
            except KeyError:
                return False  # if the token is missing, then its False

        return all(count == 0 for count in memo.values())
        # all the values have to be 0 in the memo by the end