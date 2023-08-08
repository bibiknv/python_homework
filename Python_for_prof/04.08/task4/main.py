from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    obj = pickle.load(file)
    for info in obj:
        timur = Animal(*info)
        for field, value in zip(Animal._fields, timur):
            print(field, ': ', value, sep = '')
        print('')

