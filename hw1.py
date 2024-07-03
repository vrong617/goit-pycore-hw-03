from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        difference = (current_date - input_date).days
        return difference
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."