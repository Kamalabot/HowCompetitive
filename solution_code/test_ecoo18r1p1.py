from ecoo18r1p1 import calculate_ride

def case1():
    T = 3
    N = 5
    days = ['E', 'B', 'E', 'B', 'E']
    assert calculate_ride(T, N, days) == 2

def case2():
    T = 2
    N = 4
    days = ['B', 'E', 'E', 'E']
    assert calculate_ride(T, N, days) == 0


def main():
    case1()
    case2()

if __name__ == "__main__":main()