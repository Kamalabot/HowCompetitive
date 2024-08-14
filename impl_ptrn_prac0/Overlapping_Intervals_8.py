# Pattern: Overlapping Intervals
# Introduction: The Overlapping Intervals pattern is used to merge or handle overlapping intervals in an array.

# Sample Problem: Merge all overlapping intervals.
# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]

# Example Implementation:
def mergeIntervals(intervals):
    # sort the 1st element of the interval
    intervals.sort(key=lambda x: x[0])
    # create a empty list
    merged = []
    # enumerate the intervals
    for interval in intervals:
        # check if the interval is in the merged
        # check the 2nd elem merged last element
        if not merged or merged[-1][1] < interval[0]:
            # append the interval
            merged.append(interval)
        else:
            # else merge the interval
            # by changing last interval of the merge list
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(mergeIntervals(intervals))

# LeetCode Problems:
# - Merge Intervals (LeetCode #56)
# - Insert Interval (LeetCode #57)
# - Non-Overlapping Intervals (LeetCode #435)
