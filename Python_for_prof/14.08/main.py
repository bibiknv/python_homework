# from collections import ChainMap
#
# animals = ChainMap({'monkey': 10, 'elephant': 3, 'lemur': 7},
#                    {'monkey': 1, 'elephant': 2, 'lemur': 12, 'bear': 1})
#
# print(animals.get('monkey'))
# print(animals['bear'])


# from collections import ChainMap
#
# info = ChainMap({'name': 'Rose', 'age': 17},
#                 {'country': 'USA', 'city': 'Seattle'})
#
# print(info['hobby'])


# from collections import ChainMap, defaultdict
#
# info = ChainMap(defaultdict(int, {'name': 'Rose', 'age': 17}),
#                 {'country': 'USA', 'city': 'Seattle'})
#
# print(info['hobby'])
#

# from collections import ChainMap, defaultdict
#
# info = ChainMap({'hobby': 'math', 'country': 'USA', 'city': 'Seattle'},
#                 defaultdict(int, {'name': 'Rose', 'age': 17}))
#
# print(info['hobby'])


# from collections import ChainMap
#
# letters = ChainMap({'a': 'A', 'b': 'B'},
#                    {'b': 'B', 'c': 'C'})
#
# letters['b'] = 'BB'
#
# print(letters)


# from collections import ChainMap
#
# letters = ChainMap({'a': 'A'},
#                    {'b': 'B', 'c': 'C'},
#                    {'d': 'D', 'e': 'E'})
#
# print(letters.pop('e'))


from collections import ChainMap

animals = ChainMap({'alligator': 3, 'jaguar': 2},
                   {'eagle': 5, 'zebra': 2},
                   {'bear': 2, 'alligator': 1},
                   {'lemur': 7, 'elephant': 3})

print(len(animals))




