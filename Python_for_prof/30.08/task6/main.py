
def recursive_sum(nested_lists):
    total = 0
    for i in nested_lists:
        if type(i) == int:
            total += i
        if type(i) == list:
            total += recursive_sum(i)
    return total


my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))
