import requests
import json

from enum import Enum
import re

class RedeemStatus(Enum):
    NOT_REDEEMED = 1
    REDEEM_ANNOUNCED = 2
    NOT_REDEEM_ANNOUNCED = 3
    EXPIRY_BOND = 4  #即将到期转债

def get_redeem_status(string):
    if "不强赎" in string:
        return RedeemStatus.NOT_REDEEMED
    elif "强赎" in string:
        return RedeemStatus.REDEEM_ANNOUNCED
    elif "到期" in string:
        return RedeemStatus.EXPIRY_BOND
    else:
        return RedeemStatus.NOT_REDEEM_ANNOUNCED #还没有达到强赎条件


def separate_numbers(string):
    numbers = re.findall(r'\d+', string)
    return numbers


url = "https://www.jisilu.cn/webapi/cb/redeem/"

# 发送GET请求到URL
response = requests.get(url)

#转债代码 转债名称 收盘价 溢价率 剩余规模 达标天数
#转债代码  转债名称 收盘价 溢价率 最后交易日 最后转股日
#转债代码  转债名称 收盘价 溢价率 最后交易日 最后转股日

# 检查请求是否成功
if response.status_code == 200:
    # 解析JSON响应
    json_data = response.json()

    # 访问解析后的数据
 
    for item in json_data['data']:
        redeem_status = item["redeem_status"]
        status = get_redeem_status(redeem_status)
        if status == RedeemStatus.NOT_REDEEM_ANNOUNCED:
            
            numbers = separate_numbers(redeem_status)
            compliance_days = int(numbers[0])#numbers[1]-numbers[0]
            if compliance_days>5:
                print("即将达到强赎条件")
                print("债券名称:", item["bond_nm"])
                print("收盘价:", item["redeem_price"])
                print("溢价率:", item["redeem_price"])
                print("剩余规模:", item["curr_iss_amt"])
                print("达标天数:", numbers[0])
                print("-----------------------------")              
        elif status == RedeemStatus.REDEEM_ANNOUNCED:
            print("发出强赎公告")
            print("债券名称:", item["bond_nm"])
            print("收盘价:", item["redeem_price"])
            print("溢价率:", item["redeem_price"])
            print("最后交易日:", item["delist_dt"])
            print("最后转股日:", item["last_convert_dt"])
            print("-----------------------------")
        elif status == RedeemStatus.EXPIRY_BOND:
            print("转债即将到期")
            print("债券名称:", item["bond_nm"])
            print("收盘价:", item["redeem_price"])
            print("溢价率:", item["redeem_price"])
            print("最后交易日:", item["delist_dt"])
            print("最后转股日:", item["last_convert_dt"])

        #print("债券ID:", item["bond_id"])
        #print("债券名称:", item["bond_nm"])
        #print("赎回日期:", item["redeem_dt"])
        #print("强制赎回价格:", item["force_redeem_price"])
        #print("强制赎回价格:", item["force_redeem_price"])
        #print("-----------------------------")
else:
    print("请求失败，状态码为:", response.status_code)
