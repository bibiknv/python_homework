def my_pow(number):
    list_of_numbers = []
    for count, value in enumerate(str(number), 1):
        list_of_numbers.append((count, int(value)))
    list_of_numbers = sorted(list_of_numbers, key= lambda x: x[1])
    sum_numbers = 0
    for tuple_number in list_of_numbers:
        sum_numbers += pow(tuple_number[1], tuple_number[0])
    return sum_numbers

print(my_pow(139))
