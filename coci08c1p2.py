#Ptice by Adrian, Bruno and Goran coci08c1p2
"""The code is passing 50%. Need to work on it based on the clue I get"""
import sys

questions = int(sys.stdin.readline())
answer_key = sys.stdin.readline().strip('\n')

answer_key = answer_key.replace('A','1')
answer_key = answer_key.replace('B','2')
answer_key = answer_key.replace('C','3')
    
answer_key = list(answer_key)
answer_key = [int(x) for x in answer_key]

adrian =[]
bruno = [2]
goran = [3]

q_a = 0
i = 0
while True:
    adrian.append(i + 1)
    bruno.append(i + 1)
    goran.append(i + 1)
    goran.append(i + 1)
    i = i + 1
    if i == 3:
        i = 0
        bruno.append(2)
    q_a += 1
    if q_a == questions:
        break
q_c = 0
i = 0

adrian = adrian[:questions]
bruno = bruno[:questions]
goran = goran[:questions]

ad = br = go = 0

for x in range(questions): 
    if adrian[x] == answer_key[x]:
        #print(adrian[x])
        #print(answer_key[x])
        ad += 1
    if bruno[x] == answer_key[x]:
        #print(bruno[x])
        #print(answer_key[x])
        br += 1
    if goran[x] == answer_key[x]:
        #print(goran[x])
        #print(answer_key[x])
        go += 1

result = [ad, br, go]
participants = ['Adrian', 'Bruno', 'Goran']

print(max(result))

#print(participants[result.index(max(result))])

res_dict ={}

for i in range(3):
    res_dict[participants[i]] = result[i]

res = sorted(res_dict)
#print(res)
for i in res:
    if res_dict[i] == max(result):
        print(i)
#print(adrian)
#print(bruno)
#print(goran)
#print(answer_key)