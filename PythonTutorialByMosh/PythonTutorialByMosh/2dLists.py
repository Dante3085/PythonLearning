
matrix = \
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[1][1])
print(matrix[2][:])
print(matrix[0][-2])

matrix[2][2] = 20
print(matrix)

for row in matrix:
    row_str = ""
    for column in row:
        row_str += str(column) + " "
    print(row_str)