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


print(canConstruct00("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct00("skateboard", ["bo", "rd", "ate", "t", "ska","boar"]))


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


print(canConstructMemo("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstructMemo("skateboard", ["bo", "rd", "ate", "t", "ska", "boar"]))
print(canConstructMemo("jjjjjjjjjjjjjjjjjjjjjjjjjjo", ["jj", "jjjj", "jjjjjjj", "j", "oj", "ooj"]))
