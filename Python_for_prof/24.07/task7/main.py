from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    result_list = []
    dt_string = '2021-11-30 14:22:00'
    dt_object1 = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
    info = zip_file.infolist()
    for file in info:
        if not file.is_dir():
            if datetime(*file.date_time) >= dt_object1:
                filename = file.filename[file.filename.rfind("/") + 1:]
                result_list.append(filename)
    for name in sorted(result_list):
        print(name)


