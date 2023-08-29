def number_of_frogs(year, f_k = 77):
    if year == 1:
        return f_k
    else:
        return (number_of_frogs(year - 1) - 30) * 3


print(number_of_frogs(int(input())))

