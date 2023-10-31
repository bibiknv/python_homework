def fib(num):
    if num < 2:
        return num
    if num not in fib.__dict__:
        fib.__dict__[num] = fib(num - 1) + fib(num - 2)
    return fib.__dict__[num]

fib(5)
