try:
    file = open(input(), 'r', encoding='utf-8')
    try:
        text = file.read()

    finally:
        file.close()
except FileNotFoundError:
    print('Файл не найден')

