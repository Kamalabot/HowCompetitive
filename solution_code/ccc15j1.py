#Special Day ccc15j1

m=int(input(""))
d=int(input(""))

if m == 2 and d == 18:
    print("Special")

elif m == 2 and d < 18:
    print("Before")

elif m == 2 and d > 18:
    print("After")

elif (m > 2 and m <= 12) and (d <= 31):
    print("After")

elif m == 1 and (d <= 31 and d >= 1):
    print("Before")