import csv
from datetime import datetime
import time

with open('meetings.csv', encoding='utf-8') as file:
    data = file.read()
    rows = [r.split(',') for r in data.splitlines()]
    first_row = rows[0]
    del rows[0]
    date_pattern, time_pattern = '%d.%m.%Y', '%H:%M'
    expensive = sorted(rows, key=lambda item: (datetime.strptime(item[2], date_pattern), time.strptime(item[3], time_pattern)))

from collections import namedtuple

Person = namedtuple('Person', first_row)
for i in expensive:
    person_info = Person._make(i)
    print(person_info.surname, person_info.name)



