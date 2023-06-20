#下修重算起始日即将到期的转载
#价格在110以内
import requests
import re
import json
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font, Color
from openpyxl.styles import Alignment
from openpyxl.styles import PatternFill
from datetime import datetime, timedelta

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        data = json.loads(content)
    return data

request_headers_file = 'request_headers.txt'
# 读取文件内容
request_headers = read_file(request_headers_file)

def fetch_all_convertible_bonds():
    url = "https://www.jisilu.cn/webapi/cb/adjust/"

    # 发起 HTTP GET 请求
    response = requests.get(url,headers=request_headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return []
    
def is_number(value):
    return isinstance(value, (int, float, complex))

def is_integer(variable):
    if isinstance(variable, int):
        return True
    elif isinstance(variable, str):
        return variable.isdigit()
    else:
        return False
    
def find_property_value(data, bond_id, property_name):
    for bond_data in data:
        if bond_data["bond_id"] == bond_id:
            return bond_data.get(property_name)
    return None

def find_content_by_id(target_id):
    with open('backup.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith(target_id):
                content = line.split('|', 1)[-1].strip()
                return content
    return None

def is_within_one_month(date_str):
    if date_str is None:
        return False

    # 将时间字符串转换为datetime对象
    date = datetime.strptime(date_str, "%Y-%m-%d")

    # 获取当前日期
    current_date = datetime.now().date()

    # 计算未来一个月的日期
    one_month_later = current_date + timedelta(days=30)

    # 判断给定的日期是否在当前日期和未来一个月之间
    if current_date <= date.date() <= one_month_later:
        return True
    else:
        return False
    

def is_within_10_days(date_str):
    if date_str is None:
        return False

    # 将时间字符串转换为datetime对象
    date = datetime.strptime(date_str, "%Y-%m-%d")

    # 获取当前日期
    current_date = datetime.now().date()

    # 计算未来一个月的日期
    one_month_later = current_date + timedelta(days=10)

    # 判断给定的日期是否在当前日期和未来一个月之间
    if current_date <= date.date() <= one_month_later:
        return True
    else:
        return False
    
# 抓取所有转债数据
all_bonds_data = fetch_all_convertible_bonds()

excel_header =   ['转债名称','转债代码','收盘价','溢价率','下修重算日','备注']
# 创建字体对象
title_font = Font(name='微软雅黑')
header_font = Font(name='微软雅黑',bold=False)
backup_font = Font(name='微软雅黑',size=9)
title_height = 30
header_fill = PatternFill(fill_type='solid', fgColor='f2f2f2')

# 创建一个新的工作簿
workbook = Workbook()
sheet = workbook.active
sheet.merge_cells('A1:F1')
sheet['A1'] = '下修重算日即将到期转债'
sheet['A1'].font = title_font
sheet.row_dimensions[1].height = 22
sheet.column_dimensions['A'].width = 12
sheet.column_dimensions['E'].width = 14
sheet.column_dimensions['F'].width = 14
sheet.column_dimensions['G'].width = 20

sheet.append(excel_header)
for cell in sheet[2]:
        cell.fill = header_fill
        cell.font = header_font

index = 2
for bond_data in all_bonds_data:
    bond_code = bond_data["bond_id"]
    readjust_dt = find_property_value(all_bonds_data,bond_code, 'readjust_dt')
    #print(readjust_dt)
    if is_within_one_month(readjust_dt):
        bond_nm = find_property_value(all_bonds_data,bond_code, 'bond_nm')
        bond_id = find_property_value(all_bonds_data,bond_code, 'bond_id')
        premium_rt = find_property_value(all_bonds_data,bond_code, 'premium_rt')
        premium_rt = premium_rt/100.00
        price = find_property_value(all_bonds_data,bond_code, 'price')
        bond_backup = find_content_by_id(bond_id)
        item = [bond_nm,int(bond_id),price,premium_rt,readjust_dt,bond_backup]
        index = index + 1
        sheet.append(item)
        #如果十天内就要满足下修条件了，那么标红
        red_font  = Font(color='FF4500')  
        if is_within_10_days(readjust_dt):
            pos = 'E'+str(index)
            sheet[pos].font = red_font


#设置百分比
for cell in sheet['D']:
    pos = 'D'+str(cell.row)
    print(sheet[pos].value)
    if(is_number(sheet[pos].value)):
        cell.number_format = '0.00%'

yahei_font  = Font(name='微软雅黑',bold=False)
for cell in sheet['A']:
    pos = 'A'+str(cell.row)
    #print(sheet[pos].value)
    #if(is_integer(sheet[pos].value)):
    cell.font = yahei_font

blue_font  = Font(color='0000FF')  # 蓝色字体
for cell in sheet['B']:
    pos = 'B'+str(cell.row)
    print(sheet[pos].value)
    if(is_integer(sheet[pos].value)):
        cell.font = blue_font

#设置备注文字样式
for cell in sheet['F']:
    pos = 'F'+str(cell.row)
    sheet[pos].font = backup_font
    #sheet[pos].alignment = Alignment(wrap_text=True)

#设置居中
# TOdo自动调整宽度
for row in sheet.iter_rows(min_row=1, max_row=44, min_col=1, max_col=6):
    for cell in row:
        cell.alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)

readjust_dt_list_file = datetime.now().strftime("下修重算日即将到期转债-%Y年%m月%d日.xlsx")
workbook.save(readjust_dt_list_file)
    