#USACO  Word Processor  2020 January Contest Results

with open('word.in','r') as f:
    reader = f.readlines()
sent = []
essay = []
sent = reader[0].split(' ')
essay = reader[1].split(' ')

N = int(sent[0].strip('\n'))
K = int(sent[1].strip('\n'))

sent_len = 0
new_essay = ''

with open('word.out','w') as f:
    for word in essay:
        sent_len += len(word)  # 4
        if sent_len <= K:  # sent_len = 4
            new_essay = new_essay + word + " "
        else:
            f.write(new_essay[:-1] + '\n')
            new_essay = word + ' '
            sent_len = len(word)
    f.write(new_essay[:-1])
