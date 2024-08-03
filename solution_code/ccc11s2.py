#Multiple Choice ccc11s2

import sys

quest = int(sys.stdin.readline())
answer = []
key = []

for _ in range(quest):
    answer.append(sys.stdin.readline())
for _ in range(quest):
    key.append(sys.stdin.readline())

result = 0
for x in range(quest):
    if answer[x] == key[x]:
        result += 1

print(result)