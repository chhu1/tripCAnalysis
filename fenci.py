# -*- coding: utf-8 -*-
import re
import json
import jieba
import jieba.posseg as pseg
from collections import Counter

#黑名单
PUNCTUATIONS = [u'。', u'，', u'“', u'”', u'…', u'？', u'！', u'、', u'；', u'（', u'）',u'?',u'：', '(', ')', ' ', u'—', u':', u'《', u'》']
STOPWORDS = [u'的', u'地', u'得', u'而', u'了', u'在', u'是', u'我', u'有', u'和', u'就',  u'不', u'人', u'都', u'一', u'一个', u'上', u'也', u'很', u'到', u'说', u'要', u'去', u'你',  u'会', u'着', u'没有', u'看', u'好', u'自己', u'这', u'但', u'啊', u'吧', u'但是', u'所以', u'吗', u'不过', u'而且', u'一下', u'因为', u'对', u'从', u'如果', u'这个', u'还', u'让', u'一些', u'才', u'太', u'又', u'真是', u'那', u'更', u'能', u'再', u'过', u'等', u'个', u'那个', u'每个', u'来', u'带', u'等等', u'然后', u'跟', u'应该', u'没', u'挺', u'来', u'有点', u'用', u'只', u'什么', u'它', u'被', u'为', u'呢', u'给', u'像', u'中', u'其中', u'两个', u'当时', u'部分', u'后', u'最后', u'虽然', u'做', u'与', u'由于', u'这些', u'先', u'另外', u'比', u'完', u'或者', u'凭', u'以', u'下', u'这么', u'号', u'这样', u'这次', u'那些', u'里', u'把', u'一定', u'展', u'点', u'之', u'拿', u'路', u'花', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'10', u'00', u'区', u'进', u'线', u'或', u'于', u'一共', u'哦', u'却', u'时', u'其', u'蛮', u'之一', u'比如', u'比如', u'必须', u'站', u'出', u'真', u'厅', u'及', u'内', u'并', u'当然', u'大概', u'啦', u'至', u'找', u'前', u'们', u'一去', u'一次', u'分', u'层', u'呀', u'类', u'如', u'只要', u'来说', u'16', u'可以', u'还是', u'馆', u'就是', u'这里', u'最', u'东西', u'大', u'我们', u'不用', u'不是', u'的话', u'想', u'最好', u'大家', u'主要', u'其他', u'可能', u'排', u'出来', u'一般', u'记得', u'可', u'其实', u'几个', u'个人', u'有些', u'作为', u'不能', u'已经', u'长', u'开始', u'不要', u'好像', u'太多', u'带上', u'以及', u'尤其', u'分为', u'小', u'那里', u'年', u'基本', u'才能', u'三', u'以后', u'少', u'一起', u'方面', u'一点', u'一直', u'只是', u'只有', u'关于', u'高', u'四大', u'那么', u'有个', u'方向', u'不会', u'感受', u'十分', u'队', u'之后', u'没什么', u'对面', u'不够', u'不算', u'相当', u'她', u'领', u'实在', u'来看', u'包括', u'他', u'对于', u'确实', u'算是', u'器', u'元', u'近', u'下来', u'算', u'还要', u'好好', u'大', u'肯定', u'将', u'必', u'绝对', u'还好', u'这种', u'不然', u'楼', u'三个', u'这边', u'许多', u'刚', u'爱', u'很少', u'根本', u'最大', u'超', u'省']

jieba.load_userdict('dict.txt')

class StatWords(object):
    def statTopN(self, path, savePath, n, resultPath = ''):
        word_txt = open(path, encoding='utf8')
        wordDict = {}
        for l in word_txt:
            word = ''
            words = re.split('[\s\ \\,\;\.\!\n]+', l)
            if (words[0] and words[0].find('-') > 0):
                word = words[0]
            elif (words[1] and words[1].find('-') > 0):
                word = words[1]
            else:
                continue
            if word in wordDict:
                wordDict[word] = wordDict[word] + 1
            else:
                wordDict[word] = 1  
        count = Counter(wordDict)
        words_file = open(savePath, 'w', encoding='utf8')
        for item in count:
            words_file.write(item + '\n')
        words_file.close()
        print (json.dumps(count.most_common(n), ensure_ascii = False))
        if (resultPath != ''):
            resultFile = open(resultPath, 'w', encoding='utf8')
            resultFile.write(json.dumps(count.most_common(n), ensure_ascii = False))
            resultFile.close

    def statWords(self, input, output):
        f_in = open(input, encoding = 'utf8')
        f_out = open(output, 'w', encoding = 'utf8')

        try:
            for l in f_in:
                seg_list = pseg.cut(l)
                for seg in seg_list:
                    if seg.word not in STOPWORDS and seg.word not in PUNCTUATIONS and seg.flag != 'm' and seg.flag != 'x' and seg.flag != 'f':
                        f_out.write(seg.word.lower() + '-' + seg.flag + '\n')

        finally:
            f_in.close()
            f_out.close()

if __name__ == '__main__':
    s = StatWords()
    config = {
        'xihan': {
            'file_in': 'all/xihan_result.txt',
            'file_out': 'words/xihan_out.txt',
            'words_out': 'words/xihan_words.txt',
            'result': 'words/xihan_result.txt'
        },
        'chenjiaci': {
            'file_in': 'all/chenjiaci_result.txt',
            'file_out': 'words/chenjiaci_out.txt',
            'words_out': 'words/chenjiaci_words.txt',
            'result': 'words/chenjiaci_result.txt'
        }
    }
    currentConfig = config['xihan']
    s.statWords(currentConfig['file_in'], currentConfig['file_out'])
    s.statTopN(currentConfig['file_out'], currentConfig['words_out'], 800, currentConfig['result'])
