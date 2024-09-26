# Problem Statment: Find the sum of the fibbonacci series of a given number


def fibo(n):
    if n <= 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


# intuition 0: having a cache to store the results
# intuition 1: sending the cache as func parameter, \
# intuition 2: checking if the number called is in memo, then use it
# intuition 3: n <=2 returns 1 is base case
# intuition 4: call fibo(n - 2, memo) + fibo(n -1, memo)
# intuition 3: before returning, the value is updated to cache


def fibo_memo(h, memo=dict()):
    if h in memo:
        return memo[h]

    if h <= 2:
        return 1

    memo[h] = fibo_memo(h - 1, memo) + fibo_memo(h - 2, memo)
    return memo[h]


print(f"Fibo sum of 2: {fibo(2)}")
print(f"Fibo sum of 5: {fibo(5)}")
print(f"Fibo sum of 10: {fibo(10)}")
