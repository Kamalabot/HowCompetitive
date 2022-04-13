#Lena' Boxes Timus 2144 problem

"This program will tell Lena, whether her action figure boxes can be arranged in the ascending order"

from typing import List
import sys

no_of_boxes = int(sys.stdin.readline().strip('\n'))

box_data = []

for _ in range(no_of_boxes):
    box_temp = sys.stdin.readline().strip('\n').split(' ')
    
    num_figs = int(box_temp[0]) #Find how many action figures
 
    box_contains = [] #open a new container
 
    for x in box_temp[1:]: #iterate over the remaning box temp data

        box_contains.append(int(x)) #append the figures heights to box contains list
    
    box_data.append(box_contains) #append box contains list to box_data

#print(box_data)

def check_location(box: List[int]) -> bool:
    """
    Function checks if any box that has action figures not sorted in ascending
    """
    min_box = min(box)
    max_box = max(box)
        
    if len(box) == 1:
        return box

    elif box.index(min_box) == 0 and box.index(max_box) == len(box) -1:
        return [box[0],box[-1]]
    
    elif box[0] == box[-1]:
        return box[0], box[-1]
    
    else:
        return False

assert check_location([10]) == [10]
assert check_location([5, 6, 10]) == [5, 10]
assert check_location([6, 10, 5]) == False,  'Extremes are in the middle'

def check_two(box1: List[int], box2: List[int]) -> bool:
    """
    Function intends to check if min fig height of a box is 
    smaller than max fig in other box
    """
    if box2[0] < max(box1):
        return False

    elif box1[-1] > min(box2):
        return False

    else:
        return True

assert check_two([1, 3], [2, 3]) == False
assert check_two([1, 3], [4, 3]) == True
assert check_two([1, 5], [2, 3]) == False

def box_ok(box):
    """
    box is the list of action figure heights in a given box.
    Return True if the heights in box are in nondecreasing order,
    False otherwise.
    """
    for i in range(len(box) - 1):
        print(i)
        if box[i] > box[i + 1]:
            return False
    return True

check_minmax = [check_location(box) for box in box_data]

print(check_minmax)

sorted_minmax = sorted(check_minmax, key = lambda element : element[0])

print(sorted_minmax)

last_elem = [last[-1] for last in sorted_minmax]
print(last_elem)

"""
iter = 0
chk = []
while True:
    if last_elem[iter + 1] > last_elem[iter]:
        chk.append(True)
    else:
        chk.append(False)
    iter = iter + 1
    if iter >= len(last_elem) -1:
        break 
print(chk)
"""
if box_ok(last_elem):
    print("YES")

else:
    print("NO")  


#Some of the pseudocode follows
#Check if all the boxes have min and max values of their action figures, at their left and right extremes

    #no: then print "no"

#Get the min and max of the each box

#Create new_arrange = []

#While True:

#Find the box with action fig with least height, 

# put it in the front

# 

# What I have to do for finding the figures with least action figure size?
