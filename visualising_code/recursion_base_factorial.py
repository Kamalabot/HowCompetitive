# The code implementing factorial calculation recursively

def fact(n: int) -> int:
    if n <= 0:
        return 1
    return n * fact(n - 1)


print(fact(6))
print(fact(1))
print(fact(100))
print(fact(2))