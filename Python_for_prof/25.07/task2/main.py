from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py.py']

from zipfile import ZipFile

with ZipFile('files.zip', mode='w') as zip_file:
    for name in file_names:
        zip_file.write(name)
print(zip_file.namelist())
