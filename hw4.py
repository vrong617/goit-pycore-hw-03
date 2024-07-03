from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime(today.year, birthday_date.month, birthday_date.day).date()
        
        if birthday_this_year < today:
            birthday_this_year = datetime(today.year + 1, birthday_date.month, birthday_date.day).date()

        days_until_birthday = (birthday_this_year - today).days
        
        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5:
                days_until_birthday += (7 - birthday_this_year.weekday()) + 1
                birthday_this_year = today + timedelta(days=days_until_birthday)
            
            congratulation_date = birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date})
    
    return upcoming_birthdays
