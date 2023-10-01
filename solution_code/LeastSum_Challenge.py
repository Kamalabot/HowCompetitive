#Given an array A of integers, and integer K, return the 
#maximum S such that there exists i < j with A[i] + A[j] =S
# and S < K. If no such i , j exist satifying this eqn return -1

#getting the array

import sys

arr = []

get_input = sys.stdin.readline().strip('\n')

for elem in get_input.split(','):
    arr.append(int(elem)) #converted elem to int and appended

integer = int(sys.stdin.readline())

summ = []
coordinate = []
max_sum = 0

for i in range(len(arr)):
    temp = arr[i] #34
    for j in arr[i + 1:]:
        summ.append(temp + j)
        coordinate.append([i,j])

belowK = [x for x in summ if x <= integer]
#index_K = summ.index(max(belowK))

if belowK == []:
    print(-1)

elif max(belowK):
    print(max(belowK))

