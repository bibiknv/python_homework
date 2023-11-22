
def nonempty_lines(file):
    f = open(file, "r")
    print(f.readline())

lines = nonempty_lines('file1.txt')

print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))

