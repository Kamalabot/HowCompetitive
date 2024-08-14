# Pattern: Overlapping Intervals
# Introduction: The Overlapping Intervals pattern is used to merge or handle overlapping intervals in an array.

# Sample Problem: Merge all overlapping intervals.
# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]

# Example Implementation:
def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# LeetCode Problems:
# - Merge Intervals (LeetCode #56)
# - Insert Interval (LeetCode #57)
# - Non-Overlapping Intervals (LeetCode #435)
