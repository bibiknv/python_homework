def prefix(string, to_the_end = False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if to_the_end:
                return value + string
            else:
                return string + value
            return func(*args, **kwargs)
        return wrapper
    return decorator

@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'

print(get_bonus())
