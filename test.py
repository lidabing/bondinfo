import os
from datetime import date

def create_data_directory():
    # 获取当前文件所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 获取当前日期
    today = date.today()
    date_str = today.strftime("%Y-%m-%d")
    
    # 构建目录路径
    data_dir = os.path.join(current_dir, "data")
    date_dir = os.path.join(data_dir, date_str)
    
    # 创建目录
    os.makedirs(date_dir, exist_ok=True)
    
    # 返回目录路径
    return date_dir


create_data_directory()