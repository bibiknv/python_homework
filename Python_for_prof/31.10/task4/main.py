def starmap(func, iterable):
    result_list = list(zip(*iterable))
    return map(func, *result_list)

points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]

print(*starmap(lambda x, y, z: x * y * z, points))
