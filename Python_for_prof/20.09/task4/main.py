
from collections import deque

def cyclic_shift(numbers: list[int] | list[float], step: int) -> None:
    temp = deque(numbers)
    temp.rotate(step)
    numbers[:] = [c for c in temp]
    return numbers

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)
annotations = cyclic_shift.__annotations__

print(annotations['numbers'])
print(numbers)
