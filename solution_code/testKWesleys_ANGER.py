#Testing script for the Wesley's ANGER
from wac3p3 import calculate_points


def case1():
    moves = 'URLDR'
    
    trial = [['LRURU', 500], ['LRUR', 750], ['URU', 1000]]
    
    print(calculate_points(moves, trial))


def case2():
    moves = 'URLDRDRRURRLDRURUURLLLUURDDDU'
    
    trial = [['LRURU', 500], ['LRU', 750], ['URU', 1000], ['U',50], ['D',5]]
    
    print(calculate_points(moves, trial))

def case3():
    moves = 'U'
    
    trial = [['LRURU', 500], ['LRU', 750], ['URU', 1000], ['U',5], ['D',57]]
    
    print(calculate_points(moves, trial))

def case4():
    
    moves = 'URLDRDRRURRLDRURUURLLLUURDDDUURLDRDRRURRLDRURUURLLLUURDDDU'
    
    trial = [['LRURU', 500], ['LRU', 750], ['URU', 1000], ['UUUD',5], ['LLRD',57]]
    
    print(calculate_points(moves, trial))

def main():
    case1()
    case2()
    case3()
    case4()

if __name__ == "__main__": main()