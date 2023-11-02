class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if self.index == len(self.iterable):
            self.index = 0
            return self.iterable[0]
        return self.iterable[self.index]

cycle = Cycle([1])

print(next(cycle) + next(cycle) + next(cycle))
