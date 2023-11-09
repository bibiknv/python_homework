class Xrange:
    def __init__(self, start, end, step = 1):
        self.start = start
        self.end = end
        self.step = step
        self.index = -1
        self.cur = start

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == 0:
            return self.cur
        self.cur += self.step
        if (self.cur - self.end) * self.step >= 0:
            raise StopIteration
        return self.cur

xrange = Xrange(5, 10)

print(*xrange)
