old_print = print

def print(*args, **kwargs):
    caps = tuple(c.upper() if isinstance(c, str) else c for c in args)
    if len(kwargs) == 0:
        return old_print(*caps)
    else:
        return old_print(*caps, sep = kwargs['sep'].upper(), end = kwargs['end'].upper())

words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')
