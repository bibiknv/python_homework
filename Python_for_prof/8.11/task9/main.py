def interleave(*args):
    result_list = list(zip(*args))
    for i in result_list:
        yield from i

numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]

print(*interleave(numbers, squares, qubes))
