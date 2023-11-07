from typing import List, Dict

def canConstruct00(target, wordBank):
    if target == "":
        return True
   
    for bnk in wordBank:
        # print('target_prefix', target[:len(bnk)])
        if target[:len(bnk)] == bnk:
            remainder = target[len(bnk):]
            # print('remainder', remainder)
            canConstruct00(remainder, wordBank)
            return True

    return False


# print(canConstruct00("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(canConstruct00("skateboard", ["bo", "rd", "ate", "t", "ska","boar"]))


def canConstruct(target: str, wordBank: List[str]) -> bool:
    if target == "":
        return True
 
    for word in wordBank:
        # if target.index(word) == 0: # This will throw ValueError if the searching word is not found
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank):
                return True
    return False

# print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "boar"]))
# print(canConstruct("jjjjjjjjjjjjjjjjjjjjjjjjjjo", ["jj", "jjjj", "jjjjjjj", "j", "oj", "ooj"]))

 
def canConstructMemo(target: str, wordBank: List[str], memo: Dict = dict()) -> bool:
    if target in memo:
        return memo[target]

    if target == "":
        return True
 
    for word in wordBank:
        # if target.index(word) == 0: # This will throw ValueError if the
        # searching word is not found
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstructMemo(suffix, wordBank, memo):
                memo[target] = True
                return memo[target]
    memo[target] = False
    return memo[target]


# print(canConstructMemo("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(canConstructMemo("skateboard", ["bo", "rd", "ate", "t", "ska", "boar"]))
# print(canConstructMemo("jjjjjjjjjjjjjjjjjjjjjjjjjjo", ["jj", "jjjj", "jjjjjjj", "j", "oj", "ooj"]))

def countConstruct(target: str, wordBank: List[str]):
    if target == "":
        return 1

    tot_cnt = 0 

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            # print(suffix)
            cnt = countConstruct(suffix, wordBank)
            tot_cnt += cnt
    
    return tot_cnt


# print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))

def countConstructMemo(target: str, wordBank: List[str], memo: Dict=dict()):
    if target in memo:
        return memo[target]

    if target == "":
        return 1

    tot_cnt = 0 

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            # print(suffix)
            cnt = countConstructMemo(suffix, wordBank, memo)
            tot_cnt += cnt

    memo[target] = tot_cnt
    return memo[target]


# print(countConstructMemo('pururururururpppppppplelelelele', ['purp', 'p', 'ur', 'le', 'purpl','urur','lele']))
# print(countConstruct('pururururururpppppppplelelelele', ['purp', 'p', 'ur', 'le', 'purpl','urur','lele']))


def allConstruct(target: str, wordBank: List[str]):
    if target == "":
        return [[]]
    all_ways = [] 
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank)
            targetWays = [way.insert(0, word) for way in suffixWays]
            all_ways.append(targetWays)
            
    return all_ways 


# print(allConstructMemo('pururururururpppppppplelelelele', ['purp', 'p', 'ur', 'le', 'purpl','urur','lele']))
# print(allConstruct('pururururururpppppppplelelelele', ['purp', 'p', 'ur', 'le', 'purpl','urur','lele']))
print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))