import time
import json
import requests
from random import randint
from bs4 import BeautifulSoup

crawConfig = {
  'xihan': {
    # 西汉南越王博物馆
    'key': 'Attraction_Review-g298555-d457131-Reviews-Museum_of_the_Western_Han_Dynasty_Mausoleum_of_the_Nanyue_King-Guangzhou_Guangdong.html',
    'key2': 'Attraction_Review-g298555-d457131-Reviews-or',
    'key3': '0-Museum_of_the_Western_Han_Dynasty_Mausoleum_of_the_Nanyue_King-Guangzhou_Gua.html',
    'file': 'xihan.txt',
    'pages': 16
  },
  'chenjiaci': {
    'key': 'Attraction_Review-g298555-d311546-Reviews-Chen_Clan_Ancestral_Hall_Folk_Craft_Museum-Guangzhou_Guangdong.html',
    'key2': 'Attraction_Review-g298555-d311546-Reviews-or',
    'key3': '0-Chen_Clan_Ancestral_Hall_Folk_Craft_Museum-Guangzhou_Guangdong.html',
    'file': 'chenjiaci.txt',
    'pages': 40
  }
}

# 注意修改这里
currentConfig = crawConfig['chenjiaci']

def getTripadvisorPage(page):
  url = ''
  if page == 0:
    url = 'https://cn.tripadvisor.com/' + currentConfig['key']
  else:
    url = 'https://cn.tripadvisor.com/' + currentConfig['key2'] + str(page) + currentConfig['key3']
  payload = {
    'reqNum': 1,
    'changeSet': 'REVIEW_LIST'
  }
  headers = {
    'cookie': 'VRMCID=%1%V1*id.10568*llp.%2FAttraction_Review-g298555-d1864491-Reviews-Guangdong_Museum-Guangzhou_Guangdong%5C.html*e.1505387843549; PMC=V2*MS.65*MD.20170907*LD.20170907; TAUnique=%1%enc%3AGO7Qyh9ut%2BM%2FWWMo24PrsDRwDX6kBuGDkg01BpyQ7aM1jFGw1G8Jhw%3D%3D; TAPD=cn.tripadvisor.com; ServerPool=C; TASSK=enc%3AAIGs%2BvKh463yHmW4EnDtPBtou8IqDPQjvIvlY4wWTAciAPzAPM859NBUB4Mysyo2v9HJnOkAUGjCr7AKbaT891U0MBuG3%2FfRXHsHb94vxIk1BaX77fw5DViM4fdEcq%2BoSw%3D%3D; PAC=ADrROqmoZDT5jKZTi0UAzD-sPkG-U5BI_u7oAmpZMFNKrdQBsgIjbsX_WqQ6Y3aJdU-pmO4tIYMmgYSUB81vpzJije_M8ZcMiXcTI22j_U4OmhwlxtxeE1YL9uiHaYvCVKWPxJi7VAZPX-kLDKp5vV64H0jRV0NUMIqPQDIrocb37TeD-okKqai-prJ-8pur6odhuY7MiPZodwygJ0BknkXiDOsb17IpA-HFOr3USyKVHzx0QgK9or-aVxJeWulexwOPa0assxgXT4icHJ8rudNTcqMhiDiqpzGZUIAkxDkMcvMbOjO8jrU2c-7D2WXPCQ%3D%3D; TART=%1%enc%3AIXCEKnwxKFFn%2BOpqy6WET0BBnat%2Fjx0FgG6x1pZ4uBwkiD%2F9kyhVcDRBuds9S%2FBK4ieoPdYMDDY%3D; __gads=ID=1188d04f4ae853e8:T=1504783068:S=ALNI_MaH40_-3ZOnRYYhnb45SyIqHkLYSQ; BEPIN=%1%15e5c26a711%3Bbak99b.b.tripadvisor.com%3A10023%3B; roybatty=TNI1625!AKFVo3RVIgbvFzUQUxeuE1dkn6bnbuXhQClTWtT7lyASYC346bjeJP3WZokUEqjtsNTktCLlvR3msKKVc5XUVw4DG7VHCz%2FR7BzfesfTmGfS0YIVq8sZwvqSQlyRhpc6jhL8hsvL7ALZmpIiBDxmkBTvsiNTML9OaRJIO7kK8NRe%2C1; TASession=V2ID.1BB651A7EDB7BD175BC38E1D147D8841*SQ.161*LS.Attraction_Review*GR.93*TCPAR.73*TBR.97*EXEX.34*ABTR.49*PHTB.94*FS.32*CPU.80*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.zhCN*FA.1*DF.0*IR.1*OD.null*MS.-1*RMS.-1*FLO.298555*TRA.true*LD.1864491; TATravelInfo=V2*AY.2017*AM.9*AD.17*DY.2017*DM.9*DD.18*A.2*MG.-1*HP.2*FL.3*RVL.234454_250l298555_250l1864492_250l1864491_250*DSM.1504786025118*RS.1; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Ccatchsess%2C6%2C-1%7Cbrandsess%2C%2C-1%7CCpmPopunder_1%2C3%2C1504871169%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C10%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7Cmds%2C1504785578927%2C1504871978%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1505388370%7CLaFourchette+MC+Banners%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7CTheForkORPers%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAUD=LA-1504783067022-1*RDD-1-2017_09_07*HDD-1523583-2017_09_17.2017_09_18.1*HD-2511912-2017_09_17.2017_09_18.1864491*LD-2957946-2017.9.17.2017.9.18*LG-2957948-2.1.F.; TAReturnTo=%1%%2FAttraction_Review%3Fg%3D298555%26reqNum%3D1%26d%3D1864491%26changeSet%3DREVIEW_LIST%26o%3Dr10',
    'Host': 'cn.tripadvisor.com',
    'Origin': 'https://cn.tripadvisor.com',
    'Referer': 'https://cn.tripadvisor.com/' + currentConfig['key'],
    'X-Puid': 'WbExgQoQKm0AAjrAYr8AAAAa',
    'X-Requested-With': 'XMLHttpRequest'
  }
  response = requests.post(url, params = payload, headers=headers)
  return response.content.decode('utf-8')

def getComments(html_doc):
  list = []
  soup = BeautifulSoup(html_doc, "html.parser")
  singleComment = soup.find_all('div', class_ = 'review-container')
  for item in singleComment:
    commentBox = item.find('div', class_ = 'innerBubble').find('div', class_ = 'wrap').find('p', class_ = 'partial_entry')
    if commentBox.string:
      list.append(commentBox.string)
    else:
      list.append(commentBox.get_text())
  return list

if __name__ == '__main__':
  f_out = open(currentConfig['file'], 'w', encoding = 'utf8')
  for i in range(0, currentConfig['pages']):
    time.sleep(randint(1, 3))
    print (i)
    list = getComments(getTripadvisorPage(i))
    print ('\n'.join(list))
    for item in list:
      f_out.write(item + '\n')
  f_out.close()