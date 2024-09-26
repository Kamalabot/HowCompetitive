def permutations(nums):
    result = []
    stack = [(nums, [])]

    while stack:
        remaining, path = stack.pop()
        if not remaining:
            result.append(path)
            continue
        for i in range(len(remaining)):
            stack.append((remaining[:i] + remaining[i + 1 :], path + [remaining[i]]))
    return result


print(permutations([1, 2, 3]))
