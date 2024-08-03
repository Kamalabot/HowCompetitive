# 2014 January Bronze Contest Ski Course

"""The heights of the hills are provided, and we 
search for the cost incurred at various ranges 
starting from 0 - 17 to 100 - 117"""

import sys
from typing import List

hills = [23,40,16,2]

ranges = [(x, y) for x, y in zip(range(0,101), range(17, 118))]


def cost_range(hills: List[int], interval: List[int]):

    """One has to bring the hills within the range, 
    so need to calculate the cost for the same."""

    #Each hill check the cost with respect to ends of the ranges and 
    #select the side of the range that takes range side with least cost.
    #If the hill is with in the range, then nothing to be done.
        
    cost = []
    
    for hill in hills:
        if hill < interval[0]:
        #print(c_1) 
            cost.append((interval[0] - hill) ** 2)

        elif hill > interval[1]:

            cost.append((interval[1] - hill) ** 2)
    
    return sum(cost)

#Which range will suit this set of hills?

#print(ranges)

#print(cost_range(hills, [0,17]))

cost_for_range = [cost_range(hills, x) for x in ranges]

min_cost = min(cost_for_range)

print(cost_for_range)

min_cost_index = cost_for_range.index(min_cost)

range_costing_minimum = ranges[min_cost_index]

print(f"range_costing_minimum is {range_costing_minimum}")