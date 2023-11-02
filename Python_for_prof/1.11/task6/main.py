class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(list(self.data)):
            raise StopIteration
        else:
            return list(self.data)[self.index], self.data[list(self.data)[self.index]]


data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

pairs = DictItemsIterator(data)

print(*pairs)
