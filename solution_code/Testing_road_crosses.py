#Testing road Croses

"""Script reads the files and then gets the inputs. 
After that tests it with the functions"""

import os
import sys
from typing import List

from WhyDidtheCowCrosstheRoad import calculate_crossing, check_crossing

base_path = os.getcwd() + '\\crossroad_bronze_feb17'

#print(base_path)

files_inDir = next(os.walk(base_path))[2]

ins = [fl for fl in files_inDir if 'in' in fl]

outs = [fl for fl in files_inDir if 'out' in fl]

#print(ins)

prob_inputs = [os.path.join(base_path, x) for x in ins]

prob_outs = [os.path.join(base_path, x) for x in outs]

#print(prob_outs)

for x in prob_inputs:

    with open(x , 'r') as re:
        
        reader = re.readlines()

    data_points = int(reader[0].strip('\n'))

    id_location = []

    ids = []

    locat = []

    for x in range(1, data_points + 1):

        id = reader[x].strip('\n').split(' ')

        ids.append(int(id[0]))

        locat.append(int(id[1]))


    print(calculate_crossing(ids,locat))

for x in prob_outs:

    with open(x, 'r') as x:
        
        print(x.readline())
