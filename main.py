# 一次运行所有文件
import subprocess

def execute_python_file(file_path):
    subprocess.call(['python', file_path])

# 在当前目录下执行另一个Python文件
execute_python_file('adjust_bonds.py')
execute_python_file('daifabonds.py')
execute_python_file('force_redeem.py')
execute_python_file('readjust_dt_list.py')
execute_python_file('yaoyue_stock.py')