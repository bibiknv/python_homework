def sandwich(func):          # определяем декоратор
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        a = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return a
    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))

add_ingredients(['томат', 'салат', 'сыр', 'бекон'])



