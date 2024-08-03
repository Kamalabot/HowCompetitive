#Occupy parking ccc18j2
N = int(input(""))
Y = input("")
T = input("")
#Y = 'CC.'
#T = '.C.'
def car_park(space: int, past: str, present: str) -> int:
    i = 0
    for car in range(space):
        if past[car] == 'C' and present[car] == 'C':
            i += 1
    return i

print(car_park(N,Y,T))

