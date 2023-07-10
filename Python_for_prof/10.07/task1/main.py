import csv

with open('data.csv', encoding='utf-8') as file:
    data = file.read()
    rows = [r.split('@') for r in data.splitlines()]
    del rows[0]
    value = 0
    result_dict ={}
    for row in rows:
        if row[1] not in result_dict:
            result_dict[row[1]] = 1
        else:
            result_dict[row[1]] += 1
    result_dict = sorted(result_dict.items(), key=lambda x: (x[1], x[0]))

    columns = ['domain', 'count']
    with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        for row in result_dict:
            writer.writerow(row)

