def numbers_sum(elems):
    '''Принимает список и возвращает сумму его чисел (int, float), игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    total = 0
    for i in elems:
        if type(i) == int or type(i) == float:
            total += i
    return total

print(numbers_sum([1, '2', 3, 4, 'five']))
