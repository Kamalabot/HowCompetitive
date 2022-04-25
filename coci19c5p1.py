#counting Rectangles in Emacs coci19c5p1

import sys

from typing import List

def get_rect()->str:

    reader = sys.stdin.readline().strip('\n').split(' ')
    N = int(reader[0])
    M = int(reader[1])
    matr = []
    for i in range(N):
        matr.append(sys.stdin.readline().strip('\n'))
    
    return N, M, matr

def corners(matrix: List[str])->List[int]:
    """Find how many upper left corner * 
    can be located"""

    i = 0

    upper_left = []

    while True:

        for j in range(len(matrix[0])):

            if (j >= 0 and i >= 0) and matrix[i][j] == '*':
                upper_left.append([i, j])

            elif (i > 0 and matrix[i - 1][j] == '.') and (j > 0 and matrix[i][j -1] == ".") and matrix[i][j] == "*":

                upper_left.append([i, j])

        i = i + 1

        if i >= len(matrix):
            
            return len(upper_left)
            
            break

def main():

    N, M, matrix = get_rect()

    #make_n = count_rectangle(N, M, matrix)

    print(matrix)
    counting = corners(matrix)
    
    if len(matrix) == 1:
        print(int(counting / 2))

    else:
        print(counting)

if __name__ == "__main__": main()

