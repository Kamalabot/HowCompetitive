def subset(nums):
    result = []
    stack = [(0, [])]

    while stack:
        start, path = stack.pop()
        result.append(path)
        for i in range(start, len(nums)):
            stack.append((i + 1, path + [nums[i]]))
    return result


print(subset([1, 2, 3]))
