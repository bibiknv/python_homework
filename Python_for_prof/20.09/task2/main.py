def get_digits(number: int | float) -> list[int]:
    result_list = []
    for i in str(number):
        if i.isdigit():
            result_list.append(int(i))
    return result_list

print(get_digits(13.909934))




