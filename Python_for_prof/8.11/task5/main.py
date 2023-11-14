from datetime import date, timedelta

def dates(start, count = None):
    max_date = date.toordinal(date.max)
    if count is not None:
        max_date = min(date.toordinal(start) + count - 1, max_date)

    d = date.toordinal(start)
    while d <= max_date:
        yield date.fromordinal(d)
        d = d + 1
    return


generator = dates(date(2022, 3, 8), 5)

print(*generator)

