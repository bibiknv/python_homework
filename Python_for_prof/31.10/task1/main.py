def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    filter_result = filter(lambda x: predicate(x) is False, iterable)
    return filter_result

objects = [0, 1, True, False, 17, []]

print(*filterfalse(None, objects))
