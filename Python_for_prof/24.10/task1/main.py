import functools

def add_attrs(**kwargs):
    def decorator(func):
        for key, value in kwargs.items():
            func.__dict__[key] = value
        print(func.__dict__)
        # @functools.wraps(func)
        # def wrapper(*args, **kwargs):
        #     return func(*args, **kwargs)
        return func
    return decorator


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'

print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)
