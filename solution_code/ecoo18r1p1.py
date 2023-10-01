#willow's wild ride ecoo18r1p1

import sys

def gettinput():

    getting_input = []
    box = []
    reader = sys.stdin.readline().strip('\n')

    for r in reader.split(' '):
        getting_input.append(int(r))
    bored = getting_input[0]
    days = getting_input[1]
    for x in range(days):
        box.append(sys.stdin.readline().strip('\n'))
        
    return bored, days, box

from typing import List

def calculate_ride(bored :int, days: int, box :List[str]) -> int:

    day_delay = 0

    for day in box:    
        if day_delay > 0 and day == 'B':
                day_delay += bored - 1
        
        elif day == 'B':
            day_delay += bored

        else:
            if day_delay > 0:
                day_delay -= 1

    if day_delay > 0:
        delay = day_delay - 1
        return delay
    else:
        return day_delay

def main():
    for _ in range(2):
        bored, days, box = gettinput()
        print(calculate_ride(bored, days, box))

if __name__ == "__main__": main()