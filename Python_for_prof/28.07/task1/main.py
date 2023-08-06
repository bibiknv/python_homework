import string
alphabet = input()

my_dict = {string.ascii_lowercase[i]: alphabet[i] for i in range(len(alphabet))}
line = input().lower()
m = line.maketrans(my_dict)
print(line.translate(m))

