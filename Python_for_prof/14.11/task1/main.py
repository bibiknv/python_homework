def matrix_by_elem(matrix):
    for i in matrix:
        yield from i


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(*matrix_by_elem(matrix))

# def matrix_by_elem(matrix):
#     for row in matrix:
#         for elem in row:
#             yield elem
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# print(*matrix_by_elem(matrix))
