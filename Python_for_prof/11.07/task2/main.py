
import csv

with open('prices.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    result_list = []

    res_dict = {}
    for i, row in enumerate(reader):
        for key, value in row.items():
            if key != 'Магазин':
                res_dict.setdefault(row['Магазин'], []).append((key, value))
    #         if key == 'Магазин':
    #             new_dict[value] = []
    print(res_dict)


    #for row in reader:
    #     result_list.append(row)

# with open('prices_result.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=file_names, delimiter=';')
#     writer.writeheader()
#     for row_new in result_list:
#         writer.writerow(row_new)
