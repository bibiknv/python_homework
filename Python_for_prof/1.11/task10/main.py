class Alphabet:
    def __init__(self, language):
        self.data = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}
        self.language = language
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        result_list = list(self.data[self.language])
        if self.index < len(result_list):
            for i in range(0, len(result_list) + 1):
                return result_list[self.index]
        if self.index == len(result_list):
            self.index = 0
            return result_list[self.index]


en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)
