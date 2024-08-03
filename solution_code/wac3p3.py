#Wesley learns DDR wac3p3

import sys

from typing import List

from collections import Counter

def gettinput():

    moves = sys.stdin.readline().strip('\n')

    comb = int(sys.stdin.readline().strip('\n'))
    
    combos = []
    
    for r in range(comb):
    
        reader = sys.stdin.readline().strip('\n').split(' ')

        combos.append([reader[0], int(reader[1])])

    return moves, combos


def check_same_length(combos: List[str]) -> bool:

    #Checking whether the combos are of same length, if not then take the top most combo

    chec = 0

    if len(combos) == 1:

        return 1

    same_length = 1 #means same length

    while True:

        if len(combos[chec][0]) != len(combos[chec + 1][0]):

            same_length = 0

        chec = chec + 1

        if chec >= len(combos) - 1:

            return same_length

def calculate_points(wesley: str, combos: List[str]) -> int:

    """This calculates the points based on the moves and returns
    the total."""
    moves = wesley
    total = 0
    snip = 0

    #get the number of moves irrespective of the combos and add to total

    total = total + len(moves)

    #Search the list of combos and select the longest among them. 
    sorted_combos = sorted(combos, key = lambda x: len(x[0]), reverse= True)

    #Take the longest combo and match with 1st string equal len.

    if check_same_length(sorted_combos) == 0:
        #print('They are all different lengths')

        for loc, points in sorted_combos:
            #print(moves)
            #print(loc)
            if loc in moves:

                total  = total + points
                #print(total)
                ind = moves.find(loc)

                snip = ind + len(loc)

            if snip < len(moves):

                moves = moves[snip:]

        return total

    else:
        #print('They are all same lengths')
        a = len(sorted_combos[0][0]) #In this case all elements are same length 
        
        l = 0
        
        while True:
            #print('entering while')
            for loc, points in sorted_combos:
                #print(moves[l:a])
                if loc == moves[l:a]:

                    total = total + points

                    l = l + len(loc) - 1 # The moves have to checked for the each combo, and the corresponding combo awarded
                    #If the combo matches, then the l index is moved forward by len of matched combo - 1
                    
            l = l + 1 # Irrespective of whether the combo matches inside the if statement, outside it will increment by 1

            if l >= len(moves):

                return total
            
def main():

    moves, combos = gettinput()

    print(calculate_points(moves, combos))

if __name__ == "__main__": main()