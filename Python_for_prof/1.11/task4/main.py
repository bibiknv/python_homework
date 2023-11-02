class Fibonacci:
    def __init__(self):
        self.prev = 1
        self.next_to_prev = 1
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index <= 3:
            return 1
        else:
            self.prev, self.next_to_prev = self.next_to_prev, self.prev + self.next_to_prev
            return self.next_to_prev

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
