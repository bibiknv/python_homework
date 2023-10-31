def decor(func):
    def behavior(*args, **kwargs):
        args = (str(i).upper() for i in args)
        kwargs = {i: j.upper() for i, j in kwargs.items()}
        func(*args, **kwargs)
    return behavior

print = decor(print)

print(111, 222, 333, sep='xxx')



