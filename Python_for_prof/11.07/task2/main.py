import csv

with open('prices.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')

    res_dict = {}
    for i, row in enumerate(reader):
        for key, value in row.items():
            if key != 'Магазин':
                res_dict.setdefault(row['Магазин'], []).append((key, value))

    result_list = []
    for key, value in res_dict.items():
        min_value = list(min(value, key=lambda x: (int(x[1]), x[0])))
        min_value.append(key)
        result_list.append(min_value)
    min_price_product = min(result_list, key=lambda x: (int(x[1]), x[0], x[2]))
    print(min_price_product[0], ': ', min_price_product[2], sep='')

