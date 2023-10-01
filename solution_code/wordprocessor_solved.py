input_file = open('word.in', 'r')
output_file = open('word.out', 'w')

lst = input_file.readline().split()
n = int(lst[0])
# n not needed
k = int(lst[1])

words = input_file.readline().split()
line = ''
chars_on_line = 0

for word in words:
    if chars_on_line + len(word) <= k:
        line = line + word + ' '
        chars_on_line = chars_on_line + len(word)
    else:
        output_file.write(line[:-1] + '\n')
        line = word + ' '
        chars_on_line = len(word)

output_file.write(line[:-1])

input_file.close()
output_file.close()