#Tides dmopc14c7p2

import sys

from typing import List

def gettinput():

    getting_input = []
    reader = int(sys.stdin.readline().strip('\n'))
    measure = sys.stdin.readline().strip('\n')

    for r in measure.split(' '):
        getting_input.append(int(r))
        
    return reader, getting_input

def tides(c, measure):
    """Locates the index of minimum and checks if 
    the measurement is continuosly increasing"""
    
    hi_val = max(measure)

    hi_ind = measure.index(max(measure))
    
    low_val = min(measure[:hi_ind + 1])
    
    low_ind = measure.index(low_val)
    
    ind = low_ind
    
    while True:
        print(measure[ind])
        if measure[ind] > measure [ind + 1]:
            print('1st if')
            """If lower index is having bigger value than the higher index
            and ind is lower than hi_ind"""
            if ind < hi_ind:
                return 'unknown'

        if measure[hi_ind] < measure [ind + 1]:
            print('2nd if')
            """This means, the index has crossed the max value of the list"""
            return hi_val - low_val 

        if hi_val == low_val:
            print('3rd if')
            """If lower index is having bigger value than the higher index
            and ind is lower than hi_ind"""
            return 'unknown'


        ind = ind + 1 #move the index to next

        if ind >= c - 1:
            return hi_val - low_val 
            break
        
def main():

    c, measure = gettinput()

    print(tides(c, measure))

if __name__ == "__main__": main()