def polynom(x):
    polynom.__dict__.setdefault('value', set())
    result_value = x ** 2 + 1
    if result_value not in polynom.__dict__.values():
        polynom.__dict__['value'] = result_value
    return polynom.__dict__

polynom(1)
polynom(2)
polynom(3)

print(*sorted(polynom.values))
