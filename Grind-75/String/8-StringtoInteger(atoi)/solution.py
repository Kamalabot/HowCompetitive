class Solution:
    def myAtoi(self, s: str) -> int:
        answer = index = sign = 0
        MAX_INT, MIN_INT = 2147483647, -2147483648

        s = s.strip()  # ignore leading space
        if len(s) == 0:
            return 0  # if empty s, then return 0

        sign = -1 if s[0] == "-" else 1
        # set the sign to - if abv condition met
        if s[0] in set("+-"):
            # if start char is +/- then move to next char
            index += 1

        while index < len(s) and s[index].isdigit():
            # In ASCII, int(s[index]) = ord(s[index]) - ord("0")
            answer = answer * 10 + int(s[index])
            # create the number by multiplying ans by 10 & add integer
            index += 1  # go to next char

        answer *= sign  # include the sign
        # Make sure the returned value is in [-2^31, 2^31)
        answer = min(MAX_INT, max(answer, MIN_INT))
        return answer
