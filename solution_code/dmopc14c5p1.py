#We will calculate the volume of right angle cone, dmopc14c5p1

"""The program takes 2 inputs, height and radius and gives out the volume of the cone"""

import math

PI = 3.141592653589793

r = float(input("r :"))
h = float(input("h :"))

def volume(x: float, y: float) -> float:
    return (PI * x ** 2 * y)/3

print(volume(r,h))