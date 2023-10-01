#Tracking the ball coci06c5p1
from typing import List
inp = input("")
inp = inp.upper()
start = [1,0,0]

def A(L: List[int])->List[int]:
    temp = L[1]
    L[1] = L[0]
    L[0] = temp 
    return L

def B(L: List[int])->List[int]:
    temp = L[1]
    L[1] = L[2]
    L[2] = temp 
    return L

def C(L: List[int])->List[int]:
    temp = L[0]
    L[0] = L[2]
    L[2] = temp 
    return L

for F in inp:
    if F == 'A':
        start = A(start)
    elif F =='B':
        start = B(start)
    else:
        start= C(start)

print(start.index(1)+1)
