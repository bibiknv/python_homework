import csv

def condense_csv(filename, id_name='ID'):
    with open(filename, encoding='utf-8') as file:
        id_name_lst = [id_name]
        result_dict = {}
        rows = csv.reader(file)
        for row in rows:
            if row[1] not in id_name_lst:
                id_name_lst.append(row[1])
            result_dict.setdefault(row[0], []).append(row[2])

    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(id_name_lst)
        for key, value in result_dict.items():
            writer.writerow([key, *value])


condense_csv('data.csv', id_name='ID')
