def sum_to(n):
    if n == 0:
        return 0
    else:
        return n + sum_to(n - 1)

print(sum_to(0))
print(sum_to(5))
print(sum_to(10))
print(sum_to(100))
