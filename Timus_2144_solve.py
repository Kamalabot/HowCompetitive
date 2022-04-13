#Lena' Boxes Timus 2144 problem

"""This program will tell Lena, whether her action figure boxes can be arranged in the ascending order
The below program is solution from author"""

def read_boxes(n):
    """
    n is the number of boxes to read.
    Read the boxes from the input, and return them as a
    list of boxes; each box is a list of action figure heights.
    """
    boxes = []
    for i in range(n):
        box = input().split()
        box.pop(0)
        for i in range(len(box)):
            box[i] = int(box[i])
        boxes.append(box)
    return boxes


def box_ok(box):
    """
    box is the list of action figure heights in a given box.
    Return True if the heights in box are in nondecreasing order,
    False otherwise.
    """
    for i in range(len(box) - 1):
        if box[i] > box[i + 1]:
            return False
    return True

def all_boxes_ok(boxes):
    """
    boxes is a list of boxes; each box is a list of action figure heights.
    Return True if each box in boxes has its action figures in
    nondecreasing order of height, False otherwise.
    """
    for box in boxes:
        if not box_ok(box):
            return False
    return True

def boxes_endpoints(boxes):
    """
    boxes is a list of boxes; each box is a list of action figure heights.
    Return a list, where each value is a list of two values:
    the heights of the leftmost and rightmost action figures in a box.
    """
    endpoints = []
    for box in boxes:
        endpoints.append([box[0], box[-1]])
    return endpoints

def all_endpoints_ok(endpoints):
    """
    endpoints is a list, where each value is a list of two values:
    the heights of the leftmost and rightmost action figures in a box.
    Requires: endpoints is sorted by action figure heights.
    Return True if the endpoints came from boxes that can be
    put in order, False otherwise.
    """
    maximum = endpoints[0][1]
    for i in range(1, len(endpoints)):
        if endpoints[i][0] < maximum:
            return False
        maximum = endpoints[i][1]   
    return True
# Main Program
# Read input
n = int(input())
boxes = read_boxes(n)
# Check whether all boxes are OK
if not all_boxes_ok(boxes):
    print('NO')
else:
# Obtain a new list of boxes with only left and right heights
    endpoints = boxes_endpoints(boxes)
    # Sort boxes
    endpoints.sort()
    # Determine whether boxes are organized
    if all_endpoints_ok(endpoints):
        print('YES')
    else:
        print('NO')