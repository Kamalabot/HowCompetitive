list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 2, 4, 1, 10]

# return the third list that contains above elements without duplicatest

list3 = []

for x in list1:
    if x not in list3:
        list3.append(x)

for x in list2:
    if x not in list3:
        list3.append(x)

# print(list3)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

t_matrix = []

for i in range(3):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    t_matrix.append(new_row)

print(t_matrix)
