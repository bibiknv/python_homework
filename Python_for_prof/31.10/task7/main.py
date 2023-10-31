def is_iterable(obj):
    is_iterable = hasattr(obj, '__iter__')
    return is_iterable

objects = [(1, 13), 7.0004, [1, 2, 3]]

for obj in objects:
    print(is_iterable(obj))
