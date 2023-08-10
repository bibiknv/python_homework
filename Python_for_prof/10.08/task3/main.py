from collections import Counter

string = Counter(input().lower().split())
most_common_elem = string.most_common()
print(max(most_common_elem, key = lambda x:x[1])[0])
