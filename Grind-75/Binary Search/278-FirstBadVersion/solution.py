# The isBadVersion API is defined as followed
def isBadVersion(version: int) -> bool:
    print('called')
    ...


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # here the left is 1 (lb) and right is n (ub)
        while left < right:  # loop as long as left is below right
            mid = (left+right) // 2  # get mid value
            if isBadVersion(mid):  # mid point is checked, >> this is the key <<
                right = mid  # move the right to mid if version is bad
                # reduces versions towards left
            else:
                left = mid + 1  # move left above mid
                print(left)
                # reduces versions towards right

        return left


l = Solution()
# you should minimize the calls to the API isBadVersion
print(l.firstBadVersion(10))
# print(l.firstBadVersion(100))