def gridTraveller(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraveller(m - 1, n) + gridTraveller(m, n - 1)


def memo_gridTraveller(m, n, memo={}):
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[(m, n)] = memo_gridTraveller(m - 1, n, memo) + memo_gridTraveller(m, n - 1, memo)
    return memo[(m, n)]

#Testing

print(gridTraveller(1, 1))
print(gridTraveller(2, 2))
print(gridTraveller(3, 3))
print(memo_gridTraveller(18, 18, {}))
