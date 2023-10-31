def is_iterator(obj):
    try:
        next(obj)
        return True
    except Exception as e:
        return False

beegeek = filter(None, [0, 0, 1, 1, 0, 1])

print(is_iterator(beegeek))
