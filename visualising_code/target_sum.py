# Contains the code for various Sum problem
# solved using the DP memoization and brute force method

def canSumBrute(tgt, numArray):
    # if the tgt is 0, then we can return True
    if tgt == 0:
        return True
    # if the tgt is negative, there is no solution so return False
    if tgt < 0:
        return False
    # check each number, and bubble up the results by returning

    for num in numArray:
        # if the num can create the tgt sum, then return True
        if canSumBrute(tgt - num, numArray):
            return True

    # After all the elems of the array are traversed, not found a way. Then return false

    return False

# m = tgt
# n = len(numArray)
# O(n * m)

# print(canSumBrute(7, [5, 3, 4, 7]))
# print(canSumBrute(7, [2, 4, 7]))
# print(canSumBrute(7, [2, 4]))
# print(canSumBrute(657, [2, 4]))


def canSumMemo(tgt, numArray, memo=dict()):
    # Base conditions are same, not changing
    if tgt in memo:
        return memo[tgt]

    if tgt == 0:
        return True

    if tgt < 0:
        return False
    
    for num in numArray:
        if canSumMemo(tgt - num, numArray, memo):
            memo[tgt] = True
            return memo[tgt]

    return False


# print(canSumMemo(7, [2, 4]))
# print(canSumMemo(7, [3, 4, 7]))
# print(canSumMemo(658, [3, 4, 7]))

def howSum(tgt, numArray):
    if tgt == 0:
        return list()

    if tgt < 0:
        return None

    for x in numArray:
        # print(x)
        ret_reminder = howSum(tgt - x, numArray)
        if ret_reminder is not None:
            return ret_reminder[:] + [x]
 

# print(howSum(7, [5, 3, 4, 7]))


def howSumMemo(tgt, numArray, memo=dict()):
    if tgt in memo:
        return memo[tgt]

    if tgt == 0:
        return list()

    if tgt < 0:
        return None

    for x in numArray:
        # print(x)
        ret_reminder = howSum(tgt - x, numArray)
        if ret_reminder is not None:
            memo[tgt] = ret_reminder[:] + [x]
            return memo[tgt]

    memo[tgt] = None
    return memo[tgt]


# print(howSumMemo(70, [7, 3, 4, 5]))
# print(howSumMemo(700, [7, 3, 4, 5]))


def bestSum(tgt, numArray):
    if tgt == 0:
        return list()

    if tgt < 0:
        return None

    shortest = None

    for x in numArray:
        # print(x)
        ret_reminder = howSum(tgt - x, numArray)
        if ret_reminder is not None:
            temp = ret_reminder[:] + [x]
            if shortest is None or len(temp) < len(shortest):
                shortest = temp
    
    return shortest


print(bestSum(5, [5, 4, 3, 7]))
print(bestSum(105, [1,25, 4, 5, 7]))
# print(bestSum(100005, [25, 4, 5, 7]))
