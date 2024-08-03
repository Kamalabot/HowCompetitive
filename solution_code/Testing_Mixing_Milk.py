#Testing Mixing_Milk

from Mixing_Milk import pour, after_pours

"""Script reads the files and then gets the inputs. 
After that tests it with the functions"""

import os
import sys
from typing import List

from Lifeguards_rev02 import num_covered, get_data, get_max

base_path = os.getcwd() + '\\mixmilk_bronze_dec18'

#print(base_path)

files_inDir = next(os.walk(base_path))[2]

ins = [fl for fl in files_inDir if 'in' in fl]

outs = [fl for fl in files_inDir if 'out' in fl]

#print(ins)

prob_inputs = [os.path.join(base_path, x) for x in ins]

prob_outs = [os.path.join(base_path, x) for x in outs]

#print(prob_outs)

for x in prob_inputs:

    capacities = []
    quantities = []

    with open(x, 'r') as milk:

        reader = milk.readlines()

    for bucket in reader:
        temp = bucket.split(' ')
        capacities.append(int(temp[0]))
        quantities.append(int(temp[1]))


    print(after_pours(capacities, quantities))

for x in prob_outs:

    with open(x, 'r') as x:
        print(x.readlines(), end= ' ')
