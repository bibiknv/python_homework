def find_key(data, key):
    if key in data:
        return data[key]

    for v in data.values():
        if type(v) == dict:
            value = find_key(v, key)
            if value is not None:
                return value


info = {'name': 'Alyson',
        'surname': 'Hannigan',
        'birthday': {'day': 24, 'month': 'March', 'year': 1974},
        'family': {'parents': {'mother': 'Emilie Posner', 'father': 'Alan Hannigan'}}}

print(find_key(info, 'year'))
print(find_key(info, 'father'))
