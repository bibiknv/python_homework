def print_operation_table(operation, rows, cols):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

print_operation_table(lambda a, b: a * b, 5, 5)
