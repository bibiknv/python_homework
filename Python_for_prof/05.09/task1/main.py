names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

new_list = []
for info in zip(names, box_offices, budgets):
    new_list.append((info[0], info[1] - info[2]))
for result_info in sorted(new_list, key = lambda x: x[0]):
    print("{}: {}$".format(result_info[0], result_info[1]))


