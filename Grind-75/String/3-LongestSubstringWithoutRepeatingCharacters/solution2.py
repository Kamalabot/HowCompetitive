class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = set()  # memo is different type, its set
        window_start = window_end = max_length = 0
        # window can begin closed at 0

        while window_start < len(s) and window_end < len(s):
            token = s[window_end]  # start with char of window end
            if token in memo:  # if token in memo
                memo.remove(s[window_start])  # remove the token using 
                window_start += 1
            else:
                window_end += 1
                max_length = max(max_length, window_end-window_start)
                memo.add(token)

        return max_length
