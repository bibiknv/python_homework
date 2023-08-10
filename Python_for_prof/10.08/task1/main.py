from collections import Counter

string = input().lower().split()
word = Counter(string).most_common(1)[0][0]
print(word)
