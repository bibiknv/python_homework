from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    info = zip_file.infolist()
    count = 1
    for name in info:
        list_name = name.filename[:-1:].split('/')
        if len(list_name) == count:
            print(name.filename[:-1])
        if len(list_name) == 2:
            count = 2
            if name.filename[-1:] == '/':
                print('  ', name.filename[:-1])
            else:
                print('  ', name.filename)
    def convert_bytes(size):
        if size < 1000:
            return f'{size} B'
        elif 1000 <= size < 1000000:
            return f'{round(size / 1024)} KB'
        elif 1000000 <= size < 1000000000:
            return f'{round(size / 1048576)} MB'
        else:
            return f'{round(size / 1073741824)} GB'
