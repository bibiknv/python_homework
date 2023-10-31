def zip_longest(*args, fill = None):
    max_list = max(args, key = len)
    lst_result = []
    for i in args:
        lst_result.append(i + [fill] * (len(max_list) - len(i))) if len(i) < len(max_list) else lst_result.append(i)
    return [result_tuple for result_tuple in zip(*lst_result)]

data = [[]]
print(zip_longest(*data))
