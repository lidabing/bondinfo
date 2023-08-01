import re
import json
import json
import os
from datetime import datetime,timedelta

def read_jisilu_request_headers_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        data = json.loads(content)
    return data

def find_backup_content_by_id(target_id):
    with open('backup.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith(target_id):
                content = line.split('|', 1)[-1].strip()
                return content
    return None

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
    
def compare_dates(date1_str, date2_str):
    # 将日期字符串转换为日期对象
    date1 = datetime.strptime(date1_str, '%Y-%m-%d').date()
    date2 = datetime.strptime(date2_str, '%Y-%m-%d').date()

    return date1 >= date2

def extract_date_info(date_str):
    if date_str is None:
        return None

    if not date_str:
        return None

    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        year = date.year
        month = date.month
        day = date.day
        return year, month, day
    except ValueError:
        return None
    
def separate_numbers(string):
    number = re.findall(r'\d+', string)
    return number

def create_data_directory():
    # 获取当前文件所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 获取当前日期
    today = datetime.today()
    date_str = today.strftime("%Y-%m-%d")
    
    # 构建目录路径
    data_dir = os.path.join(current_dir, "data")
    date_dir = os.path.join(data_dir, date_str)
    
    # 创建目录
    os.makedirs(date_dir, exist_ok=True)
    
    # 返回目录路径
    return date_dir

def get_image_path():
    # 获取当前文件所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 获取当前日期
    current_date = datetime.today().strftime("%Y-%m-%d")

    # 构建数据目录路径
    data_dir = os.path.join(current_dir, "data", current_date)

    # 创建数据目录（如果不存在）
    os.makedirs(data_dir, exist_ok=True)

    # 构建数据目录路径
    images_dir = os.path.join(data_dir, "images")

    # 创建数据目录（如果不存在）
    os.makedirs(images_dir, exist_ok=True)

    # 返回文件路径
    return images_dir

def get_file_path(filename):
    # 获取当前文件所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 获取当前日期
    current_date = datetime.today().strftime("%Y-%m-%d")

    # 构建数据目录路径
    data_dir = os.path.join(current_dir, "data", current_date)

    # 创建数据目录（如果不存在）
    os.makedirs(data_dir, exist_ok=True)

    # 构建完整的文件路径
    file_path = os.path.join(data_dir, filename)

    # 返回文件路径
    return file_path


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
    

def write_array_to_file(array, file_path):
    with open(file_path, 'w') as file:
        for item in array:
            file.write(str(item) + '\n')


#获取提醒文件路径
def get_reminder_file_path():
    return os.path.join(get_image_path(),'提醒内容.txt')

#创建需要关注的文件内容
def generate_reminder_file(file_path, content=""):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"File generated successfully: {file_path}")
    except Exception as e:
        print(f"Error occurred while generating the file: {e}")

#追加内容
def append_reminder(text):
    try:
        file_path = get_reminder_file_path()
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(text + '\n')
        print(f"Appended text '{text}' to the file: {file_path}")
    except Exception as e:
        print(f"Error occurred while appending text: {e}")


def get_today_date():
    today = datetime.now().strftime("%Y-%m-%d")
    return today

def is_same_day(date_string):
    try:
        input_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        today = datetime.now().date()
        return input_date == today
    except ValueError:
        return False
