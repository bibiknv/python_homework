def get_all_values(nested_dicts, key):
    new_list = []
    if key in nested_dicts:
        new_list.append(nested_dicts[key])
    for v in nested_dicts.values():
        if type(v) == dict:
            value = get_all_values(v, key)
            get_all_values(nested_dicts).update(value)
            if value is not None:
                return value

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(result)
