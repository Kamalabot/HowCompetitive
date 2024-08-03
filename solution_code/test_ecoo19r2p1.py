from ecoo19r2p1 import count_email

def case1():
    mails = 3
    e_list = ['foo@bar.com', 'fO.o+baz123@bAR.com', 'foo@bar..com']
    
    print(count_email(e_list))

def case2():
    mails = 3
    e_list = ['c++@foo.com', 'c...@Foo.com', '.c+c@FOO.COM']
    
    print(count_email(e_list))


def main():
    case1()
    case2()
    
if __name__ == "__main__":main()