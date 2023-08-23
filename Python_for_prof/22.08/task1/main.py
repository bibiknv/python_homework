try:
    file = open('data.txt', encoding='utf-8')
    try:
        text = file.read()
    except:
        print('При чтении из файла произошла ошибка!')
    else:
        print('Чтение из файла прошло успешно!')
    finally:
        file.close()
except FileNotFoundError:
    print('Файл с указанным именем не найден!')
