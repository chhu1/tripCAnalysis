allConfig = {
  'xihan': {
    # 西汉南越王博物馆
    'items': ['../baidu/xihan.txt', '../ctrip/xihan.txt', '../dianping/xihan.txt', '../dianping/xihan2.txt', '../mafengwo/xihan.txt', '../qunar/xihan.txt', '../tripadvisor/xihan.txt'],
    'out': 'xihan.txt'
  },
  'chenjiaci': {
    'items': ['../baidu/chenjiaci.txt', '../ctrip/chenjiaci.txt', '../dianping/chenjiaci.txt', '../mafengwo/chenjiaci.txt', '../qunar/chenjiaci.txt', '../tripadvisor/chenjiaci.txt'],
    'out': 'chenjiaci.txt'
  }
}

# 注意修改这里
currentConfig = allConfig['chenjiaci']

def colAll(items, out):
    f_out = open(out, 'w', encoding = 'utf8')
    for item in items:
        f_in = open(item, encoding = 'utf8')
        for l in f_in:
            f_out.write(l)
        f_in.close()
        f_out.write('\n\n\n\n\n\n\n\n\n\n')
    f_out.close()

if __name__ == '__main__':
    colAll(currentConfig['items'], currentConfig['out'])
