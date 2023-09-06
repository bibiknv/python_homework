def dict_travel(nested_dicts):
     for i in range(1, 6):
        with open(f'{i}', 'r', encoding='utf-8') as file:
            print(file.read())
            print()
        with open(f'{i}.clue', 'r', encoding='utf-8') as file:
            print(file.read())
            print('---------------------------')

data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)
