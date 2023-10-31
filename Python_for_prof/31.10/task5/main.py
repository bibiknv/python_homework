import copy

def get_min_max(iterable):
    iterable_1 = iterable
    iterable_2 = copy.copy(iterable_1)
    try:
        return min(iterable_1), max(iterable_2)
    except Exception as e:
        return None


iterable = [6, 4, 2, 33, 19, 1]

print(get_min_max(iterable))
