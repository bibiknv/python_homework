
class ReverseGenerator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.current = 0
        self.sequence_len = len(sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == len(self.sequence):
            raise StopIteration
        else:
            self.sequence_len -= 1
            self.current += 1
            return self.sequence[self.sequence_len]

sequence = 'beegeek'
print(list(ReverseGenerator(sequence)))
