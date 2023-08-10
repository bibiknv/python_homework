from collections import Counter

string = input().lower().split()
letter = sorted(Counter(string).most_common()[::-1], key = lambda x: x[0])

list_result = []
for i in letter:
    if i[1] == 1:
        list_result.append(i[0])
for i in list_result:
    print(i, end = ', ')


