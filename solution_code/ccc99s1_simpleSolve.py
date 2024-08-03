NUM_CARDS = 52
def no_high(lst):
    """
    lst is a list of strings representing cards.
    Return True if there are no high cards in lst, False otherwise.
    """
    if 'jack' in lst:
        return False
    if 'queen' in lst:
        return False
    if 'king' in lst:
        return False
    if 'ace' in lst:
        return False
    
    return True
deck = []

for i in range(NUM_CARDS):
    deck.append(input())

score_a = 0
score_b = 0
player = 'A'

for i in range(NUM_CARDS):
    card = deck[i]
    points = 0
    remaining = NUM_CARDS - i - 1
    if card == 'jack' and remaining >= 1 and no_high(deck[i+1:i+2]):
        points = 1
    elif card == 'queen' and remaining >= 2 and no_high(deck[i+1:i+3]):
        points = 2
    elif card == 'king' and remaining >= 3 and no_high(deck[i+1:i+4]):
        points = 3
    elif card == 'ace' and remaining >= 4 and no_high(deck[i+1:i+5]):
        points = 4
    
    if points > 0:
        print(f'Player {player} scores {points} point(s).')

    if player == 'A':
        score_a = score_a + points
        player = 'B'
    else:
        score_b = score_b + points
        player = 'A'

print(f'Player A: {score_a} point(s).')
print(f'Player B: {score_b} point(s).')