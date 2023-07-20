
import csv
import json

with open('playgrounds.csv', encoding='utf-8') as csv_file:
    ext_dict = {}
    data = csv_file.read()
    play_ground = [i.split(';') for i in data.splitlines()][1:]
    for x in play_ground:
        ext_dict.setdefault(x[1], {}).setdefault(x[2], []).append(x[3])

    with open('addresses.json', 'w', encoding='utf-8') as file:
        json.dump(ext_dict, file, indent=2, ensure_ascii=False)
