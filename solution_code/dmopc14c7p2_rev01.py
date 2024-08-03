#Tides dmopc14c7p2

"""Problem yet to be solved"""

import sys

from typing import List

def gettinput():

    getting_input = []
    reader = int(sys.stdin.readline().strip('\n'))
    measure = sys.stdin.readline().strip('\n')

    for r in measure.split(' '):
        getting_input.append(int(r))
        
    return reader, getting_input

def compare_neig(measure: List[int]) ->List[int]:
    comp_measure = []

    ind = 0 # The index to calculate the difference
    
    while True:
    
        #print(measure[ind])
    
        comp_measure.append(measure[ind + 1] > measure [ind])
    
        ind = ind + 1
    
        if ind >= len(measure) - 1:
    
            break
    
    return comp_measure

def flag_val(diff_comp: List[int]) -> List[int]:
    """Returns the number of values below 0 in a list"""
    
    flag = 5 #assume all are true
    
    ind = 0

    while True:
        #print(flag)
        if flag == 2 and diff_comp[ind] is False:

            flag = -1
            
            return flag
            
            break
        
        elif flag == 1 and diff_comp[ind] is True:
             
            flag = 2

        elif (flag == 0 or flag == 2) and diff_comp[ind] is True:
            
            flag = 2
        
        elif flag == 1 and diff_comp[ind] is False:

            flag = 1

        elif diff_comp[ind] is True:
            
            flag = 0

        elif diff_comp[ind] is False:
            
            flag = 1
        
        ind = ind + 1
        
        if ind >= len(diff_comp):
            
            return flag

            break

def tides(measure):
    """Function checks the gradient of the point
    and decide whether the dataset can be used"""
    get_slope = compare_neig(measure)
    
    get_pattern = flag_val(get_slope)

    if get_pattern == 2:

        return (max(measure) - min(measure))
    
    else:

        return 'unknown'

def main():

    c, measure = gettinput()

    print(tides(measure))

if __name__ == "__main__": main()