#An Honest Day's work wc18c3j1

P = int(input(""))
B = int(input(""))
D = int(input(""))

N = P // B
R = P % B

cash = N * D

total = cash + R
print(total)
