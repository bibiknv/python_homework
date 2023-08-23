def add_to_list_in_dict(data,key,element):
    new_data = data.setdefault(key, []).append(element)
    return new_data


data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
add_to_list_in_dict(data, 'c', 7)

print(data)
