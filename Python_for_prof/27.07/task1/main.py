import pickle
import sys

func_file_name, *args = [line.strip() for line in sys.stdin]

with open(func_file_name, 'rb') as func_file:
    func_name = pickle.load(func_file)
print(func_name(*args))
