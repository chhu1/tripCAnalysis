import json
import time
import requests
from random import uniform

sentimentConfig = {
  'xihan': {
    # 西汉南越王博物馆
    'file': 'all/xihan_result.txt',
    'file_out': 'sentiment/xihan.txt'
  },
  'chenjiaci': {
    'file': 'all/chenjiaci_result.txt',
    'file_out': 'sentiment/chenjiaci.txt'
  },
  'shengbo': {
    'file': 'all/shengbo_result.txt',
    'file_out': 'sentiment/shengbo.txt'
  }
}

# 注意修改这里
currentConfig = sentimentConfig['shengbo']

def getSentiment(text):
  url = "http://fileload.datagrand.com:8080/sentiment"
  payload = {
    'text': text
  }
  headers = {
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'fileload.datagrand.com:8080',
    'Origin': 'http://www.datagrand.com',
    'Referer': 'http://www.datagrand.com/demo/nlp/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
  }
  response = requests.post(url, params = payload, headers = headers)
  result = response.content.decode('unicode-escape').encode('latin1').decode('utf-8')
  if result.find('message') >= 0:
    time.sleep(5)
    return getSentiment(text)
  return result

if __name__ == '__main__':
  f_in = open(currentConfig['file'], 'r', encoding = 'utf8')
  try:
    for line in f_in:
      f_out = open(currentConfig['file_out'], 'a', encoding = 'utf8')
      time.sleep(uniform(0.8, 1.2))
      result = getSentiment(line)
      print (line)
      print (result)
      f_out.write(result + '\n')
      f_out.close()
    f_in.close()
  except Exception as e:
    print (e)
    f_in.close()
    print ('Error: Break')
