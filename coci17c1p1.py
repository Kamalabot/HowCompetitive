#Cezar coci17c1p1

"""The program advices Cezer whether to stop or continue the Blackjack"""

import sys
try:

    drawn = int(sys.stdin.readline().strip('\n'))

except ValueError:

    pass

cards_drawn = []

for _ in range(drawn):
    try:
        cards_drawn.append(sys.stdin.readline().strip('\n')) #the cards drawn till now are stored

    except ValueError:

        pass

ranks = ['2', '3' ,'4' ,'5' ,'6' ,'7', '8', '9', '10', 'Jack', 'King', 'Queen', 'Ace']

vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

rank_vals = {x: y for x,y in zip(ranks, vals)}

available = ranks[:]

for _ in range(3):
    available.extend(ranks) #appending will attach the entire list to the end of the first list.

for card in cards_drawn:
    available.remove(card)

drawn_value = sum([rank_vals[card] for card in cards_drawn])

diff_to_21 = abs(drawn_value - 21)

#print(f'diff {diff_to_21}')

#print(f'drawn value {drawn_value}')

greater_than_diff = [card for card in available if rank_vals[card] > diff_to_21]

#print(greater_than_diff)

less_than_diff = [card for card in available if rank_vals[card] <= diff_to_21]

#print(less_than_diff)

less_than_diff = 52 - drawn - len(greater_than_diff)

#print(f'len greater {len(greater_than_diff)}')
#print(f'len lesser {less_than_diff}')

if len(greater_than_diff) >= less_than_diff:
    print('DOSTA')
else:
    print('VUCI')

