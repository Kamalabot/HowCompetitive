from typing import List
list_int = List[List[int]]


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> list_int:       
        output_list = []  # create store
        for counter, interval in enumerate(intervals):
            # enumerate each intervals
            if interval[1] < newInterval[0]:
                # elem 1 of inter is less than elem 0 of ninter
                output_list.append(interval)
                # ninter is bigger than inter, so append inter to store
            elif interval[0] > newInterval[1]:
                # elif elem 0 of inter is
                # greater than ninter elme 1
                # append ninter as that is smaller
                output_list.append(newInterval)
                # once ninter inserted, then append rest
                # of intervals to output and return
                return output_list + intervals[counter:]
            else:
                # if scenario is inters [[6, 10]] and ninter is [0, 10]
                new_start_elem= min(interval[0], newInterval[0])
                # start elem is min of both start elems
                new_end_elem = max(interval[1], newInterval[1])
                # end is max of both end elems 
                newInterval = [new_start_elem, new_end_elem]
                # merged interval is ninter
        output_list.append(newInterval)

        return output_list
