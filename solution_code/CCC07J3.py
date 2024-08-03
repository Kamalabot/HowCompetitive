#Deal or No Deal CCC07J3

"""Program will help the contenstant to either accept or reject the deal"""

import sys

no_of_cases = int(sys.stdin.readline().strip('\n'))

case_numbers = []

for _ in range(no_of_cases):
    case_numbers.append(int(sys.stdin.readline().strip('\n')))

#case_numbers = [x - 1 for x in case_numbers]

banker = int(sys.stdin.readline().strip('\n'))

x = [x for x in range(1,10)]
y = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
case_values = {x:y for x, y in zip(x, y)}

case_vals = [case_values[num] for num in x if num not in case_numbers]
print(case_vals)
average = sum(case_vals)/ len(case_vals)

print(average)
if banker > average:
    print('deal')
else:
    print('no deal')