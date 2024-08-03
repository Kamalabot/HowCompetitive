#English Vs French ccc11s1
import sys

lines = sys.stdin.readline()
text = []

for _ in range(int(lines)):
    text.append(sys.stdin.readline())

t = s = 0

for l in text:
    t = t + l.count('t') + l.count('T')
    s = s + l.count('s') + l.count('S')
if t > s:
    print("English")
elif s > t:
    print("French")
else:
    print('French')