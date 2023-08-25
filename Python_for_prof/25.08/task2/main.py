def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print('Факториал числа 4 равен', factorial(4))
