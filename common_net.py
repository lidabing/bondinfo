#一些基础网络请求库
import requests
from common import *
def fetch_base_bonds_info():
    request_headers_file = 'request_headers.txt'
    request_headers = read_jisilu_request_headers_file(request_headers_file)
    url = "https://www.jisilu.cn/webapi/cb/list/"
    # 发起 HTTP GET 请求
    #my_header = request_headers
    my_header = {
    'cookie': request_headers["cookie"],
    'Referer': 'https://www.jisilu.cn/web/data/cb/list', 
    'Accept': 'application/json, text/plain, */*',
    #':authority':'www.jisilu.cn',
    #':method':'GET',
    #':path':'/webapi/cb/list/',
    #':scheme':'https',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en,zh-CN;q=0.9,zh;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6,ko;q=0.5',
    'Columns':'1,70,2,3,5,6,7,8,9,10,11,12,14,15,77,78,79,80,81,82,83,84,16,19,22,23,24,72,25,26,27,28,29,30,31,32,33,34,35,75,44,46,47,50,52,53,74,73,54,55,56,57,58,59,60,61,62,76,63,67,71',
    'Dnt':'1',
    'If-Modified-Since':'Mon, 04 Sep 2023 11:10:38 GMT',
    'Init':'1',
    'Referer':'https://www.jisilu.cn/web/data/cb/list',
    'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'Sec-Ch-Ua-Mobile':'?1',
    'Sec-Ch-Ua-Platform':"Android",
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
    }
    #my_header['Referer'] = 'https://www.jisilu.cn/web/data/cb/list'
    response = requests.get(url,headers=my_header)
    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return []

def fetch_adjust_bonds_info():
    #下修相关内容
    url = "https://www.jisilu.cn/webapi/cb/adjust/"

    request_headers_file = 'request_headers.txt'
    request_headers = read_jisilu_request_headers_file(request_headers_file)
    # 发起 HTTP GET 请求
    response = requests.get(url,headers=request_headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return []