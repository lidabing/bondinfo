# 一次运行所有文件
import subprocess
from common import *

def execute_python_file(file_path):
    subprocess.call(['python', file_path])


#初始化
create_data_directory()
get_image_path()
generate_reminder_file(get_reminder_file_path())

# 在当前目录下执行另一个Python文件
execute_python_file('adjust_bonds.py')
execute_python_file('daifabonds.py')
#execute_python_file('force_redeem.py')
execute_python_file('readjust_dt_list.py')
execute_python_file('yaoyue_stock.py')
execute_python_file('tiyixiaxiu.py')

#获取夜盘数据
append_reminder('[隔夜数据]')
execute_python_file('usdrmb.py')
execute_python_file('cha50cfd.py')
execute_python_file('kweb.py')