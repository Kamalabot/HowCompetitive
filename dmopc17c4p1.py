#the ribbon painting contest dmopc17c4p1

"""Need to find what length of the ribbon is still purple and what length is blue"""
"""Below code back fires because the way it checks the number that is covered by the paints"""
import sys

from typing import List

lst = input().strip('\n').split()

length = int(lst[0])

strokes = int(lst[1])

range_covered = set()

for i in range(strokes):

    paint = input().strip('\n').split(' ')

    for i in range(int(paint[0]), int(paint[1])):
        #print(i)
        range_covered.add(i)

range_covered = list(range_covered)    

min_start = min(range_covered)

max_end = length - max(range_covered)

print(range_covered)

fpaint = 0

for painted in range(length):

    if painted not in range_covered:

        print(painted)

        fpaint = fpaint + 1

fpaint = fpaint + max_end + min_start

print(length - fpaint, fpaint)
