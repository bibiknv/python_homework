def is_prime(number):
    sum_list = []
    if number == 1:
        return False
    for i in range(1, number + 1):
        if number % i == 0:
            sum_list.append(i)
    if (sum(sum_list) - 1) == number:
        return True
    else:
        return False

print(is_prime(7))
