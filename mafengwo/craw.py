import time
import json
import requests
from random import randint
from bs4 import BeautifulSoup

crawConfig = {
  'xihan': {
    # 西汉南越王博物馆
    'key': 1049,
    'file': 'xihan.txt',
    'pages': 44
  },
  'chenjiaci': {
    'key': 444,
    'file': 'chenjiaci.txt',
    'pages': 121
  }
}

# 注意修改这里
currentConfig = crawConfig['chenjiaci']

def getMafengwoPage(page):
  url = "http://pagelet.mafengwo.cn/poi/pagelet/poiCommentListApi"
  payload = {
    'params': json.dumps({
      'poi_id': currentConfig['key'],
      'page': page,
      'just_comment': 1
    })
  }
  response = requests.post(url, params = payload)
  return response.json()['data']['html']

def getComments(html_doc):
  list = []
  soup = BeautifulSoup(html_doc, 'html.parser')
  singleComment = soup.find_all('li', class_ = 'rev-item')
  for item in singleComment:
    commentBox = item.find('p', class_ = 'rev-txt')
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
    list = getComments(getMafengwoPage(i))
    for item in list:
      f_out.write(item + '\n')
  f_out.close()