import csv
with open('student_counts.csv', 'r', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=','))
    file_names = [i for i in reader[0]]
    sorted_file_names = sorted(file_names, key = lambda x: (len(x), x))
    print(reader)

with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(sorted_file_names)
    for row in reader:
        for s in row:
            writer.writerow(row)

    # reader.fieldnames
    # result = []
    # result_list = list(reader)
    # for dct_i in result_list:
    #     print(type(dct_i))
        # dct_i = sorted(dct_i, key = lambda x: (len(x), x))
        # print(type(dct_i))


# Для тех кто отчаялся:
#
# 1.  Создаем список  примерно так list(csv.DictReader(file))
#
# 2. Создаем список отсортированных заголовков по условию, при этом созданный в п.1 список сортировать не нужно
#
# 3. Записываем при помощи writer = csv.DictWriter(file, fieldnames="Здесь указываемым созданный список по п.2 "), т.е. задаете порядок следования ключей по которым будут записываться столбцы....
#
# 4. Дальше код согласно теории из первого шага




# with open('student_counts.csv', 'r', encoding='utf-8') as file:
#     rows = list(csv.DictReader(file, delimiter=','))
#     colums = [i for i in rows[0]]
#     for obj in rows:



