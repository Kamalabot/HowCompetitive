#Data plan coci16c1p1
import sys
all_data = []

data = int(sys.stdin.readline()) #data plan between 1 and 100

month = int(sys.stdin.readline()) #Number of month Pero had plan

for x in range(month):
    all_data.append(int(sys.stdin.readline()))
            #will gather each month usage from input

unused = 0

for consume in all_data:
    #current month usage
    temp = unused + data - consume # temp == 5
    unused = 0
    unused = temp + unused # data == 15
    #print(unused)

print(unused + data)
#print(data)    