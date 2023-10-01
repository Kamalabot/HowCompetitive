#WhyDidtheCowCrosstheRoad

from collections import defaultdict

from typing import List


with open('1.in', 'r') as re:
    reader = re.readlines()

data_points = int(reader[0].strip('\n'))

id_location = []

ids = []

locat = []

for x in range(1, data_points + 1):

    id = reader[x].strip('\n').split(' ')

    ids.append(int(id[0]))

    locat.append(int(id[1]))



def check_crossing(crossed: List[int]):

    temp = len(crossed)

    ind = 0

    crosses = 0

    while ind < temp - 1:

        if crossed[ind] != crossed[ind + 1]:

            crosses += 1
        
        ind = ind + 1

    return crosses

def calculate_crossing(ids: List[int], locat:List[int]):
    
    crossing = defaultdict(list)

    for id, locat in zip(ids, locat):
        
        temp = []

        crossing[id].append(locat)

    #print(crossing)

    total_crosses = 0 

    for id, locations in crossing.items():

        total_crosses = total_crosses + check_crossing(locations)

    return total_crosses

def main():

    calculate_crossing(ids= ids, locat= locat)

if __name__ == "__main__": main()