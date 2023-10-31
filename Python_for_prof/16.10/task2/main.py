def returns_string(func):
    def wrapper(*args, **kwargs):
        if type(func(*args, **kwargs)) == str:
            return func(*args, **kwargs)
        else:
            raise TypeError
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

@returns_string
def add(a, b):
    return a + b

try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))
