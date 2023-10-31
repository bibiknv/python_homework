def power(degree):
    def square(x):
        return x ** degree
    return square
print(power(3)(3))
# square = power(2)
# print(square(5))
