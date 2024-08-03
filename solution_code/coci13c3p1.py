#Rijeci Mirko's Machine coci13c3p1
from typing import List
import sys

press = int(sys.stdin.readline())

"""
#start = 'A'

def char_change(in_data: List[str], press: int)->str:
    intab = ["A","B"]
    outtab = ["B","BA"]
    for _ in range(press):
        in_data = in_data.translate({ord(x):y for (x,  y) in zip(intab, outtab)})
    
    return in_data.count('A'), in_data.count('B')

def fibo(num):
    a = 0
    b = 1
    if num == 0:
        return 0
    else:
        for x in range(num):
            #print(a)
            half = a + b
            a = b 
            b = half
        return half

#print(f"{fibo(press - 1)} {fibo(press)}")
"""
#for i in range(10):
    #print(fibo_rec(i))

def fibo_rec(n):
    if n in {0, 1}:
        return n
    return fibo_rec(n-1) + fibo_rec(n - 2)

def fibonacci_of(n):
    # Validate the value of n
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    # Handle the base cases
    if n in {0, 1}:
        return n

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number

print(f"{fibonacci_of(press-1)} {fibonacci_of(press)}")