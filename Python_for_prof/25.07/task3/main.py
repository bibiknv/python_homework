import os.path
from zipfile import ZipFile

file_names = ['code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py.py']

with ZipFile('test.zip', mode='a') as zip_file:
    for name in file_names:
        size = os.path.getsize(name)
        if size <= 100:
            zip_file.write(name)

