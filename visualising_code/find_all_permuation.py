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
print(permute(perm_me))
