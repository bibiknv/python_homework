from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    result_list = []
    for file in info:
        if not file.is_dir():
            file_size_f = file.file_size
            compress_size_f = file.compress_size
            persent_zip = 100 - (compress_size_f /file_size_f * 100)
            filename = file.filename[file.filename.rfind("/") + 1:]
            result_list.append((filename, persent_zip))
    result_list.sort(key=lambda x: x[1], reverse = True)
    print(result_list[0][0])
    #
    # # 100 - (Vc / Vo * 100)

