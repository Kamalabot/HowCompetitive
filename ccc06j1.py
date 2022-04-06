#Lets count calories ccc06j1

A1 = int(input(""))
A2 = int(input(""))
A3 = int(input(""))
A4 = int(input(""))

them = 0

if A1 == 1:
    them  = them + 461
elif A1 == 2:
    them = them + 431
elif A1 == 3:
    them = them + 420
else:
    them = them

if A2 == 1:
    them  = them + 100
elif A2 == 2:
    them = them + 57
elif A2 == 3:
    them = them + 70
else:
    them = them

if A3 == 1:
    them  = them + 130
elif A3 == 2:
    them = them + 160
elif A3 == 3:
    them = them + 118
else:
    them = them

if A4 == 1:
    them  = them + 167
elif A4 == 2:
    them = them + 266
elif A4 == 3:
    them = them + 75
else:
    them = them

print(f"Your total Calorie count is {them}.")