def palindromes():
    start = 1
    while True:
        if str(start) == str(start)[::-1]:
            yield start
        start += 1
    yield from palindromes()


generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)


