def fib(n):
    if n <= 2:
        return 1                             # базовый случай
    else:
        return fib(n - 1) + fib(n - 2)
