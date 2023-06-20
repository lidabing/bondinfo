data = '''000810|创维数字|14.82|正式邀约报告书
002644|佛慈制药|9.6|出摘要两个月
600282|南钢股份|3.69|民事诉讼
600449|宁夏建材|12.59|最新公告重组方案
000830|鲁西化工|12.76|合并实施被暂停
600729|重庆百货|19.49|29.72'''

lines = data.split('\n')  # 按行分割数据

for line in lines:
    fields = line.split('|')  # 按竖线分割字段
    if len(fields) >= 4:
        stock_code = fields[0]
        stock_name = fields[1]
        stock_price = fields[2]
        stock_info = fields[3]
        
        print(f"股票代码: {stock_code}")
        print(f"股票名称: {stock_name}")
        print(f"要约价格: {stock_price}")
        print(f"要约阶段: {stock_info}")
        print()


filename = "yaoyuedata.txt"  # 文件名

with open(filename, "r", encoding="utf-8") as file:
    data = file.read()  # 读取文件内容

lines = data.split('\n')  # 按行分割数据

for line in lines:
    fields = line.split('|')  # 按竖线分割字段
    if len(fields) >= 4:
        stock_code = fields[0]
        stock_name = fields[1]
        stock_price = fields[2]
        stock_info = fields[3]
        
        print(f"股票代码: {stock_code}")
        print(f"股票名称: {stock_name}")
        print(f"要约价格: {stock_price}")
        print(f"要约阶段: {stock_info}")
        print()