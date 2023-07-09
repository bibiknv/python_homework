
import csv
def csv_columns(filename):
    filename = input()
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        rows = csv.DictReader(file, delimiter=',')
        for row in rows:
            print(row)


