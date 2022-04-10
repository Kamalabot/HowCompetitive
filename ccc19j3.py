# Cold compressing the Cellphone messages ccc19j3

import sys
from collections import defaultdict, Counter

lines = int(sys.stdin.readline())
text = []
for _ in range(lines):
    text.append(sys.stdin.readline().strip('\n'))
compress = []

for c in text:
    compress.append(Counter(c))

for coun in compress:
    print(coun)
