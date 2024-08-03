from ccc00s2 import calculate_babbling

def case1():
    streams = 3
    ind_stream = [10, 20, 30]
    stream_data = [99, 1, 50, 88, 3, 88, 2]
    assert calculate_babbling(streams, ind_stream, stream_data) == [5, 55]

def case2():
    streams = 3
    ind_stream = [10, 20, 30]
    stream_data = [99, 2, 50, 88, 3, 88, 1]
    assert calculate_babbling(streams, ind_stream, stream_data) == [20, 40]

def case3():
    streams = 5
    ind_stream = [10, 20, 30, 57, 65]
    stream_data = [99, 2, 50, 88, 3, 88, 2, 99, 4, 57, 99, 5, 22, 88, 5]
    print(calculate_babbling(streams, ind_stream, stream_data))

def case4():
    streams = 10
    ind_stream = [10, 20, 30, 57, 65, 75, 22, 55, 67, 64]
    stream_data = [99, 2, 50, 88, 3, 88, 2, 99, 4, 57, 99, 5, 22, 88, 5, 88, 2, 88,7, 88, 9]
    print(calculate_babbling(streams, ind_stream, stream_data))

def case5():
    streams = 1
    ind_stream = [200]
    stream_data = [99, 1, 50, 99, 1, 40, 99, 3, 10, 88, 2, 88, 2, 88, 1]
    print(calculate_babbling(streams, ind_stream, stream_data))

def case6():
    streams = 14
    ind_stream = [53, 914, 827, 302, 631, 785, 230, 11, 567, 350, 307, 339, 929, 589]
    stream_data = [99, 1, 4, 88, 1, 99, 1, 53, 99, 3, 18, 99, 1, 92, 99, 2, 3, 88, 5]
    print(calculate_babbling(streams, ind_stream, stream_data))

def main():
    #case1()
    #case2()
    case3()
    case4()
    case5()
    case6()

if __name__ == "__main__":main()