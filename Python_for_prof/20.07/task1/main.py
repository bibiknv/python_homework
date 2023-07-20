import json
import csv

with open("students.json", "r", encoding="utf-8") as file:
    dict_result = {}
    js_data = json.load(file)
    for i in js_data:
        if int(i["age"]) >= 18 and int(i["progress"]) >= 75:
            dict_result.setdefault('name', []).append(i['name'])
            dict_result.setdefault('phone', []).append(i['phone'])
    columns_name = []
    for key in dict_result.keys():
        columns_name.append(key)


with open('data.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns_name, delimiter=',')
    writer.writerow(columns_name)
    for object in dict_result:
        print(object)
        # writer.writerow((object['name'],dict_result['phone']))



