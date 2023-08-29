# def main(x):
#     return len(str(x))

def main(number):
    if number < 10:
        return 1
    return 1 + main(number // 10)

print(main(int(input())))
