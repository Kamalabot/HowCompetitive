#Bakers' Bonus ecoo17r3p1
"""The problem has lend itself for testing, 
so using functional pieces"""

import sys
from typing import List

def getting_data(cases: int)->List[str]:
    case_outlines = []
    dozen=[]

    for _ in range(cases):
        line_data=[]
        outline = sys.stdin.readline().strip('\n')
        data_1 =int(outline.split()[0])
        data_2 =int(outline.split()[1])
        #print(f"outline data collected {_} case")     
    
        #Need to complete the above loop    
        for _ in range(data_2):
            get_data = sys.stdin.readline().strip('\n')
            get_data = get_data.split(' ')
            each_line = []
            for c in get_data:
                each_line.append(int(c))
            line_data.append(each_line)
    
        #print(f"each line data collected for {_}")
    
    #Starting the calculation of sums
        row_sum = []
        for rows in line_data:
            row_sum.append(sum(rows))

        col_sum = [0 for x in range(len(line_data[0]))]
        
        for i in range(len(col_sum)):
            for rows in line_data:
                col_sum[i] = col_sum[i] + rows[i]
        
        #checking the number of bonuses
        bonus = 0
        
        for row in row_sum:
            if row % 13 == 0:
                bonus += row // 13

        for col in col_sum:
            if col % 13 == 0:
                bonus += col // 13
        
        dozen.append(bonus)
    
    return dozen

cas = 10
values = getting_data(cas)
for val in values:
    print(val)
