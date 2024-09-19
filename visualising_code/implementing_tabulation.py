# Script contains the implementation of DP
# problems using the Tabulation method


def fib(n):
    table = [0 for _ in range(n + 1)]
    # create empty list
    print(table)
    table[1] = 1
    # assign 1 to 2nd element

    for i in range(n):
        # enumerate over range of n
        print("i: ", i)
        table[i + 1] += table[i]
        # add the val of next idx with curr idx val & store
        if i + 1 < n:
            # check if i + 1 is not crossing the range
            table[i + 2] += table[i]
            # add val next to next idx with curr val & store

    return table


print(fib(13))
# print(fib(1))
# print(fib(2))
# print(fib(5))
# print(fib(11))
print(fib(51))

