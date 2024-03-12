import collections


class TimeMap:
    def __init__(self):
        self.map = collections.defaultdict(list)  # instantiating defaultDict
        # from collections modules

    def set(self, key: str, value: str, timestamp: int) -> None:
        # there is a key, a value and a timestamp is pulled from outside
        self.map[key].append([value, timestamp])  # self-explanatory

    def get(self, key: str, timestamp: int) -> str:
        matches = self.map[key]  # use the key to get the list of vals, ts

        answer = ""
        # initiate a modified binary search
        left, right = 0, len(matches)-1

        while left <= right:  # loop as long as left is lte right
            mid = left + (right-left) // 2
            if matches[mid][1] <= timestamp:  # ts is to be found
                left = mid + 1
                answer = matches[mid][0]
            else:
                right = mid - 1  # else move the right to left of mid

        return answer
