some_input = input()

expression1 = "some_input[-1]"
expression2 = "some_input[0]"
expression3 = "len(some_input)"

if type(some_input) == list:
    print(eval(expression1))
if type(some_input) == tuple:
    print(eval(expression2))
if type(some_input) == set:
    print(eval(expression3))

