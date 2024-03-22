class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = {}  # initiate a memo
        max_length = pointer = 0  # initiate 2 pointers at 0

        for index, token in enumerate(s):
            # enumerate the string 
            if token in memo and pointer <= memo[token]:
                # token in memo & pointer is lte 
                pointer = memo[token] + 1
                # incr memo token count and assign to pointer
            else:
                max_length = max(max_length,
                                 index-pointer + 1)
            memo[token] = index  # place token & idx in memo

        return max_length
