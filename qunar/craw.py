import time
import requests
from random import randint
from bs4 import BeautifulSoup

crawConfig = {
  'xihan': {
    # 西汉南越王博物馆
    'key': 706055,
    'file': 'xihan.txt',
    'pages': 7
  },
  'chenjiaci': {
    'key': 715026,
    'file': 'chenjiaci.txt',
    'pages': 23
  }
}

# 注意修改这里
currentConfig = crawConfig['chenjiaci']

def getQunarPage(page):
  url = "https://travel.qunar.com/place/api/html/comments/poi/" + str(currentConfig['key'])
  payload = {
    'poiList': 'true',
    'sortField': 1,
    'rank': 0,
    'pageSize': 10,
    'page': page
  }
  response = requests.get(url, params = payload)
  return response.json()['data']

def getComments(html_doc):
  list = []
  hrefs = []
  soup = BeautifulSoup(html_doc, "html.parser")
  singleComment = soup.find_all('li', class_ = 'e_comment_item')
  for item in singleComment:
    seeMore = item.find('a', class_ = 'seeMore')
    if (seeMore):
      if (seeMore['href']):
        hrefs.append(seeMore['href'])
    else:
      commentBox = item.find('div', class_ = 'e_comment_content')
      list.append(commentBox.get_text())
  return (list, hrefs)

def getDetail(url):
  newStr = ''
  response = requests.get(url)
  content = response.content.decode('unicode-escape').encode('latin1').decode('utf-8')
  soup = BeautifulSoup(content, "html.parser")
  items = soup.find_all('div', 'comment_content')
  for item in items:
    newStr += item.get_text()
  return newStr

if __name__ == '__main__':
  f_out = open(currentConfig['file'], 'w', encoding = 'utf8')
  for i in range(1, currentConfig['pages']):
    time.sleep(randint(1, 3))
    print (i)
    lists, hrefs = getComments(getQunarPage(i))
    for href in hrefs:
      time.sleep(randint(0, 2))
      lists.append(getDetail(href))
    for item in lists:
      f_out.write(item + '\n')
  f_out.close()