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

#The objective is the maximize the time range that is covered.
#There are ranges that overlap, so need function merge and get their overall range
#We 
def merge_slots(slot1: List[int], slot2: List[int]) -> List[int]:
    """Returns merged slot with over all range"""
    
    if slot2[0] > slot1[0] and slot2[-1] < slot1[-1]:
        return slot1
    
    elif slot2[0] < slot1[0] and slot2[-1] > slot1[-1]:
        return slot2

    elif slot1[-1] > slot2[0] and slot2[-1] > slot1[-1]:
        return [[slot1[0],slot2[-1]]]

    elif slot2[-1] > slot1[0] and slot1[-1] > slot2[-1]:
        return [[slot2[0], slot1[-1]]]

    else:
        return slot1, slot2

def max_time(guard_time: List[List[int]]) -> int:

    """This function takes in the guard times and returns the maximum time
    that can be still covered."""

    time_slot = []

    indt = 0

    duration = []

    while True:

        time_slot.extend(merge_slots(guard_time[indt], guard_time[indt + 1]))

        indt = indt + 1

        if indt > len(guard_time) - 2:

            break
    #print(time_slot)

    for times in time_slot:

        x = times[-1] - times[0]

        duration.append(x)

    #Remove the minimum time slot or search for the longer slots??

    min_dur = min(duration)
    
    #based on the min slot, the guard to be fired is found.

    max_dur = max(duration)
    
    return min_dur + max_dur

def main():

    guards = get_data(path)

    #print(guards)

    print(max_time(guards))


if __name__ == "__main__": main()
