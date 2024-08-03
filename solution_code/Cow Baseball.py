#2013 December Bronze Cow Baseball

import sys
from turtle import position
from typing import List

cows_ind = [3, 1, 10, 7, 4]

"""Based on the given list find the triples that match the condition
2nd throw is atleast equal to first or atmost 2wice the 1st"""

def triplet(cows_list: List[int]) -> List[int]:
    
    triplet = []

    for x in cows_list:

        for y in cows_list:

            if (y - x) != 0:

                for z in cows_list:

                    if (z -y) >= (y - x) and (z - y) <= 2 * (y - x):

                        temp = [x, y, z]
                        
                        triplet.append(temp)
                        #print(f'abs(x - y) {abs(x - y)}')

                        #print(f'abs(y - z) {abs(y - z)}')
    return(triplet)


def triplet_author(cows_list :List[int]) -> List[int]:
    total = 0

    for position1 in cows_list:

        for position2 in cows_list:

            first_diff = position2 - position1

            if first_diff > 0:

                low = position2 + first_diff
                high = position2 + 2 * first_diff

                for position3 in cows_list:

                    if position3 >= low and position3 <= high:

                        total = total + 1

    return total

def triplet_sort(cows_list :List[int]) -> List[int]:
    total = 0

    cows_list.sort()
    n = len(cows_list)

    for i in range(n):

        for j in range(i + 1, n):

            first_diff = cows_list[j] - cows_list[i]

            low = cows_list[j] + first_diff
            high = cows_list[j] + 2 * first_diff

            left = j + 1

            while left < n and cows_list[left] < low:

                left = left + 1

            right = left

            while right < n and cows_list[right] <= high:

                right = right + 1
                
                
            total = total + right - left

    return total


next_kows = [16, 14, 23, 18, 1, 6, 11]

print(triplet_author(next_kows))

print(triplet(next_kows))

print(triplet_sort(next_kows))
