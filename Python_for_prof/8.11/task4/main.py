# class GenerateInts:
#     def __init__(self, n):         # конструктор принимает верхнюю границу диапазона
#         self.n = n
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current == self.n:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current - 1
#
#
# def generate_ints(n):
#     i = 0
#     while i != n:
#         i += 1
#         yield i - 1
#
#
# n = 5
# print(list(GenerateInts(n)), list(generate_ints(n)))

def reverse(sequence):
    i = len(sequence)
    while i != 0:
        i -= 1
        yield sequence[i]


sequence = 'beegeek'
print(list(reverse(sequence)))

def reverse(sequence):
    for i in range(len(sequence) -1, -1, -1):
        yield sequence[i]

class ReverseGenerator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.current = len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == len(self.sequence):
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


def reverse(sequence):
    i = len(sequence)
    while i != 0:
        i -= 1
        yield sequence[i]

# sequence = 'beegeek'
# print(list(ReverseGenerator(sequence)))

# generator = reverse(list(reverse('beegeek')))
#
# print(type(generator))
# print(list(generator))
#
#
#
# #
# # generator = reverse('beegeek')
# #
# # print(type(generator))
# # print(*generator)
