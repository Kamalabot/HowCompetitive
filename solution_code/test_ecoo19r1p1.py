from ecoo19r1p1 import count_shirts

def case1():
    shirts = 1
    events = 1
    days = 10
    contest = [10]
    print(count_shirts(shirts, days, contest))

def case2():
    shirts = 1
    events = 3
    days = 10
    contest = [2, 9, 5]
    print(count_shirts(shirts, days, contest))

def main():
    case1()
    case2()

if __name__ == "__main__":main()