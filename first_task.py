from datetime import datetime


def get_days_from_today(date):
    today = datetime.today()
    try:
        datetime_object = datetime.strptime(date, '%Y-%m-%d')
        date_difference = (today - datetime_object).days
        return date_difference
    except ValueError:
        return "Неправильний формат дати"


result = get_days_from_today("2021-10-09")

print(f"Кількість днів до 2021-10-09: {result} днів")