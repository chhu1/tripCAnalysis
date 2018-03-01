import json

sentimentConfig = {
  'xihan': 'xihan.txt',
  'chenjiaci': 'chenjiaci.txt',
  'shengbo': 'shengbo.txt'
}

def getResult(file):
  nums = 0
  numResult = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
  }
  result = {
    1: '0',
    2: '0',
    3: '0',
    4: '0',
    5: '0',
    6: '0',
    7: '0'
  }
  f_in = open(file, 'r', encoding = 'utf8')
  for line in f_in:
    data = json.loads(line)
    if data and (data['positive'] or data['negative']):
      nums = nums + 1
      if 0 <= data['positive'] <= 0.15:
        numResult[1] = numResult[1] + 1
      elif 0.15 < data['positive'] <= 0.28:
        numResult[2] = numResult[2] + 1
      elif 0.28 < data['positive'] <= 0.4:
        numResult[3] = numResult[3] + 1
      elif 0.4 < data['positive'] <= 0.6:
        numResult[4] = numResult[4] + 1
      elif 0.6 < data['positive'] <= 0.72:
        numResult[5] = numResult[5] + 1
      elif 0.72 < data['positive'] <= 0.85:
        numResult[6] = numResult[6] + 1
      elif 0.85 < data['positive'] <= 1.0:
        numResult[7] = numResult[7] + 1
  f_in.close()
  for key in numResult:
    result[key] = str(round(numResult[key] / float(nums) * 100, 2)) + '%'
  return {
    'nums': nums,
    'numResult': numResult,
    'result': result
  }

if __name__ == '__main__':
  f_out = open('tongji.txt', 'w', encoding = 'utf8')
  f_out.write('规则：\n========================================\n')
  print ('规则：\n========================================')
  f_out.write('1    |       0 - 0.15    |    非常不满\n')
  print ('1    |       0 - 0.15    |    非常不满')
  f_out.write('2    |    0.15 - 0.28    |    不满\n')
  print ('2    |    0.15 - 0.28    |    不满')
  f_out.write('3    |    0.28 - 0.4     |    稍微不满\n')
  print ('3    |    0.28 - 0.4     |    稍微不满')
  f_out.write('4    |     0.4 - 0.6     |    中立\n')
  print ('4    |     0.4 - 0.6     |    中立')
  f_out.write('5    |     0.6 - 0.72    |    稍微满意\n')
  print ('5    |     0.6 - 0.72    |    稍微满意')
  f_out.write('6    |    0.72 - 0.85    |    满意\n')
  print ('6    |    0.72 - 0.85    |    满意')
  f_out.write('7    |    0.85 - 1.0     |    非常满意\n')
  print ('7    |    0.85 - 1.0     |    非常满意')
  f_out.write('\n\n')
  print ('\n')
  for key in sentimentConfig:
    result = getResult(sentimentConfig[key])
    print (key + '\n========================================' + '\n总数量：' + str(result['nums']) + '\n数据结果：' + str(result['numResult']) + '\n比例结果：' + str(result['result']) + '\n')
    f_out.write(key + '\n========================================' + '\n总数量：' + str(result['nums']) + '\n数据结果：' + str(result['numResult']) + '\n比例结果：' + str(result['result']) + '\n\n')