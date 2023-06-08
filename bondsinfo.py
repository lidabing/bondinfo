import requests
import csv
from datetime import datetime


headers = {"cookie": 'kbzw__Session=elbqk07dap4k0uqf4o5k6retg2; Hm_lvt_164fe01b1433a19b507595a43bf58262=1685855555; kbz_newcookie=1; kbzw__user_login=7Obd08_P1ebax9aXYOkFRiQHWB34VekdmrCW6c3q1e3Q6dvR1YzRl6iwrsqyzqmW18Sr2KjalaOXqbGooNrP3Mitltqpq5mcndbd3dPGpKWplKiXmLKgubXOvp-qq6GupKyXrZiomK6ltrG_0aTC2PPV487XkKylo5iJx8ri3eTg7IzFtpaSp6Wjs4HHyuKvqaSZ5K2Wn4G45-PkxsfG1sTe3aihqpmklK2Xm8OpxK7ApZXV4tfcgr3G2uLioYGzyebo4s6onaiVpJGlp6GogcPC2trn0qihqpmklK0.; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1685884076'}

def fetch_all_convertible_bonds():
    url = "https://www.jisilu.cn/webapi/cb/adjust/"

    # 发起 HTTP GET 请求
    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return []

def find_property_value(data, bond_id, property_name):
    for bond_data in data:
        if bond_data["bond_id"] == bond_id:
            return bond_data.get(property_name)
    return None

def find_backup_by_bond_id(bond_id, backup_data):
    for item in backup_data:
        if item['bond_id'] == bond_id:
            return item['backup']
    return None

# 抓取所有转债数据
all_bonds_data = fetch_all_convertible_bonds()

bond_code_array = ['127033', '127075', '110067', '128021', '128119','123103','123144','113641','128023','127005','128062','123128','123096','113600','123049','118009','123087','127082','123119','123145','128117','113569','123002','113017','127049','123010','123153','123061','128123','118034','128039','113573','113066']

current_date = datetime.now()
date_string = current_date.strftime("%Y年%m月%d日.csv")
csv_file = date_string


heaser =   ['转债名称','转债代码','转债价格','转债溢价率','下修日计数','下修重算起始日','备注']
backup = [{"bond_id":'123128',"backup":'下修或可低于净资产'},
          {"bond_id":'127075',"backup":'[打电话]说不下修'},
          {"bond_id":'127075',"backup":'[打电话]说不下修'},
          {"bond_id":'123103',"backup":'[打电话]说不下修'},
          {"bond_id":'123096',"backup":'公司财务不健康，不要上头'},
          {"bond_id":'128021',"backup":' 只有半年时间了，谨慎一点'}
          ]

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(heaser)
#转债名称 bond_nm
#转债代码 bond_id
#转债价格 price
#转债溢价率 premium_rt
#下修天计数 adjust_count
#下修重算起始日 readjust_dt
for bond_code in bond_code_array:
    bond_nm = find_property_value(all_bonds_data,bond_code, 'bond_nm')
    bond_id = find_property_value(all_bonds_data,bond_code, 'bond_id')
    price = find_property_value(all_bonds_data,bond_code, 'price')
    premium_rt = find_property_value(all_bonds_data,bond_code, 'premium_rt')
    adjust_count = find_property_value(all_bonds_data,bond_code, 'adjust_count')
    readjust_dt = find_property_value(all_bonds_data,bond_code, 'readjust_dt')
    bond_backup = find_backup_by_bond_id(bond_id,backup)
    item = [bond_nm,bond_id,price,premium_rt,adjust_count,readjust_dt,bond_backup]
    with open(csv_file, 'a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(item)
    #table_data.append(item)



#with open(csv_file, 'a', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerow(table_data)


# 输入转债代码
#bond_code = input("请输入转债代码: ")
# 查找指定转债数据
#bond_data = find_property_value(all_bonds_data,bond_code, 'stock_nm')

# 打印结果
#if bond_data:
#    print(f"转债 {bond_code} 的数据:")
#    print(bond_data)
#else:
#    print(f"未找到转债 {bond_code} 的数据")
