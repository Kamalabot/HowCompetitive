#ecoo19r1p1 Free T-shirts

import sys

from typing import List

def gettinput():

    getting_input = []
    contest = []
    reader = sys.stdin.readline().strip('\n')

    for r in reader.split(' '):
        getting_input.append(int(r))
    shirts = getting_input[0]

    events = getting_input[1]
    
    days = getting_input[2]
    
    cont_days = sys.stdin.readline().strip('\n')
    
    for x in cont_days.split(' '):
        contest.append(int(x))
        
    return shirts, events, days, contest

def count_shirts(shirts, days, contest) -> int:

    launder = []
    
    event = 0 #There can be more than one event, so better create a variable
    
    s = shirts # this is Ian's wardrobe

    t_s = s #This variable will keep track whether Ian does laundry or not

    i = 1 # The days of the Ian's life

    # Following are the conditions that can trigger laundry or not

    while True:
        
        if t_s > 0:

            event = contest.count(i)

            s = s + event   

            t_s = t_s - 1 + event #current t_s cannot be renewed fully
        
        elif t_s == 0:
            
            event = contest.count(i)
            
            s = s + event 
            
            t_s = s 

            t_s = t_s - 1
            
            launder.append(i)

        i = i + 1
        
        if i > days:
        
            break
    
    return launder
        

def main():

    for datasets in range(2):

        shirts, events, days, contest = gettinput()

        print(len(count_shirts(shirts, days, contest)))

if __name__ == '__main__': main()

