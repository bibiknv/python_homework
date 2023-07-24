from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    filelist = zip_file.infolist()
    t = ((f.filename, f.compress_size/f.file_size) for f in filelist
         if f.file_size != 0)
    print(min(t, key=lambda x: x[1])[0].split("/")[-1])
