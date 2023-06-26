import requests
import json
from datetime import datetime

def szseAnnual(page, stock):
    query_path = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
    headers = "" # 定义User_Agent
    query = {'pageNum': page,  # 页码
             'pageSize': 30,
             'tabName': 'fulltext',
             'column': 'szse',  # 深交所
             'stock': stock,
             'searchkey': '',
             'secid': '',
             'plate': 'sz',
             'category': 'category_kzzq_szsh;',  # 可转债查询
             'trade': '',
             #'seDate': '2016-01-01+~+2019-4-26'  # 时间区间
             }

    namelist = requests.post(query_path, data=query)
    return namelist.json()['announcements']


announcements = szseAnnual(1,'002022,gssz0002022')
# 定义目标日期
target_date = datetime(2023, 6, 22)  # 指定日期

# 存储符合条件的公告
filtered_announcements = []

# 遍历公告列表并筛选出目标日期的公告
for announcement in announcements:
    time = announcement['announcementTime'] / 1000  # 将时间戳转换为秒
    time = datetime.fromtimestamp(time)  # 转换为datetime对象

    # 检查是否与目标日期匹配
    if time.date() == target_date.date():
        filtered_announcements.append(announcement)

# 输出符合条件的公告
for announcement in filtered_announcements:
    title = announcement['announcementTitle']
    time = announcement['announcementTime'] / 1000  # 将时间戳转换为秒
    time = datetime.fromtimestamp(time)  # 转换为datetime对象
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")  # 格式化时间
    url = announcement['adjunctUrl']
    print("公告标题:", title)
    print("公告时间:", formatted_time)
    print("公告链接:", url)
    print()