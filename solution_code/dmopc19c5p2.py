#Charlies conquest dmopc19c5p2

import sys

from typing import List

def get_game():

    commands = sys.stdin.readline().strip('\n').split(' ')

    entry = int(commands[0])

    health = int(commands[1])

    plays_char = []

    plays_bot = []

    for _ in range(entry):
        
        temp = sys.stdin.readline().strip('\n').split(' ')

        plays_char.append([temp[0],int(temp[1])])

    for _ in range(entry):
    
        temp = sys.stdin.readline().strip('\n').split(' ')

        plays_bot.append([temp[0],int(temp[1])]) 

    return plays_char, plays_bot, health

def play_game(health: int, charlie: List[int, int], bot: List[int, int]):

    idx = 0

    charlie_health = health

    bot_health = health

    while True:

        if charlie[idx][0] == 'A' and bot[idx][0] == 'A':

            charlie_health = charlie_health - bot[idx][1]

            bot_health = bot_health - charlie[idx][1]

        if charlie[idx][0] == 'D' and bot[idx][0] == 'D':

            charlie_health = charlie_health - charlie[idx][1]

            bot_health = bot_health - bot[idx][1]

        if charlie[idx][0] == 'A' and bot[idx][0] == 'D':

            charlie_health = charlie_health - charlie[idx][1]

            bot_health = bot_health - bot[idx][1]


def main():

    print(get_game())

if __name__ == "__main__": main()

