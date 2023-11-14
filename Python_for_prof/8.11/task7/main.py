def count_iterable(iterable):
    even_numbers = (num for num in iterable)
    sum_list = 0
    for i in even_numbers:
        sum_list += 1
    return sum_list


data = tuple(range(432, 3845, 17))

print(count_iterable(data))
