def custom_isinstance(objects, typeinfo):
    sum_numbers = 0
    for i in objects:
        if isinstance(i, typeinfo):
            sum_numbers += 1
        else:
            pass
    return sum_numbers

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, (int, float)))
