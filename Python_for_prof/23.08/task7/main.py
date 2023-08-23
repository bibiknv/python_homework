import sys

def get_stat(numbers):
    new_numbers = numbers[::-1]
    for number in new_numbers:
        print(number)

data = [int(line.strip()) for line in sys.stdin]

get_stat(data)


# def rec():
#     n = input()
#     if n != '0':
#         rec()
#     print(n)
#
# rec()
