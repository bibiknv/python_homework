import csv
import random
from collections import namedtuple

Point = namedtuple('Point', ('x', 'y'))

with open('points.csv', mode='w', encoding='utf-8') as file_out:
    data = [[random.randint(0, 100), random.randint(0, 100)] for _ in range(20)]
    writer = csv.writer(file_out)
    writer.writerows(data)

with open('points.csv', mode='r', encoding='utf-8') as file_in:
    rows = csv.reader(file_in)
    points = []
    for row in rows:
        x, y = row
        points.append((Point(int(x), int(y))))
print(points)
