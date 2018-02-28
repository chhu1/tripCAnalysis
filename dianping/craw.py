import time
import json
import requests
from random import randint
from bs4 import BeautifulSoup

crawConfig = {
  'xihan': {
    # 西汉南越王博物馆
    'key': '1595860',
    'file': 'xihan.txt',
    'pages': 34
  },
  'xihan2': {
    # 南越王墓
    'key': '45668387',
    'file': 'xihan2.txt',
    'pages': 4
  },
  'chenjiaci': {
    # 陈家祠
    'key': '1595869',
    'file': 'chenjiaci.txt',
    'pages': 84
  }
}

# 注意修改这里
currentConfig = crawConfig['xihan2']

def getDianping(page):
  url = "http://www.dianping.com/shop/" + currentConfig['key'] + "/review_all/p" + str(page)
  headers = {
    'Referer': url,
    'Host': 'www.dianping.com',
    'Cookie': '_lxsdk_cuid=15e5b9c2264c8-01a2606e4f6e72-3a3e5f04-1fa400-15e5b9c2264c8; _lxsdk=15e5b9c2264c8-01a2606e4f6e72-3a3e5f04-1fa400-15e5b9c2264c8; _hc.v=009b0c97-fa20-232d-5b00-2defe7378c91.1504775513; __mta=214848040.1504775516006.1504775516006.1504783355188.2; td_cookie=317642863; s_ViewType=10; JSESSIONID=DA060C7C176E9F1C96CF0CF29F84A2EE; aburl=1; cy=4; cye=guangzhou; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=15ffbbd0376-ddf-ba0-ea8%7C%7C117',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
  }
  response = requests.get(url, headers = headers)
  return response.content.decode('utf-8')

def getComments(html_doc):
  list = []
  soup = BeautifulSoup(html_doc, 'html.parser')
  singleComment = soup.find_all('div', class_ = 'J_brief-cont')
  for item in singleComment:
    list.append(item.get_text())
  return list

if __name__ == '__main__':
  f_out = open(currentConfig['file'], 'w', encoding = 'utf8')
  for i in range(1, currentConfig['pages']):
    time.sleep(randint(1, 5))
    print (i)
    list = getComments(getDianping(i))
    for item in list:
      f_out.write(item.strip() + '\n')
  f_out.close()