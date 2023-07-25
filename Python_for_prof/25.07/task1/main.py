from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    result_list = []
    info = zip_file.infolist()
    for file in info:
        if not file.is_dir():
            f = datetime(*file.date_time)
            filename = file.filename[file.filename.rfind("/") + 1:]
            result_list.append((filename, f, file.file_size, file.compress_size))
    for tuple_file in sorted(result_list, key = lambda x: x[0]):
        print(tuple_file[0])
        print('  Дата модификации файла:', tuple_file[1].strftime('%Y-%m-%d %H:%M:%S'))
        print('  Объем исходного файла:', tuple_file[2], 'байт(а)')
        print('  Объем сжатого файла:', tuple_file[3], 'байт(а)')
        print(' ')


