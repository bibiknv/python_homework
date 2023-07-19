
import json

with open('data.json') as file:
    result_list = []
    data = json.load(file)
    for object in data:
        if type(object) == str:
            result_list.append((object + '!'))
        elif type(object) == bool:
            result_list.append((not object))
        elif type(object) == int:
             result_list.append((object + 1))
        elif type(object) == list:
            copy_list = object + object
            result_list.append(copy_list)
        elif type(object) == dict:
            object.update({"newkey": None})
            print(object)
            result_list.append(object)
        if object is None:
            pass

with open('data_out.json', 'w', encoding='utf8') as file:
    json.dump(result_list, file, indent=3, )


