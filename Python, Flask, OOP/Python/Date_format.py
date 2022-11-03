import datetime
import locale
def format_date(day, month, year):
    if month > 12:
        return None
    elif month < 1:
        return None
    elif day > 31:
        return None
    elif month == 2 and day > 28:
        return None
    else:
        locale.setlocale(locale.LC_ALL, '')
        return datetime.date(year, month, day).strftime("%d %B %Y")
print(format_date(28, 2, 2022))


def monthss(day, month, year):
    months_names = {
        1: 'stycznia',
        2: 'lutego',
        3: 'marca',
        4: 'kwietnia',
        5: 'maja',
        6: 'czerwca',
        7: 'lipca',
        8: 'sierpnia',
        9: 'wrzesnia',
        10: 'października',
        11: 'listopada',
        12: 'grudnia'
    }
    months_days = {
        1: 30,
        2: 25,
        3: 31,
        4: 24,
        5: 'maja',
        6: 'czerwca',
        7: 'lipca',
        8: 'sierpnia',
        9: 'wrzesnia',
        10: 'października',
        11: 'listopada',
        12: 'grudnia'
    }

    if day not in range(months_days[day]):
        return None
    if month > 12 or month < 1:
        return None
    return f"{day} {months_names[month]} {year}"


print(monthss(2, 12, 1999))