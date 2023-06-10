import requests
import csv
import re
import json
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font, Color
from openpyxl.styles import Alignment
from openpyxl.styles import PatternFill

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        data = json.loads(content)
    return data

request_headers_file = 'request_headers.txt'
# 读取文件内容
request_headers = read_file(request_headers_file)

# 输出文件内容
print(request_headers)

def find_content_by_id(target_id):
    with open('backup.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith(target_id):
                content = line.split('|', 1)[-1].strip()
                return content
    return None


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

#辅助函数
def parse_adjust_string(s):
    if(s == None):
        return None
    pattern = r"([\d]+)/([\d]+) \| ([\d]+)"
    match_obj = re.match(pattern, s)
    if match_obj:
        num1, num2, num3 = map(int, match_obj.groups())
        return num1, num2, num3
    else:
        return None

def is_number(value):
    return isinstance(value, (int, float, complex))

def is_integer(variable):
    if isinstance(variable, int):
        return True
    elif isinstance(variable, str):
        return variable.isdigit()
    else:
        return False

# 抓取所有转债数据
all_bonds_data = fetch_all_convertible_bonds()


excel_header =   ['转债名称','转债代码','收盘价','溢价率','下修日计数','下修重算起始日','备注']
# 创建字体对象
title_font = Font(name='楷体')
header_font = Font(name='宋体',bold=True)
title_height = 30
header_fill = PatternFill(fill_type='solid', fgColor='f2f2f2')


# 创建一个新的工作簿
workbook = Workbook()
sheet = workbook.active
sheet.merge_cells('A1:G1')
sheet['A1'] = '即将下修转债列表'
sheet['A1'].font = title_font
sheet.row_dimensions[1].height = 22
sheet.column_dimensions['A'].width = 12
sheet.column_dimensions['E'].width = 16
sheet.column_dimensions['F'].width = 16
sheet.column_dimensions['G'].width = 25

sheet.append(excel_header)
for cell in sheet[2]:
        #if(cell.internal_value != "代码"):
        cell.fill = header_fill
        cell.font = header_font
index = 2
for bond_data in all_bonds_data:
    bond_code = bond_data["bond_id"]
    adjust_count = find_property_value(all_bonds_data,bond_code, 'adjust_count')
    print(bond_code)
    print(adjust_count)
    adjust = parse_adjust_string(adjust_count)
    if adjust == None:
        continue
    if adjust[0] == 0:
        continue
    if adjust[0] > 15:
        continue
    bond_nm = find_property_value(all_bonds_data,bond_code, 'bond_nm')
    bond_id = find_property_value(all_bonds_data,bond_code, 'bond_id')
    #bond_id = int(bond_id)
    price = find_property_value(all_bonds_data,bond_code, 'price')
    premium_rt = find_property_value(all_bonds_data,bond_code, 'premium_rt')
    premium_rt = premium_rt/100.00
    #premium_rt_str =  str(premium_rt) + '%'
    readjust_dt = find_property_value(all_bonds_data,bond_code, 'readjust_dt')
    bond_backup = find_content_by_id(bond_id)
    item = [bond_nm,int(bond_id),price,premium_rt,adjust_count,readjust_dt,bond_backup]
    sheet.append(item)
    

#设置百分比
for cell in sheet['D']:
    pos = 'D'+str(cell.row)
    print(sheet[pos].value)
    if(is_number(sheet[pos].value)):
        cell.number_format = '0.00%'

blue_font  = Font(color='0000FF')  # 蓝色字体
for cell in sheet['B']:
    pos = 'B'+str(cell.row)
    print(sheet[pos].value)
    if(is_integer(sheet[pos].value)):
        cell.font = blue_font

#设置居中
for row in sheet.iter_rows(min_row=1, max_row=100, min_col=1, max_col=8):
    for cell in row:
        cell.alignment = Alignment(horizontal='center', vertical='center')
# 保存工作簿
adjust_list_file = datetime.now().strftime("即将下修转债列表-%Y年%m月%d日.xlsx")
workbook.save(adjust_list_file)