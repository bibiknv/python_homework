import json

with open('data1.json', encoding='utf-8') as file:
    data_first = json.load(file)

with open('data2.json', encoding='utf-8') as file:
    data_second = json.load(file)

data_3 = data_first | data_second

with open('data_merge.json', 'w') as file:
    json.dump(data_3, file, indent=3)


