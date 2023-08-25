def bee(number = 16):
    num = 16
    for i in range(1, 5):
        new_string = (str(i) * number)
        print(new_string.center(num))
        number = number - 4
        num -= 1

def new_bee(new_number = 4):
    num_1 = 13
    for j in range(3, 0, -1):
        new_string_1 = (str(j) * (new_number + 4))
        print(new_string_1.center(num_1))
        new_number = new_number + 4
        num_1 += 1

bee()
new_bee()
