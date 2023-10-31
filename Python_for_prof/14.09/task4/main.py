def fib(n):
    f = lambda x: [x == 1] if n <= 2 else [fib(n - 1) + fib(n-2)]
    return int(f)
print(fib(1))
# if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fib(1))

# if n <= 2:
#         return 1                             # базовый случай
#     else:
#         return fib(n - 1) + fib(n - 2)
