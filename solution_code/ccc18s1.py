#Villages of Voronoi ccc18s1

import sys

n = int(sys.stdin.readline())
village = []

for _ in range(n):
    village.append(int(sys.stdin.readline()))

village = sorted(village)

diff = []

# 0 4 10 15 16
for ind, vill in enumerate(village):
    if ind != 0 and ind != len(village) - 1:
        #print(ind)
        left = (village[ind + 1] - village[ind]) / 2
        right = (village[ind] - village[ind - 1]) / 2
        diff.append(left + right)

print(min(diff))
