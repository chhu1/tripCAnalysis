import time
import requests
from random import randint
from bs4 import BeautifulSoup

crawConfig = {
  'xihan': {
    # 西汉南越王博物馆
    'key': 76901,
    'key2': 6808,
    'file': 'xihan.txt',
    'pages': 38
  },
  'chenjiaci': {
    'key': 76877,
    'key2': 6772,
    'file': 'chenjiaci.txt',
    'pages': 157
  }
}

# 注意修改这里
currentConfig = crawConfig['chenjiaci']

def getCtripPage(page):
  url = "http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView"
  payload = {
    'poiID': currentConfig['key'],
    'districtId': 152,
    'districtEName': 'Guangzhou',
    'pagenow': page,
    'order': 3.0,
    'star': 0.0,
    'tourist': 0.0,
    'resourceId': currentConfig['key2'],
    'resourcetype': 2
  }
  response = requests.post(url, params = payload)
  return response.content.decode('unicode-escape').encode('latin1').decode('utf-8')

def getComments(html_doc):
  list = []
  soup = BeautifulSoup(html_doc, 'html.parser')
  singleComment = soup.find_all('div', class_ = 'comment_single')
  for item in singleComment:
    commentBox = item.find('li', class_ = 'main_con').find('span', class_ = 'heightbox')
    if commentBox.string:
      list.append(commentBox.string)
    else:
      list.append(commentBox.get_text())
  return list

if __name__ == '__main__':
  f_out = open(currentConfig['file'], 'w', encoding = 'utf8')
  for i in range(1, currentConfig['pages']):
    time.sleep(randint(1, 3))
    print (i)
    list = getComments(getCtripPage(i))
    for item in list:
      f_out.write(item + '\n')
  f_out.close()
