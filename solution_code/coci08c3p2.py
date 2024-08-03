#Kemija coci08c3p2

import sys
import typing

cemija = sys.stdin.readline()
cemija = cemija.strip('\n')
data = cemija.split(' ')

vowel = ['a','e','i','o','u']


def decode(data: str) ->str:
    data = list(data)
    i = 0
    while i < len(data):
        if data[i] == 'p' and data[i+1] in vowel:
            #print(data[i])
            data.pop(i+1)
            data.pop(i)
        i += 1
    return ''.join(data)

new_sent = []

for word in data:
    new_sent.append(decode(word))

print(" ".join(new_sent))
