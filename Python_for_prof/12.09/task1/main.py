def hash_as_key(objects):
    hash_list = []
    for i in objects:
        hash_list.append(hash(i))
    result = {}
    for j in range(0, len(hash_list)):
        result[hash_list[j]] = result.get(hash_list[j], []) + [objects[j]]
    for key, value in result.items():
        if len(value) == 1:
            result[key] = result[key][0]
    print(result)

data = [-1, -2, -3, -4, -5]

print(hash_as_key(data))

# 1) создаем список их хэшей
#
# 2) создаем словарь из цикла по длине списка любого (хэшей или входящего в функцию), и проделываем такой трюк:
#
# result[hash_list[i]] = result.get(hash_list[i], []) + [lst[i]]
#
# 3) преобразуем словарь, если значение-список состоит из одного элемента, заменяем его result[key][0]
#
# 4) возвращаем словарь
