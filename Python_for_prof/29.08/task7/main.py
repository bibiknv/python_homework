def is_power(number):
    if number < 2:
        if number == 1:
            return True
        else:
            return False
    else:
        return is_power(number / 2)

print(is_power(15))
