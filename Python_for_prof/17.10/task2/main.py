import functools

def takes(*types_decorator):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in args + tuple(kwargs.values()):
                if isinstance(i, types_decorator):
                    continue
                else:
                    raise TypeError
            res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator


@takes(list, bool, float, int)
def repeat_string(string, times):
    assert isinstance(times, int), "uhiuy"
    return string * times

try:
    print(repeat_string([1, 2], "vgufty"))
except TypeError as e:
    print(type(e))
