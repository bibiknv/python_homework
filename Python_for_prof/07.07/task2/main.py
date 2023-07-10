import csv


def csv_columns(filename):
    result_dict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file, delimiter=',')
        for row in rows:
            for key in list(row.keys()):
                result_dict[key] = result_dict.get(key, []) + [row[key]]
    return result_dict

print(csv_columns('data.csv'))
