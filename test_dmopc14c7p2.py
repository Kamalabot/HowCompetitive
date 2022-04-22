from dmopc14c7p2 import tides

def case1():
    c = 5
    measure = [2, 1, 3, 5, 10]
    print(tides(c, measure))

def case2():
    c = 5
    measure = [1, 2, 5, 4, 9]
    print(tides(c, measure))

def case3():
    c = 9
    measure = [1, 2, 7, 9, 11, 15, 19, 25, 23]
    print(tides(c, measure))

def case4():
    c = 5
    measure = [9, 9, 9, 9, 9]
    print(tides(c, measure))

def case5():
    c = 5
    measure = [10, 100, 1, 20, 150, 1000, 9000, 9100]
    print(tides(c, measure))

def case6():
    c = 5
    measure = [2, 10, 3, 5, 1]
    print(tides(c, measure))
    

def main():
    #case1()
    #case2()
    #case3()
    case6()
    #case5()
if __name__ == "__main__":main()