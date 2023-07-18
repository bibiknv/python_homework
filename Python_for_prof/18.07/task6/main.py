
import json
import sys

MODE = 'PROD'

if MODE=='TEST':
    fin = open('test.txt')
    fout = open('test_out.txt', 'w')
else:
    fin = sys.stdin
    fout = sys.stdout


json_data = json.loads(data)
print(json_data)
