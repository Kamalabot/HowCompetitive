#Magnus coci18c3p1
#import re

def removeDuplicates(s:str) ->str:
    chars = []
    prev = None
 
    for c in s:
        if prev != c:
            chars.append(c)
            prev = c
 
    return ''.join(chars)

def remove_notwanted(s:str) ->str:
    for c in s:
        if c not in 'HONI':
            s = s.replace(c,"")
    return s

def wrong_char(s: str)-> str:
    char = []
    prev = None
    for c in word:
        if prev == 'H':
            if c != 'N' and c != 'I':
                char.append(c)
                prev = c
        elif prev == 'O':
            if c != 'H' and c != 'I':
                char.append(c)
                prev = c
        elif prev == 'N':
            if c != 'H' and c != 'O':
                char.append(c)
                prev = c
        elif prev == 'O':
            if c != 'N' and c != 'I':
                char.append(c)
                prev = c
        else:
            char.append(c)
            prev = c
    return ("").join(char)

word =input("") #get input

word = removeDuplicates(word)
word = remove_notwanted(word)
word = wrong_char(word)

any_honi = word.count('HONI')

print(any_honi)
