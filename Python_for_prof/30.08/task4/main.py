def get_all_str(data):
    if type(data) == str:
         print(data, end = ' ')
    if type(data) == list:
        for i in data:
            get_all_str(i)

numbers = ['1', ['2', '3', ['4'], ['5', ['6', '7']]]]

get_all_str(numbers)

