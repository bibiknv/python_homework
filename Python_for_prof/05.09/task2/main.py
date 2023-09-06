def zip_longest(*args, fill = None):
    max_list = max(args, key = len)
    lst_result = []
    for i in args:
        lst_result.append(i + [fill] * (len(max_list) - len(i))) if len(i) < len(max_list) else lst_result.append(i)
    return [result_tuple for result_tuple in zip(*lst_result)]

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
print(zip_longest(*data))
