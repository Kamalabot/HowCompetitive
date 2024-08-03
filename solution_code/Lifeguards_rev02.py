#Lifeguards

"""Another way to solving the problem..."""

import sys

from typing import List

path = 'c:\\WorkFiles\\WPy64-37120\\notebooks\\HowCompetitive\\2.in'

def get_data(file: str) -> List[int]:

    with open(file, 'r') as f:
        reader = f.readlines()

    slots = int(reader[0].strip('\n'))

    guard_time = []

    for sol in reader[1:]:
        
        temp = []

        for x in sol.split(' '):

            temp.append(int(x))

        guard_time.append(temp)

    return guard_time

def num_covered(intervals, fired):
    """
    intervals is a list of lifeguard intervals;
    each interval is a [start, end] list.
    fired is the index of the lifeguard to fire.
    Return the number of time units covered by all lifeguards
    except the one fired.
    """
    covered = set() #Using set to filter out the 

    for i in range(len(intervals)):

        if i != fired:

            #print(intervals[i])

            interval = intervals[i]

            for j in range(interval[0], interval[1]):

                covered.add(j)
    
    return len(covered)

def get_max(intervals: List[List[int]]):

    #print(intervals)

    max_covered = 0
        
    for intd, fired in enumerate(intervals):
        
        result = num_covered(intervals, intd)
        
        if result > max_covered:
            
            max_covered = result

    return max_covered

def main():

    print(get_max(get_data(path)))

if __name__ == "__main__": main()
