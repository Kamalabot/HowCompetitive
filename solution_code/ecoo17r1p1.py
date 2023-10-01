#Brunch and Munch ecoo17r1p1

import sys
import math

trips = 10
trip_data = []

for _ in range(10):
    instance = []

    for _ in range(3):
        instance.append(sys.stdin.readline().strip("\n"))

    trip_data.append(instance)

#converting the data types into appropriate values

from typing import List

def proportions(attendees: str) ->List[float]:
    temp = [] 

    for att in attendees.split(' '):
        temp.append(float(att))
    
    return temp
    
assert(proportions('0.1 0.2 0.5')) == [0.1,0.2,0.5]

for trip in trip_data:
    trip[0] = int(trip[0])
    trip[1] = proportions(trip[1])
    trip[2] = int(trip[2])
#data is converted for calculations

def contribution(propotion: List[float], attend: int) ->int:
    brunch = [12, 10, 7, 5]
    total = 0
    
    for i, stud in enumerate(propotion):
        total = total + math.ceil(stud * attend) * brunch[i]
        #print(f"brunch - {math.ceil(stud * attend) * brunch[i]}")
    
    return total

assert(contribution([0.1,0.1,0.1,0.1],1000)) == 3400

year_end = []

for trip in trip_data:
    contri = contribution(trip[1], trip[2]) * 0.5
    #print(f"conribution {contri}")
    if contri >= trip[0]:
        year_end.append('NO')
    else:
        year_end.append('YES')

for yer in year_end:
    print(yer)