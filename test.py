from datetime import datetime, date

def compare_to_today(date_str):
    # 将日期字符串转换为 datetime 对象
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')

    # 获取当前日期
    today = date.today()

    if date_obj.date() > today:
        return "今天之后"
    elif date_obj.date() < today:
        return "今天之前"
    else:
        return "今天"

# 测试示例
date1 = '2023-06-11'
date2 = '2023-06-12'
date3 = '2023-06-14'

result1 = compare_to_today(date1)
result2 = compare_to_today(date2)
result3 = compare_to_today(date3)

print(result1)  # 今天之后
print(result2)  # 今天之前
print(result3)  # 今天
