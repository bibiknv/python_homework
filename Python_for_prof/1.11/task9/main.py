import random

class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > self.n:
            raise StopIteration
        else:
            random_number = random.randrange(self.left, self.right + 1)
            return random_number


iterator = RandomNumbers(1, 10, 2)

for i in RandomNumbers(1, 10, 2):
    print(i)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
