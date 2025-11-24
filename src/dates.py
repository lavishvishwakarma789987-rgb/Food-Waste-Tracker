from datetime import datetime, date

def enter_date_today():
    return date.today()

def parse_date_string(date_string):
    try:
        return datetime.strptime(date_string,"%Y-%m-%d").date()
    except ValueError:
        return None
    
    def calculate_days_remaining(expiry_date):
        today = enter_date_today()
        delta = expiry_date - today
        return delta.days