import csv

with open('titanic.csv', encoding='utf-8') as file:
    data = file.read()
    rows = [r.split(';') for r in data.splitlines()]
    del rows[0]
    result_dict ={}
    for row in rows:
        if int(row[0]) == 1 and float(row[3]) < 18:
            if row[1] not in result_dict:
                result_dict[row[1]] = row[2]
    result_dict = sorted(result_dict.items(), key=lambda x: x[1], reverse= True)
    for name in result_dict:
        print(name[0])



    # result_dict = sorted(result_dict.items(), key=lambda x: (-x[1], x[0]))
    #
    # for row_dict in result_dict:
    #     print(row_dict[0], ': ', row_dict[1], sep = '')
