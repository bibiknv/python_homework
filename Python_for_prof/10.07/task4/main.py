

import csv

with open('name_log.csv', encoding='utf-8') as file:
    data = file.read()
    rows = [r.split(',') for r in data.splitlines()]
    first_row = rows[0]
    del rows[0]
    expensive = sorted(rows, key=lambda item: item[2])
    result_dict = {}
    for row in expensive:
        if row[1] not in result_dict:
            result_dict[row[1]] = list(row)
        else:
            result_dict[row[1]] = list(row)

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(first_row)
    for v in sorted(result_dict.values(), key=lambda v: v[1]):
        writer.writerow(v)


