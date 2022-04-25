#ecoo18r1p2 Rue's Rings

import sys

from typing import List

from collections import Counter

def getinput():

    routes = int(sys.stdin.readline().strip('\n'))
    
    ids = []

    rounds = []

    for r in range(routes):
        rings = []

        reader = sys.stdin.readline().strip('\n').split(' ')

        ids.append(int(reader[0]))
        
        for x in reader[1:]:

            rings.append(int(x))

        rounds.append(rings)

    return ids, rounds

def calculate_congestion(ids, rounds):
    min_round = {}
    
    for i, values in zip(ids,rounds):
        
        min_round[i] = min(values[1:])
    
    temp = list(min_round.items())
    
    m = min([x for _, x in temp])

    fin_list = [i for i, a in temp if a == m]

    print(f"{m} ",end='')
    print('{',end='')
    print(','.join([str(x) for x in fin_list]),end='')
    print('}')


def main():

    for i in range(10):

        ids, rounds = getinput()

        #print(ids, rounds)

        calculate_congestion(ids, rounds)

if __name__ == "__main__": main()