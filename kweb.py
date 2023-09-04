import yfinance as yf
from common import *

# 定义KWEB ETF的股票代码
symbol = "KWEB"

#symbol = "CHA50CFD"

# 使用yfinance获取KWEB ETF的历史数据
stock_data = yf.Ticker(symbol)

# 获取最近十个交易日的历史数据
historical_data = stock_data.history(period="10d")

# 创建一个空列表来存储涨跌幅数据
percentage_changes = []

# 计算每个交易日的涨跌幅并存储到列表中
for i in range(1, len(historical_data)):
    close_price_yesterday = historical_data['Close'][i - 1]
    close_price_today = historical_data['Close'][i]
    percentage_change = ((close_price_today - close_price_yesterday) / close_price_yesterday) * 100
    percentage_changes.append(percentage_change)

def format_percentage(number):
    if number >= 0:
        formatted_string = f"+{number:.2f}%"
    else:
        formatted_string = f"{number:.2f}%"
    return formatted_string

percentage = format_percentage(percentage_changes[-1])
# 打印涨跌幅数据
print(percentage)


def convert_sign(a):
    if a.startswith('-'):
        return f"KWEB(中概网络股ETF)跌{a}"
    elif a.startswith('+'):
        return f"KWEB(中概网络股ETF)涨{a}"
output= convert_sign(percentage)
append_reminder(output)
#KWEB(中概网络股ETF)涨+3.48%
