# def rec(num):
#     sum_number = 0
#     if len(str(num)) == 1:
#         sum_number += num
#         return sum_number
#     else:
#         return int(str(num)[:1]) + rec(num % 10)
# print(rec(int(input())))


def num_of_digits(number):
    if number < 10:
        return number % 10
    return number % 10 + num_of_digits(number // 10)

print(num_of_digits(int(input())))
