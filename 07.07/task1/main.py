import csv

sorting_col = int(input()) - 1
with open('deniro.csv', 'r', encoding='utf-8') as file:
    data = file.read()
    table = [r.split(',') for r in data.splitlines()]
    table.sort(key=lambda x: int(x[sorting_col]) if x[sorting_col].isdigit() else x[sorting_col])
    for i in table:
        print(*i, sep=',')
