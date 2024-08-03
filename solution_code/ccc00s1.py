#Martha's Getting Rich ccc00s1

import sys

data = []
for _ in range(4):
    data.append(int(sys.stdin.readline()))

quarters = data[0]
ma = data[1]
mb = data[2]
mc = data[3]
turn = 0

def deli_quarter(machine: str)->int:
    if machine == 'ma':
        return 30
    elif machine == 'mb':
        return 60
    elif machine == 'mc':
        return 9

#assert deli_quarter('ma') + 10 == 40
#assert deli_quarter('mc') + 10 == 19

while True:

    if quarters > 0:
        ma = ma + 1
        quarters -= 1
        turn += 1
    else:
        break

    if quarters > 0:
        mb = mb + 1
        quarters -= 1
        turn += 1
    else:
        break

    if quarters > 0:
        mc = mc + 1
        quarters -= 1            
        turn += 1

    else:
        break    

    if ma % 35 == 0:
        quarters = quarters + deli_quarter('ma')
        #print('entering ma')
    if mb % 100 == 0:
        quarters = quarters + deli_quarter('mb')
        #print('entering mb')
    if mc % 10 == 0:
        quarters = quarters + deli_quarter('mc')
        #print('entering mc')
        
        #print(f"qtr : {quarters}")

print(f"Martha plays {turn} times before going broke")