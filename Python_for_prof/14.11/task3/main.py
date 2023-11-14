def flatten(nested_list):
    new_list = []
    for i in nested_list:
        if type(i) == int:
            yield i
        if type(i) == list:
            yield from flatten(i)

generator = flatten([1, 2, 3, 4, 5, 6, 7])

print(*generator)
