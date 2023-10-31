
def takes_positive(func):          # определяем декоратор
    def wrapper(*args, **kwargs):
        full_args = args + kwargs.values()
        for index in full_args:
            if type(index) != int:
                raise TypeError
        for index in full_args:
            if index <= 0:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)

try:
    print(positive_sum(-3, "df"))
except Exception as err:
    print(type(err))

