#coci18c2p1 Pereokret

"""The program answer the question raised by King James on Basket ball"""

"""Q1 : How many total points were scored in the 1st half of the game, that 2 * 12 * 60 = 1440 sec"""
"""Q2 : How many times has a losing team come to winning situation or vice versa in whole game"""

import sys
from typing import List

A_score = int(sys.stdin.readline())

#A_score = 6

A_sec = []
B_sec = []

for i in range(A_score):
    A_sec.append(int(sys.stdin.readline().strip('\n')))

B_score = int(sys.stdin.readline())
#B_score = 7
for i in range(B_score):
    B_sec.append(int(sys.stdin.readline().strip('\n')))

half_time = 2 * 12 * 60 

score_ht = 0
for x in A_sec:
    if x < half_time:
        score_ht += 1

for x in B_sec:
    if x < half_time:
        score_ht += 1

print(score_ht)

#increase the length of one array that is smaller
if len(A_sec) > len(B_sec):
    diff = len(A_sec) - len(B_sec)
    a_more = A_sec[-diff:]
    A_sec = A_sec[:-diff]
    b_more = False
    #print(f"Additional scores of A: {a_more}")
elif len(A_sec) < len(B_sec):
    diff = len(B_sec) - len(A_sec)
    b_more = B_sec[-diff:] 
    B_sec = B_sec[:-diff]
    a_more = False
    #print(f"Additional scores of B: {b_more}")

#print(A_sec)
#print(B_sec)
#idea is to find who scored before the other. The time gap between the scores can be used

score_A = [0]
score_B = [0]

#Who scored first?
tracker = [] 

gls_sec = A_sec + B_sec
gls_sec.sort() #okay this sorting works

#print(gls_sec)

a_i = 0 #index for the scoring list
b_i = 0
g_i = 0

while True:

    if a_i < len(A_sec):                                         #ai = 1 and resolves True
        if gls_sec[g_i] == A_sec[a_i]:                           #gi = 0 and resolves true
            score_A.append(score_A[a_i] + 1)                     #appends so score_a = [0, 1, 2], score_b = [0, 1]
            tracker.append([score_A[-1], score_B[-1]])           #appends so tracker = [[1, 0],[1, 1],[2, 1]]
            a_i = a_i + 1                                        #ai = 6
    
    if b_i < len(B_sec):                                         #bi = 0 resolves true
        if gls_sec[g_i] == B_sec[b_i]:                           #gi = 0 resolve true
            score_B.append(score_B[b_i] + 1)                     #score_b =[0, 1]
            tracker.append([score_A[- 1], score_B[-1]])          #tracker = [[1,0],[1,1]]
            b_i = b_i + 1                                        #bi = 0

    if a_i == len(A_sec) and b_i == len(B_sec):                  #resolves false
        break

    #print(f"tracker_updates {tracker[-1]}")                      #prints tracker updates
    
    g_i = g_i + 1                                                #gi = 2


if a_more:
    for x in a_more:
        score_A.append(score_A[- 1] + 1)
        tracker.append([score_A[- 1], score_B[-1]])
elif b_more:
    for x in b_more:
        score_B.append(score_B[- 1] + 1)
        tracker.append([score_A[- 1], score_B[-1]])

#print(f"Final tracker {tracker}")

lead_change = 0
lead = []
for ind, elem in enumerate(tracker):
    if elem[0] < elem[1]:
        lead.append('B')
    elif elem[0] == elem[1]:
        lead.append(lead[-1])
    else:
        lead.append('A')
#print(lead)

ind = 0
while True:
    if lead[ind] != lead[ind + 1]:
        lead_change += 1
    ind = ind + 1
    #print(f"lead changing {lead_change}")
    if ind >= len(lead) - 1:
        break
print(lead_change)

    
    
