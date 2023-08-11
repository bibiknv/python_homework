string = input().split()
dict_result = {}
for i in string:
    value = dict_result.setdefault(len(i), 0)
    dict_result[len(i)] = value + 1

sorted_values = sorted(dict_result.items(), key = lambda x: x[1])
for values in sorted_values:
    print(f"Слов длины {values[0]}: {values[1]}")

# from collections import Counter
#
# words = list(map(len, input().split()))
# count = Counter(words).most_common()
# count_sort = sorted(count, key=lambda x: x[1])
# for length, count in count_sort:
#     print(f'Слов длины {length}: {count}')


