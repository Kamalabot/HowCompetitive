from cco99p2 import common_words, gettinput

def case1():
    e_list = ['foo@bar.com', 'fO.o+baz123@bAR.com', 'foo@bar..com']
    
    print(common_words(e_list, 2))

def case2():
    mails = 3
    e_list = ['c++@foo.com', 'c...@Foo.com', '.c+c@FOO.COM']
    
    print(common_words(e_list, 2))


def main():
    gettinput()
    case1()
    case2()
    
if __name__ == "__main__":main()