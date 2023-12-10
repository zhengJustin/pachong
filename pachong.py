import requests
from bs4 import BeautifulSoup
import logging
import os

# 目标网站URL
url = "https://www.satsx.io/marketplace/atomicals/dmint/containers/toothy/listed?sort_by=price&page=1"

# 发送HTTP GET请求，获取页面内容
response = requests.get(url)

# 解析HTML页面内容
soup = BeautifulSoup(response.text, 'html.parser')

# 获取最低价格
floor_price = soup.select_one('.flex-col.items-center .flex div span').text

# 打印最低价格
PUSH_TOKEN = os.environ.get("PUSHPLUS_KEY")
url1 = 'http://www.pushplus.plus/send'
title = "鳄鱼的价格："
if float(floor_price) <0.007 or float(floor_price)>0.02:
    r = requests.get(url1, params={'token': PUSH_TOKEN,
                               'title': title,
                              'content': floor_price})
    logging.info(f'通知推送结果：{r.status_code, r.text}')
