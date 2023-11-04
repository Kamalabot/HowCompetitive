from typing import List


def permute(num: List[int]) -> List[List[int]]:
    result = []

    # base case
    if (len(num)) == 1:
        return [num[:]]

    for x in range(len(num)): #1 in range(3) # 1 in range(2) 
        n = num.pop()        #num = [1,2] n = 3 # num = [1] n = 2 
        permutations = permute(num) # permns = permute([1,2]) # permns = permute([1]) = [1] 

        for perm in permutations: #--#for perm in [1] 
            perm.append(n) #--#[1].append(2)
        result.extend(permutations) #--#[[1,2]]
        num.append(n) #--#num=[1,2] 
    
    return result #--#[[1,2]]


perm_me = [1, 2, 3]
# print(permute(perm_me))


def permuto(elements: List[int]) -> List[List[int]]:

    if len(elements) == 0:
        return [elements]

    firstEl = elements[0]
    restEl = elements[1:]
    print('firstEl', firstEl)
    print('restEl', restEl)
    permWOFirst = permuto(restEl)

    permutationAll = []
    for perm in permWOFirst:
        for i in range(len(perm)):
            # iterate all possible insertion position
            permWFirst = perm[:i] + [firstEl] + perm[i:]
            permutationAll.append(permWFirst)
    
    return permutationAll


perm_one = ['a']
print('final_out', permuto(perm_one))


def permutations(arr):
    if len(arr) <= 1:
        return [arr]

    result = []
    for i, element in enumerate(arr):
        rest = arr[:i] + arr[i+1:]
        for p in permutations(rest):
            result.append([element] + p)

    return result


# Example usage:
numbers = [1, 2, 3]
all_permutations = permutations(numbers)

print(all_permutations)
