class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.times:
            raise StopIteration
        else:
            self.index += 1
            return self.obj

geek = BoundedRepeater('geek', 3)

print(next(geek))
print(next(geek))
print(next(geek))

try:
    print(next(geek))
except StopIteration:
    print('Error')

