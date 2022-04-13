#Take a number ecoo13r1p1

"""Program output the number of students who where late the day.
number of students in the queue and finally the next number in 
the machine"""

import sys

student_late = serve = 0

def find_int(data: str) ->int:
    try:
        return int(data)
    except ValueError:
        return False

assert find_int(12) == 12, 'it cannot be a number'
assert find_int('F') == False, 'it cannot be a number'

while True:
    data = sys.stdin.readline().strip('\n')
    if find_int(data):
        machine_num = find_int(data)
        #print(machine_num)
    elif data == 'TAKE':
        student_late += 1
        machine_num = machine_num + 1
        if machine_num > 999:
            machine_num = 1
        #print(student_late)
        #print(f"Machine NUm {machine_num}")
    elif data == 'SERVE':
        serve += 1
        #print(serve)
    elif data == 'CLOSE':
        print(f"{student_late} {student_late - serve} {machine_num}")
        student_late = serve = 0
    elif data == "EOF":
        break