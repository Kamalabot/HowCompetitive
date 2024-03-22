from typing import List
# , we can use a simulation approach. We will keep track of the 
# boundaries of the matrix and simulate the spiral traversal

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output_list = []
        top, bottom = 0, len(matrix)-1  # top & bottom elms
        left, right = 0, len(matrix[0])-1  # right & left elms

        while top < bottom and left < right:  # keep looping as long as cond meet
            for column in range(left, right):  # move left to right
                output_list.append(matrix[top][column])
                # append the value to output list
            # traverse top to bottom
            for row in range(top, bottom):
                output_list.append(matrix[row][right])
            # traverse right to left
            for column in range(right, left, -1):
                output_list.append(matrix[bottom][column])
            # traverse bottom to top
            for row in range(bottom, top, -1):
                output_list.append(matrix[row][left])
            # update the constraints
            top, bottom, left, right = top+1, bottom-1, left+1, right-1
        # why do this?
        for row in range(top, bottom+1):
            for column in range(left, right+1):
                output_list.append(matrix[row][column])

        return output_list
