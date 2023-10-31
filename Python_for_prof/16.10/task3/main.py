import functools

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        x = repr(args)
        print(f"TRACE: вызов {func.__name__}() с аргументами: {x}, {dict(kwargs)}")
        print(f"TRACE: возвращаемое значение {func.__name__}(): '{func(*args, **kwargs)}'") if type(func(*args, **kwargs)) == str else print(f"TRACE: возвращаемое значение {func.__name__}(): {func(*args, **kwargs)}")
        return func(*args, **kwargs)
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'

say('Jane', 'Hello, World')


