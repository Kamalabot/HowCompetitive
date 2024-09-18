# prob statement:
# Find the factorial of the given number using recursion

# intuition 1: base case is n <= 2 where return value is n
# intuition 2: higher numbers are reduced recursively to to n < 2
# intuition 3: each reduction is multiplied with each other and n


def fact(n):
    if n <= 2:
        return n
    return fact(n - 1) * n


def factm(n, memo=dict()):
    if n in memo:
        return memo[n]
    if n <= 2:
        return n
    memo[n] = factm(n - 1, memo) * n
    return memo[n]


print("1 factorial:", fact(1))
print("2 factorial:", fact(2))
print("3 factorial:", fact(3))
print("4 factorial:", fact(4))
print("5 factorial:", fact(5))

print("10 factorial:", factm(10))
