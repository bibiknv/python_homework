from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    sum_file_size = 0
    sum_compress_size = 0
    info = zip_file.infolist()
    for file in info:
        sum_file_size += file.file_size
        sum_compress_size += file.compress_size
    print('Объем исходных файлов:', sum_file_size, 'байт(а)')
    print('Объем сжатых файлов:', sum_compress_size, 'байт(а)')
