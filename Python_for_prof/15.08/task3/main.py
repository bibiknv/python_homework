a = input()
b = input()
numbers = []

for i in range(a, b):
    if i // 7 == 0:
        numbers = numbers.append(i)

print(numbers)
