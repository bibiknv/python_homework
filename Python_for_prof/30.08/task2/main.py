def to_binary(number):
    string = ''
    if number // 2 <= 1:
        return number % 2
    else:
        return '0' + str(to_binary(number // 2)) if number % 2 == 0 else '1' + str(to_binary(number // 2))


print(to_binary(15))
