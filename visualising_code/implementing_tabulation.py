# Script contains the implementation of DP 
# problems using the Tabulation method

def fib(n):
    table = [0 for _ in range(n + 1)]
    print(table)
    table[1] = 1

    for i in range(n):
        print("i: ", i)
        table[i + 1] += table[i] 
        if i + 1 < n:
            table[i + 2] += table[i] 

    return table


print(fib(13))
# print(fib(1))
# print(fib(2))
# print(fib(5))
# print(fib(11))
print(fib(51))