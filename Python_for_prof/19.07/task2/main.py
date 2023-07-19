import json

with open('people.json', encoding='utf-8') as file:
    js_people = json.load(file)
    pattern = max(js_people, key=len)
    for i in js_people:
        for key, value in pattern.items():
             i[key] = i.get(key, None)

    with open('updated_people.json', 'w', encoding='utf-8') as file:
        json.dump(js_people, file, indent=2)
