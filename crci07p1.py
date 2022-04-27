#Platforme crci07p1

import sys

from typing import List

def get_platforms() -> List[int]:

    plats = int(sys.stdin.readline().strip('\n'))

    data = []

    for p in range(plats):

        tmp = []

        forme = sys.stdin.readline().strip('\n').split(' ')

        for x in forme:

            tmp.append(int(x))

        data.append(tmp)

    return data, plats

def pillar_coords(start: int, end: int) -> List[int]:

    ps = start + 0.5
    
    pe = end - 0.5

    length = end - start

    return ps, pe, length

def get_pillar(data: List[List[str]]) ->int:
    
    temp_data = data

    for ind, d in enumerate(data):

        height = d[0]
        start = d[1]
        end = d[2]

        temp_data[ind].extend(pillar_coords(start, end))
    
    return temp_data    

def check_ifbetween(pillar: int, start: int, end: int) -> bool:

    if pillar > start and pillar < end:
        
        return True 

    else:

        return False

given_data = get_pillar(get_platforms()[0]) 

ind = 0

while True:

    chec_data = given_data.pop(ind)

    chec_data.append(chec_data[0])
    
    chec_data.append(chec_data[0])

    for loc_ind, data in enumerate(given_data): 

        if check_ifbetween(chec_data[4], data[1], data[2]):

            if chec_data[6] > abs(chec_data[0] - data[0]): 
                
                chec_data[6] = abs(chec_data[0] - data[0])

        
        if check_ifbetween(chec_data[5], data[1], data[2]):

            if chec_data[7] > abs(chec_data[0] - data[0]):

                chec_data[7] = abs(chec_data[0] - data[0])


    given_data.insert(ind, chec_data)

    ind = ind + 1

    if ind > len(given_data) - 1:

        break

print(given_data)