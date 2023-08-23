# def print_numbers(start, end):
#     def rec(num):
#         if num <= end:
#             print(num)
#             rec(num + 1)
#     rec(start)


def print_numbers(start, end):
    def rec(num):
        if num <= 100:
            print(num)
            rec(num + 1)
    rec(start)

print_numbers(1, 100)
