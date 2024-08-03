#Solving the Pandemic Problem ccc20j2

import sys
from xml.etree.ElementTree import QName

P = int(sys.stdin.readline())
N = int(sys.stdin.readline())
R = int(sys.stdin.readline())

#When total people having the disease is more than P

total = N #Keep track of the total infected
#day 1 infection 2 * 1 = 2 + 2 + 2 + 2 + 2
day = 0
while True:
    if day == 0:
        infected = R * N
    else:
        infected = infected * R
    
    total += infected
    day += 1
    #print(f"infected_nextday {infected}")
    #print(f"day {day}")
    
    if total > P:
        break

print(day)
