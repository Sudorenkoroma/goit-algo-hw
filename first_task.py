from datetime import datetime


def get_days_from_today(date):
    try:
        datetime_object = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        date_difference = today - datetime_object
        return date_difference.days
    except ValueError:
        return "Неправильний формат дати."




current_date = datetime.today().strftime('%Y-%m-%d')
user_date = input("Введіть дату в форматі 'РРРР-ММ-ДД': ")
result = get_days_from_today(user_date)

print(f"Сьогодні {current_date}, кількість днів до {user_date}: {result}")