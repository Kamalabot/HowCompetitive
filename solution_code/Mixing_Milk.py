#2018 december bronze Mixing Milk
"""3 tests failed in the judge, so the logic is correct. Fine tuning of the code is necessary"""
import sys

#Reading contents of the file

capacities = []
quantities = []


def pour(cap_str, cap_end, qty_str, qty_end):

    total_qty = qty_str + qty_end

    if total_qty > cap_end:

        qty_end = cap_end

        qty_str = total_qty - cap_end

    elif total_qty <= cap_end:

        qty_end = total_qty

        qty_str = 0

    return qty_str, qty_end
"""
with open('mixmilk.in', 'r') as milk:

    reader = milk.readlines()

for bucket in reader:
    temp = bucket.split(' ')
    capacities.append(int(temp[0]))
    quantities.append(int(temp[1]))
"""

from typing import List

#initiating the pour sequence
def after_pours(capacities: List[int], quantity: List[int]) ->List[int]:
    pouring = 0
    quantities = quantity

    while pouring <= 100:

        quantities[0], quantities[1] = pour(capacities[0], capacities[1], quantities[0], quantities[1])
        quantities[1], quantities[2] = pour(capacities[1], capacities[2], quantities[1], quantities[2])
        quantities[2], quantities[0] = pour(capacities[2], capacities[0], quantities[2], quantities[0])

        pouring += 3
    #the last pour cannot be done in the while loop, above so making seperate
    quantities[0], quantities[1] = pour(capacities[0], capacities[1], quantities[0], quantities[1])

    return quantities
"""
with open('mixmilk.out', 'w') as writer:
    for qty in quantities:
        writer.write(str(qty)+'\n')
"""

def main():
    pass

if __name__ == "__main__": main()