#Testing Bovine Genomics

"""Script reads the files and then gets the inputs. 
After that tests it with the functions"""

import os
import sys
from typing import List

from Bovine_Genomics import surmise_position

base_path = os.getcwd() + '\\cownomics_bronze_open17'

#print(base_path)

files_inDir = next(os.walk(base_path))[2]

ins = [fl for fl in files_inDir if 'in' in fl]

outs = [fl for fl in files_inDir if 'out' in fl]

#print(ins)

prob_inputs = [os.path.join(base_path, x) for x in ins]

prob_outs = [os.path.join(base_path, x) for x in outs]

#print(prob_outs)

for x in prob_inputs:

    spotty = []

    plainy = []

    with open(x , 'r') as yb:

        reader = yb.readlines()

    data_points = reader[0].strip('\n').split(' ')

    speci = int(data_points[0])

    gene_len = int(data_points[1])

    for ind, gen in enumerate(reader[1:]):

        if ind < speci:

            spotty.append(gen.strip('\n'))

        else:

            plainy.append(gen.strip('\n'))


    print(surmise_position(spotty,plainy))

for x in prob_outs:

    with open(x, 'r') as x:
        
        print(x.readline())
