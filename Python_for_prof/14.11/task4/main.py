def cubes_of_odds(iterable):
    for number in iterable:
        if number % 2:
            yield number ** 3


evens = [2, 4, 6, 8, 10]

print(list(cubes_of_odds(evens)))
