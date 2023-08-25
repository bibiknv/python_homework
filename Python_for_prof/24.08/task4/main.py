

def print_digits(numbers: str) -> str:
    print(str(numbers)[-1])
    active = True
    while active:
        if len(str(numbers)) <= 0:
            break
        else:
            print_digits(str(numbers)[:-1])


print_digits(12345)
