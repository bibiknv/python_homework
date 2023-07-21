import csv
import json
from datetime import datetime

with open('exam_results.csv', encoding='utf-8') as file:
    data = file.read()
    exam_information = [r.split(',') for r in data.splitlines()]


    data = []
    my_set = set()
    sorted_list = []

    for email in exam_information[1:]:
        my_set.add(email[4])
    for mail in sorted(my_set):
        r = list(filter(lambda row: row[4] == mail, exam_information))
        def best_scor(i:r):
            score = i[2]
            d = datetime.strptime(i[3], '%Y-%m-%d %H:%M:%S')
            return (d, score)

        dict_keys = ["name", "surname", "best_score", "date_and_time", "email"]
        max_list_result = max(r, key=best_scor)
        exam_dictionary = {k:v for k,v in zip(dict_keys, max_list_result)}
        exam_dictionary["best_score"]  = int(exam_dictionary["best_score"] )
        data.append(exam_dictionary)

with open('best_scores.json', 'w') as file:
    json.dump(data, file, indent=2)



