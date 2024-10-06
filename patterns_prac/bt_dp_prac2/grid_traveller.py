def gt(m, n):
    # base case 1, there is just a cell
    if m == 1 and n == 1:
        return 1

    # base case 2, as there is no 2d space
    if m == 0 or n == 0:
        return 0
    # reduce the problem space in every call
    return gt(m - 1, n) + gt(m, n - 1)
