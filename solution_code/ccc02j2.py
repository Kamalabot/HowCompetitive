# AmeriCanadian challenge ccc02j2

import sys

word_list = []
while True:
    word_list.append(sys.stdin.readline().strip('\n'))
    if word_list[-1] == 'quit!':
        break
vowels = ','.join('aeiouy')
new_list = []
for word in word_list[:-1]:
    if len(word) > 4 and word[-2:] == 'or' and word[-3] not in vowels:
        word = word[:-2] + 'our'
        new_list.append(word)
    else:
        new_list.append(word)
[print(x) for x in new_list]

