#Testing script for the Wesley's ANGER
from ecoo18r1p2 import calculate_congestion


def case1():
    ids = [4, 3, 2, 1] 
    
    rounds = [[2, 3, 4], [3, 4, 2, 4], [7, 2, 3, 3, 4, 5, 2, 6], [5, 3, 2, 5, 1, 4]]
    
    calculate_congestion(ids, rounds)

def case2():
    ids = [1, 2, 3] 
    
    rounds = [[6, 4, 5, 2, 6, 3, 2], [3, 2, 3, 4], [4, 2, 3, 2, 4]]
    
    calculate_congestion(ids, rounds)

def case3():

    ids = [1] 
    
    rounds = [[6, 4, 5, 2, 6, 3, 2]]
    
    calculate_congestion(ids, rounds)

def case4():

    ids = [1, 2, 3] 
    
    rounds = [[1, 1], [1, 5], [1, 5]]
    
    calculate_congestion(ids, rounds)

def main():
    case1()
    case2()
    case3()
    case4()

if __name__ == "__main__": main()