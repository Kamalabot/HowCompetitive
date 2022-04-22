from dmopc14c7p2_rev01 import tides, compare_neig, flag_val

def case1():
    c = 5
    measure = [2, 1, 3, 5, 10]
    
    compare = compare_neig(measure)
    
    #print(compare)

    #print(flag_val(compare))

    print(tides(measure))

def case2():
    c = 5
    measure = [1, 2, 5, 4, 9]

    #compare = compare_neig(measure)
    
    #print(compare)

    #print(flag_val(compare))

    print(tides(measure))

def case3():
    c = 9
    measure = [1, 2, 7, 9, 11, 15, 19, 25, 23]
    
   #compare = compare_neig(measure)
    
    #print(compare)

    #print(flag_val(compare))

    print(tides(measure))

def case4():
    c = 5
    measure = [9, 9, 9, 9, 9]
    
    #compare = compare_neig(measure)
    
    #print(compare)

    #print(flag_val(compare))

    print(tides(measure))

def case5():
    c = 5
    
    measure = [10, 100, 1, 20, 150, 1000, 9000, 9100]
    
    #compare = compare_neig(measure)
    
    #print(compare)

    #print(flag_val(compare))

    print(tides(measure))

def case6():
    c = 5
    measure = [2, 10, 3, 5, 1]
    #lowVal_lt = 2 and lowValrt = 1
    
    #compare = compare_neig(measure)

    #print(compare)

    #print(flag_val(compare))
    
    print(tides(measure))

def main():
    case1()
    case2()
    case3()
    case4()
    case5()
    case6()
if __name__ == "__main__":main()