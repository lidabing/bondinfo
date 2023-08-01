from datetime import datetime

def is_same_day(date_string):
    try:
        input_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        today = datetime.now().date()
        return input_date == today
    except ValueError:
        return False

# Usage example
date_to_check = "2023-08-1"
result = is_same_day(date_to_check)
print(result)  # Output: True (if today is August 4, 2023)