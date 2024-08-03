#USACO December Silver Contest problem Cities and States 

"""The curious pairs of states and cities has to be identified
and the count returned"""

#Getting the data from the file
import os
from typing import List
from collections import Counter

def get_tree(base_path: str) -> List[str]:

    for d, di, files in os.walk(base_path):
    
        file_need = files

    file_names = [f for f in file_need if f[-2:] == 'in']
    out_names = [f for f in file_need if f[-3:] == 'out']

    inputs = [os.path.join(base_path, x) for x in file_names]
    outputs = [os.path.join(base_path, x) for x in out_names]

    return inputs, outputs

def file_read(file_path: str) -> List[str]:

    with open(file_path, 'r') as cities:
        reader = cities.readlines()

    num = reader[0].strip('\n')
    pairs = []

    for lin in reader[1:]:
        pairs.append(lin.strip('\n').split(' '))
    return num , pairs

def get_pairs(num: int, pairs: List[str])-> int:
    
    states = [st for _, st in pairs]
    cities = [ci for ci,_ in pairs]
    #Find any of the states initials has common characters
    cities_st = [ci[:2] for ci in cities]
    pair_name = []
    for ind, s in enumerate(states):
        if cities_st[ind] != states[ind]:
            pair_name.append(states[ind]+cities_st[ind])

    return pair_name

def reverse_match(state1, state2):
    temp = state1[:2]
    state1 = state1[2:]+temp
    if state1 == state2:
        return True
    else:
        return False

assert (reverse_match('FLMI', 'MIFL')) is True
assert (reverse_match('FLMI', 'MIFo')) is False

def counting(pair_common) -> int:
    count = 0
    #print(pair_common)
    for combo in pair_common:
        other_combo = combo[2:] + combo[:2]
        if other_combo in pair_common:
            count = count + pair_common[combo] * pair_common[other_combo]
    return count

def get_result(outs: List[str]) ->str:
    with open(outs, 'r') as result:
        reader = result.readlines()
        print(reader[0].strip('\n'))

def main():

    base_path = 'C:\\WorkFiles\\WPy64-37120\\notebooks\\HowCompetitive\\citystate_silver_dec16\\'

    inputs, outputs = get_tree(base_path)

    for file in inputs:

        num, pairs = file_read(file)

        pair_name = get_pairs(num, pairs)

        pair_common = Counter(pair_name)
        
        print(counting(pair_common) // 2)

if __name__ == "__main__": main()
