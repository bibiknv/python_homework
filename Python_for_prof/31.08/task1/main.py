def linear(nested_lists):
    new_list = []
    for i in nested_lists:
        if type(i) == int:
            new_list.append(i)
        if type(i) == list:
            new_list += linear(i)
    return new_list

my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))

