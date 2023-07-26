from zipfile import ZipFile
import json

with ZipFile('data.zip') as z:
    for item in z.infolist():
        if item.filename.split('.')[-1] == 'json':
            name = item.filename
            def is_correct_json(name):
                try:
                    print(json.loads(name))
                except ValueError:
                    print('false')
            print(is_correct_json(name))
