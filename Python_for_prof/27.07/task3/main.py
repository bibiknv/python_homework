import pickle

file_name = input()
number = int(input())

with open(file_name, 'rb') as file:
    obj = pickle.load(file)
