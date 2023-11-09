def alternating_sequence(count=None):
    n = 1
    while True:
        if n % 2 == 0:
            yield -n
        else:
            yield n
        n += 1
        if not(count is None) and n > count:
            return



generator = alternating_sequence(10)

print(*generator)

