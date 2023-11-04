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


# print(canSumBrute(7, [5, 3, 4, 7]))
# print(canSumBrute(7, [2, 4, 7]))
# print(canSumBrute(7, [2, 4]))
# print(canSumBrute(657, [2, 4]))


def canSumMemo(tgt, numArray, memo=dict()):
    # Base conditions are same, not changing 
    if tgt == 0:
        return True
    if tgt < 0:
        return False
    
    for num in numArray:
        if canSumMemo(tgt - num, numArray, memo):
            memo[tgt] = True
            return memo[tgt]

    return False


print(canSumMemo(7, [2, 4]))
print(canSumMemo(7, [3, 4, 7]))
print(canSumMemo(658, [3, 4, 7]))
