
import datetime
def years_days(year):
    today = datetime.date(year, 1, 1)
    day = datetime.date(today.year, today.month, 1)

    single_day = datetime.timedelta(days = 1)

    while day.year == today.year:
        yield day
        day += single_day


dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))


