def fibo(n):
    if n <= 2: return 1
    return fibo(n - 1) + fibo(n - 2)


print(fibo(1))
print(fibo(2))
#print(fibo(50))

# Memoization in the code
def fibom(n, memo=dict()):
    if n in memo:  
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibom(n - 1, memo) + fibom(n - 2,memo)
    return memo[n]


print(fibom(5))
print(fibom(50))
