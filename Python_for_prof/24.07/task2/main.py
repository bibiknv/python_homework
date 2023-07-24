from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    info = zip_file.infolist()
    print(info[6].file_size)
    print(info[6].compress_size)
    print(info[6].filename)
    print(info[6].date_time)
