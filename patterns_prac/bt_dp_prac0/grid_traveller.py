# Given a n x n grid starting at top left
# find how many ways you can reach the
# bottom right corner. You can move right & down

# intu1 : 2 base cases m, n = 1 / m or n = 0
# intu2 : reduce the gridsize and recurse


def gt(m, n):
    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    return gt(m - 1, n) + gt(m, n - 1)


def mem_gt(m, n, memo={}):
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    memo[(m, n)] = mem_gt(m - 1, n, memo) + mem_gt(m, n - 1, memo)
    return memo[(m, n)]
