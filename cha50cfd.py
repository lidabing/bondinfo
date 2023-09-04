from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from common import *

# 设置Chrome选项以模拟移动设备
chrome_options = ChromeOptions()
chrome_options.add_argument("--headless")  # 无头模式，不显示浏览器窗口
chrome_options.add_argument("--disable-gpu")  # 禁用GPU加速
chrome_options.add_argument("--disable-extensions")  # 禁用扩展
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=360,640")  # 设置窗口大小，模拟移动设备

# 创建Chrome WebDriver实例
#chrome_service = ChromeService(executable_path='你的Chrome驱动程序路径')  # 请替换为您的Chrome驱动程序路径
driver = webdriver.Chrome( options=chrome_options)

# 打开页面
url = "https://gu.sina.cn/ft/hq/hf.php?symbol=CHA50CFD&autocallup=no&isfromsina=no"
driver.get(url)

# 等待页面加载完成，这里可以根据需要自定义等待条件
# 例如，等待某个元素可见或页面标题等
# driver.implicitly_wait(10)  # 隐式等待，等待10秒

# 查找元素并获取其文本内容
element = driver.find_element(By.ID, "HQBox_Point_percent")
content = element.text
print(content)

def convert_sign(a):
    if a.startswith('-'):
        return f"隔夜A50指数跌{a}"
    elif a.startswith('+'):
        return f"隔夜A50指数涨{a}"
    
output= convert_sign(content)
append_reminder(output)

# 关闭浏览器窗口
driver.quit()
