from functools import partial

def send_email(name, email_address, text):
    pass

to_Timur = partial(send_email, email_address = 'timyrik20@beegeek.ru')


def pretty_print(text, symbol, count):
    print(symbol * count)
    print(text)
    print(symbol * count)

star_pretty_print = partial(send_email, )

star_pretty_print(count=7)

print(star_pretty_print.args)
print(star_pretty_print.keywords)

star_pretty_print.func('Исходная функция', symbol='~', count=20)
