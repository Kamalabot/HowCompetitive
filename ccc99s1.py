#Card game between 2 people ccc99s1

"""The pack of shuffled card are dealt between 2 players
and the player with the highest score wins"""

high = ['jack', 'queen', 'king', 'ace']

import sys
from typing import List 

cards = []

for i in range(52):
    cards.append(sys.stdin.readline().strip('\n').strip(' '))

point_a = 0
point_b = 0

def ace(ind: int, cards: List[str]) -> int:
    checks = []
    if ind > 48:
        return False
    for card in cards:
        checks.append(card in high)
    if not any(checks):
        return 4
def king(ind: int, cards: List[str]) -> int:
    checks = []
    if ind > 49:
        return False
    for card in cards:
        checks.append(card in high)
    if not any(checks):
        return 3

def queen(ind: int, cards: List[str]) -> int:
    checks = []
    if ind > 50:
        return False
    for card in cards:
        checks.append(card in high) 
    if not any(checks):
        return 2

def jack(ind: int, cards: str) -> int:
    checks = []
    if ind > 51:
        return False
    for card in cards:
        checks.append(card in high) 
    if not any(checks):
        return 1

overall_a = []
overall_b = []
ind = 0
while True:
    #print(f"index is {ind}")

    if cards[ind] == 'ace' and ind % 2 != 0:
        #print("Ace B entry")
        #print(cards[ind + 1 : ind + 5]) #test
        
        point_b = ace(ind, cards[ind + 1 : ind + 5])
        if point_b:
            print(f"Player B scores {point_b} point(s).")
            overall_b.append(point_b)
        ind = ind + 4
    
    elif cards[ind] == 'ace' and ind % 2 == 0:
        #print("Ace A entry")
        #print(cards[ind + 1 : ind + 5]) #test
        
        point_a = ace(ind, cards[ind + 1 : ind + 5])
        if point_a:
            print(f"Player A scores {point_a} point(s).")
            overall_a.append(point_a)
        ind = ind + 4

    elif cards[ind] == 'king' and ind % 2 != 0:
        #print("King B entry")
        #print(cards[ind + 1 : ind + 4]) #test
        
        point_b = king(ind, cards[ind + 1 : ind + 4])
        if point_b:
            print(f"Player B scores {point_b} point(s).")
            overall_b.append(point_b)
        ind = ind + 3
    
    elif cards[ind] == 'king' and ind % 2 == 0:
        #print("King A entry")
        #print(cards[ind + 1 : ind + 4]) #test
        
        point_a = king(ind, cards[ind + 1 : ind + 4])
        if point_a:
            print(f"Player A scores {point_a} point(s).")
            overall_a.append(point_a)
        ind = ind + 3
    
    elif cards[ind] == 'queen' and ind % 2 != 0:
        #print("queen B entry")
        #print(cards[ind + 1 : ind + 3]) #test

        point_b = queen(ind, cards[ind + 1 : ind + 3])
        if point_b:
            print(f"Player B scores {point_b} point(s).")
            overall_b.append(point_b)
        ind = ind + 2
    
    elif cards[ind] == 'queen' and ind % 2 == 0:
        #print("queen A entry")
        #print(cards[ind + 1 : ind + 3]) #test

        point_a = queen(ind, cards[ind + 1 : ind + 3])
        if point_a:
            print(f"Player A scores {point_a} point(s).")
            overall_a.append(point_a)
        ind = ind + 2
    
    elif cards[ind] == 'jack' and ind % 2 != 0:
        #print("Jack B entry")
        #print(cards[ind + 1]) #test

        point_b = jack(ind, cards[ind + 1 : ind + 2])
        
        if point_b:
            print(f"Player B scores {point_b} point(s).")
            overall_b.append(point_b)
        ind = ind + 1
    
    elif cards[ind] == 'jack' and ind % 2 == 0:
        #print("Jack A entry")
        #print(cards[ind + 1]) #test
        
        point_a = jack(ind, cards[ind + 1 : ind + 2])
        if point_a:
            print(f"Player A scores {point_a} point(s).")
            overall_a.append(point_a)
        ind = ind + 1
    
    ind = ind + 1
    
    if ind > 51:
        break
#print(overall_a)
print(f"Player A: {sum(overall_a)} point(s).")
#print(overall_b)
print(f"Player B: {sum(overall_b)} point(s).")
