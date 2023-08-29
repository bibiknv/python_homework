# def range_sum(numbers, start, end):
#     new_list_numbers = numbers[start:end + 1]
#     return sum(new_list_numbers)
#
# print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))


def range_sum(numbers, start, end):
    if start == end:
        return numbers[start]
    else:
        return numbers[start] + range_sum(numbers, start + 1, end)
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))
