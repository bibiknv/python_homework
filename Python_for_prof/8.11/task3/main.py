def primes(left, right):
    for i in range(left, right + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            yield i
    return

generator = primes(6, 36)

print(next(generator))
print(next(generator))
