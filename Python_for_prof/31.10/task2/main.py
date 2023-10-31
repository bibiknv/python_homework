def transpose(matrix):
    matrix_transpose = [list(i) for i in zip(*matrix)]
    return matrix_transpose

matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10]]

for row in transpose(matrix):
    print(row)
