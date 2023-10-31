def do_twice(func):
    def wrapper(*args, **kwargs):
        m = func(*args, **kwargs)
        m = func(*args, **kwargs)
        return m
    return wrapper

@do_twice
def beegeek():
    print('beegeek')

print(beegeek())

