import csv

with open('student_counts.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')

    file_names = reader.fieldnames
    file_names_sorted = sorted(file_names[1:], key=lambda x: (len(x), x))
    first_string_names = file_names[:1] + file_names_sorted

    result_list = []
    for row in reader:
        result_list.append(row)


with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=first_string_names, delimiter=',')
    writer.writeheader()
    for row_new in result_list:
        writer.writerow(row_new)

