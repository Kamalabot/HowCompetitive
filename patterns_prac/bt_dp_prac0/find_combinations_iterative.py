def combinations(n, k):
    result = []
    stack = [(0, [])]

    while stack:
        start, path = stack.pop()
        if len(path) == k:
            result.append(path)
            continue  # skips the below code
        for i in range(start, n):
            stack.append((i + 1, path + [i + 1]))

    return result


print(combinations(4, 2))
