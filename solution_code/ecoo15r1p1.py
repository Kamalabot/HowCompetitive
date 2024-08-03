#When you eat your smarties ecoo15r1p1

"""The program outputs the time it takes to eat the 
smarties provided by each of 10 cases"""

import sys
from collections import Counter

cases = 2

for _ in range(cases):
    get_smarties = []

    while True:
        get_smarties.append(sys.stdin.readline().strip('\n').strip(' '))
        if get_smarties[-1] == 'end of box':
            break
    time = 0
    count = Counter(get_smarties[:-1])
    print(count)
    for cols in count:
        if cols != 'red':
            hands = count[cols] // 7
            if count[cols] % 7 > 0:
                hands += 1
            time = time + hands * 13
        else:
            time = count['red'] * 16 + time

    print(time)
