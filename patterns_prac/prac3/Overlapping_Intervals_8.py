# Pattern: Overlapping Intervals
# Introduction: The Overlapping Intervals pattern is used to merge or handle overlapping intervals in an array.

# Sample Problem: Merge all overlapping intervals.
# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]

# intuition 1: the intervals have to first sorted with their starting coordinate
# intuition 2: create a new list to place the updated intervals
# intuition 3: intervals are enumerated and 2nd coordinate in last element of merged
# interval is checked with 1st coordinate of current interval, and merge is performed
# intuition 4: merge is performed by taking the max of last interval in merged list,
# curr interval 2nd coordinate

# Example Implementation:
def mergeIntervals(intervals):
    sort_intl = sorted(intervals, key=lambda x: x[0])
    merged = [sort_intl[0]]
    for intl in range(1, len(sort_intl)):
        if merged[-1][1] < sort_intl[intl][0]:
            merged.append(sort_intl[intl])
        else:
            merged[-1][1] = max(merged[-1][1], sort_intl[intl][1])
    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(mergeIntervals(intervals))

# LeetCode Problems:
# - Merge Intervals (LeetCode #56)
# - Insert Interval (LeetCode #57)
# - Non-Overlapping Intervals (LeetCode #435)
