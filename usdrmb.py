import requests
import pandas as pd
from common import *

# Alpha Vantage API密钥，请替换为你自己的密钥
api_key = "HHLFT3WW151AQ4XM"

def get_historical_exchange_rates():
    try:
        # 使用Alpha Vantage API获取历史汇率数据
        url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=USD&to_symbol=CNY&apikey={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            
            if "Time Series FX (Daily)" in data:
                # 将汇率数据转换为DataFrame
                exchange_rate_data = data["Time Series FX (Daily)"]
                df = pd.DataFrame(exchange_rate_data).T
                df.index = pd.to_datetime(df.index)
                df.columns = ["open", "high", "low", "close"]
                
                # 计算涨跌幅
                df["change"] = df["close"].astype(float).pct_change() * 100
                
                # 获取昨日涨跌幅
                yesterday_change = df["change"].iloc[1]
                
                # 获取当前汇率
                current_exchange_rate = df["close"].iloc[1]
                
                return yesterday_change, current_exchange_rate
            else:
                print("找不到历史汇率数据")
                return None
        else:
            print(f"请求失败，状态码：{response.status_code}")
            return None
    except Exception as e:
        print(f"发生错误：{str(e)}")
        return None

def convert_sign(a, b):
    if b.startswith('-'):
        return f"隔夜人民币兑美元汇率报{a}(RMB涨+{b[1:]}%)"
    elif b.startswith('+'):
        return f"隔夜人民币兑美元汇率报{a}(RMB跌-{b[1:]}%)"
    else:
        return f"隔夜人民币兑美元汇率报{a}(RMB{b}%)"

if __name__ == "__main__":
    result = get_historical_exchange_rates()
    if result is not None:
        yesterday_change, current_exchange_rate = result
        f"隔夜人民币兑美元汇率报{current_exchange_rate}(RMB涨+0.31)"

        #print(f"昨日涨跌幅：{yesterday_change:.2f}%")
        print(f"当前汇率：{current_exchange_rate}") 
        output= convert_sign(current_exchange_rate,f'{yesterday_change:.2f}')
        append_reminder(output)