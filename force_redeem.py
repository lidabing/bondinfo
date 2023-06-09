import requests
import json

from enum import Enum
import re

class RedeemStatus(Enum):
    NOT_REDEEMED = 1
    REDEEM_ANNOUNCED = 2
    NOT_REDEEM_ANNOUNCED = 3

def get_redeem_status(string):
    if "强赎" in string:
        return RedeemStatus.REDEEM_ANNOUNCED
    elif "不强赎" in string:
        return RedeemStatus.NOT_REDEEM_ANNOUNCED
    else:
        return RedeemStatus.NOT_REDEEMED


def separate_numbers(string):
    numbers = re.findall(r'\d+', string)
    return numbers


url = "https://www.jisilu.cn/webapi/cb/redeem/"

# 发送GET请求到URL
response = requests.get(url)

#转债代码  转债名称 收盘价 溢价率 最后交易日 最后转股日
#转债代码 转债名称 收盘价 溢价率 剩余规模 达标天数
# 检查请求是否成功
if response.status_code == 200:
    # 解析JSON响应
    json_data = response.json()

    # 访问解析后的数据
 
    for item in json_data['data']:
        redeem_status = item["redeem_status"]
        status = get_redeem_status(redeem_status)
        if status == RedeemStatus.NOT_REDEEMED:
            print("还未满足强赎条件")
        elif status == RedeemStatus.REDEEM_ANNOUNCED:
            print("发出强赎公告")
        #print("债券ID:", item["bond_id"])
        print("债券名称:", item["bond_nm"])
        #print("赎回日期:", item["redeem_dt"])
        print("强制赎回价格:", item["force_redeem_price"])
        print("强制赎回价格:", item["force_redeem_price"])
        print("-----------------------------")
else:
    print("请求失败，状态码为:", response.status_code)
