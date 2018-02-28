import time
import requests
from random import randint
from bs4 import BeautifulSoup

crawConfig = {
  'xihan': {
    # 西汉南越王博物馆
    'key': '70d3330a23088cc57454b3f8',
    'file': 'xihan.txt',
    'pages': 27
  },
  'chenjiaci': {
    'key': 'b2eac43404a6a431877150f8',
    'file': 'chenjiaci.txt',
    'pages': 73
  }
}

# 注意修改这里
currentConfig = crawConfig['xihan']

def getBaiduPage(page):
  url = "https://lvyou.baidu.com/user/ajax/remark/getsceneremarklist"
  payload = {
    'xid': currentConfig['key'],
    'score': 0,
    'pn': page * 15,
    'rn': 15,
    'style': 'hot',
    'format': 'ajax',
    'flag': 1,
    't': int(time.time())
  }
  response = requests.get(url, params = payload)
  return response.json()

def parseJson(jsonText):
  list = []
  for item in jsonText['data']['list']:
    soup = BeautifulSoup(item['content'], 'html.parser')
    list.append(soup.get_text())
  return list

if __name__ == '__main__':
  f_out = open(currentConfig['file'], 'w', encoding = 'utf8')
  for i in range(0, currentConfig['pages']):
    time.sleep(randint(1, 3))
    print (i)
    for item in parseJson(getBaiduPage(i)):
      f_out.write(item + '\n')
  f_out.close()