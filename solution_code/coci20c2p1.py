#getting the networth graphed coci20c2p1

import sys

from typing import List

def get_days()->str:

    days = int(sys.stdin.readline().strip('\n'))
    symbol = (sys.stdin.readline().strip('\n'))
    
    return days, symbol


def lets_draw(days, symbol) -> None:

    ind = 0
    day = 0
    mark = 0
    drawin = []

    #Need to find how many dots need to create first
    plus = symbol.count('+')
    minus = symbol.count('-')
    equals = symbol.count('=')

    dots = plus + minus - 1

    for i in range(day):
        drawin.append('.' * dots)

    while True:

        if symbol[ind] == '+':

            temp = '.' * days
            temp[day] = '/'
            day = day + 1

        elif symbol[ind] == '-':

            temp = '.' * days
            temp[day] = '\\'
            day = day + 1

        elif symbol[ind] == '=':

            temp = '.' * days
            
            temp[day] = '_'
            day = day + 0
    


