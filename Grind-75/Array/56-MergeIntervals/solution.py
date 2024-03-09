from typing import List

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sorting intervals can make sure that i.start <= i+1.start
        intervals.sort()  # sort is done based on the 1st elem of the lists
        output_list = [intervals[0]]  # create a output list with 1st pair

        for i in range(1, len(intervals)):
            # No Overlapping Case
            if output_list[-1][1] < intervals[i][0]:
                # if elem[1] of last inter in output list
                # is less than curr_inter[0]
                output_list.append(intervals[i])
            # Else it is a Overlapping Case
            else:
                # change the elem[1] of last inter in output list
                output_list[-1][1] = max(output_list[-1][1], intervals[i][1])

        return output_list
