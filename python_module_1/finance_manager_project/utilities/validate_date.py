#this function validates a date string in MM/DD/YYYY format and returns a datetime object or an error message if invalid or in the future.
from datetime import datetime
def validate_date(date_str):
    try:
        date = datetime.strptime(date_str, "%m/%d/%Y")
        if date > datetime.now():
            return "Date cannot be in the future."
        return date
    except ValueError:
        return "Date format must be MM/DD/YYYY."
