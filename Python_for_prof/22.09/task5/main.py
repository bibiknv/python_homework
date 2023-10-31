def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            m = func(*args, **kwargs)
            return (m, 'Функция выполнилась без ошибок')
        except:
            return (None, 'При вызове функции произошла ошибка')
    return wrapper

sum = exception_decorator(sum)

print(sum(['199', '1', 187]))
