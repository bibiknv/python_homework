class PowerOf:
    def __init__(self, number):
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.obj:
            raise StopIteration
        else:
            self.index += 1
            return self.index ** 2


power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
