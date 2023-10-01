#Lifeguards

"""Wrong way of solving the problem..."""

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

def max_time(guard_time: List[List[int]]) -> int:

    """This function takes in the guard times and returns the maximum time
    that can be still covered."""

    time_slot = []

    for times in guard_time:

        x = times[-1] - times[0]

        time_slot.append(x)

    #Remove the minimum time slot or search for the longer slots??

    min_guard = min(time_slot)
    
    #based on the min slot, the guard to be fired is found.
    guard = guard_time[time_slot.index(min_guard)]

    time_slot.pop(time_slot.index(min_guard))
    
    return sum(time_slot)

def main():

    guards = get_data(path)

    print(max_time(guards))


if __name__ == "__main__": main()
