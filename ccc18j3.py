#Are we there yet ccc18j3

import sys
from typing import List

def get_distances() ->List[int]:

    reader = sys.stdin.readline().strip('\n').split(' ')

    distance = []

    for i in reader:
        distance.append(int(i))

    return distance

def print_toprow(distance: List[int]):

    idx = 0

    local_dist = distance 

    local_dist.insert(0, 0)

    sum = []

    temp = 0

    while True:

        temp = temp + local_dist[idx]

        sum.append(temp)

        idx = idx + 1

        if idx >= len(local_dist):

            break

    return sum

def get_addrows(toprow: List[int])-> List[List[int]]:

    top_r = toprow

    jdex = 0

    top_list = []

    while True:

        temp = []

        for idex in range(len(top_r)):

            temp.append(str(abs(top_r[idex] - toprow[jdex])))

        top_list.append(temp)

        jdex = jdex + 1

        if jdex >= len(toprow):

            break
    
    return top_list

distance = get_distances()

top_row = print_toprow(distance)

top_list = get_addrows(top_row)

for x in top_list:
    print(' '.join(x))        