
import json
import sys

MODE = 'TEST'

if MODE=='TEST':
    fin = open('test.txt')
    fout = open('test_out.txt', 'w')
else:
    fin = sys.stdin
    fout = sys.stdout

with fin, fout:
    dict_data = json.load(fin )
    for key, value in dict_data.items():
        if type(value) == list:
            print(key, ': ', ", ".join(map(str, value)), sep = '')
        else:
            print(key, ': ', value, sep = '')

