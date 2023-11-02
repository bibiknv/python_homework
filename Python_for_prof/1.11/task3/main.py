class Square:
    def __init__(self, n):
        self.obj = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.obj:
            raise StopIteration
        else:
            self.index += 1
            return self.index ** 2


squares = Square(1)

print(list(squares))
