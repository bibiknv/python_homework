

import pickle

def calc_control_sum(obj):
    int_list = list(filter(lambda x: isinstance(x, int), obj))
    if isinstance(obj, list):
        return min(int_list, default=0)*max(int_list, default=0)
    elif isinstance(obj, dict):
        return min(int_list, default=0)+max(int_list, default=0)



with open(input(), 'rb') as file:
    obj = pickle.load(file)
    control_sum = calc_control_sum(obj)
    number = int(input())
    if number == control_sum:
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')
