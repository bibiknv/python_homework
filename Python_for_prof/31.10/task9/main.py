from random import randint

def random_numbers(left, right):
    return iter(lambda: randint(left, right), right + 1)


iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
