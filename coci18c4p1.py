#The Elder coci18c4p1
import sys

owner = sys.stdin.readline().strip('\n')
fights = int(sys.stdin.readline())
winner = []
loser = []
no_of_owner = 1 # starting owner

owners = [] #keep track of the owners
owners.append(owner)

#getting data and filling them in the array
for duel in range(fights):
    temp = sys.stdin.readline().split(' ')
    winner.append(temp[0].strip('\n'))
    loser.append(temp[1].strip('\n'))

#Which duel did the owner lose the match? 
for ind in range(fights):
    #print(ind)
    if loser[ind] == owners[-1]:
        #print('entered if')
        owners.append(winner[ind])
        #no_of_owner += 1

#Same owners can take possession again. So double counting needs to be removed.
conv_set = list(set(owners))

#print(conv_set)
#print(owners)
#Which duel did the winner loss
print(owners[-1])
print(len(conv_set))