import json


with open('countries.json', encoding='utf-8') as file:
    result_dict = {}
    d = {}
    dict_countries = json.load(file)
    for i in dict_countries:
        country_key = i['country']
        religion_key = i['religion']
        result_dict[religion_key] = result_dict.get(religion_key, []) + [country_key]

    with open('religion.json', 'w', encoding='utf-8') as file:
        json.dump(result_dict, file, indent=2)





# d = {}
# numbers = [1, 2, 3]
#
# for digit in numbers:
#     d.setdefault('key', []).append(digit)
#
# print(d)  # {'key': [1, 2, 3]}
