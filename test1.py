from datetime import datetime, timedelta

def is_over_three_months(date_string):
    current_time = datetime.now()
    if date_string is None:
        return False

    supported_formats = ["%Y/%m/%d", "%Y-%m-%d"]

    for date_format in supported_formats:
        try:
            input_time = datetime.strptime(date_string, date_format)
            three_months_later = current_time + timedelta(days=90)
            return input_time > three_months_later
        except ValueError:
            continue

    return False

# 调用函数进行测试
date1 = "2099/12/31"
date2 = "2023-06-26"

print(is_over_three_months(date1))  # True，时间超过三个月
print(is_over_three_months(date2))  # False，时间未超过三个月
