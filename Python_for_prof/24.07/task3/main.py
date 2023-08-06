from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    with zip_file.open('test.py/Разные файлы/astros.json') as file:
        print(file.read().decode('utf-8'))
