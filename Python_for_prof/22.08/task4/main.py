from calendar import day_name
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
days = {i: d for i, d in enumerate(map(str.title, day_name), 1)}
