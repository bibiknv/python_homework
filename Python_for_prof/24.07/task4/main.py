from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    count = 0
    for i in info:
        if i.is_dir():
            pass
        else:
            count += 1
    print(count)
