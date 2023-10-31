import string
string.ascii_lowercase
string.ascii_uppercase


def verification(login, password, success, failure):
    pass
d = {0: 'в пароле нет ни одной буквы',
     1: 'в пароле нет ни одной заглавной буквы',
     2: 'в пароле нет ни одной строчной буквы',
     3: 'в пароле нет ни одной цифры'}

def success(login):
    print(f'Привет, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')

verification('timyrik20', 'Beegeek314', success, failure)
