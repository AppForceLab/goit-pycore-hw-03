from datetime import datetime

def get_days_from_today(date):

    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")
    
    current_date = datetime.today().date()
    difference = current_date - given_date

    return difference.days
