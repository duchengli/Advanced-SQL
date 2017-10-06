#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Duchengli'
# 透明房产网新房爬虫


import requests
from bs4 import BeautifulSoup
import lxml
import pickle

def get_page(page_number):
    page_url = 'http://www.funi.com/loupan/region_0_0_0_0_%d' %page_number

    retry_time = 20
    for i in range(retry_time):
        try:
            r = requests.get(url=page_url)
            break
        except:
            if i < retry_time - 1:
                continue
            else:
                print('多次尝试仍然失败!')

    if r.status_code == 200:
        soup = BeautifulSoup(r.text,'lxml')
        results = soup.find_all('dt', class_='clearfix')
        for result in results:
            try:
                title = result.h2.a.text.strip()
                if title in loupanlist:
                    pass
                else:
                    loupanlist.append(title)
                    print(title)
            except:
                print('有问题')

datafile = open('d:\\loupanlist.pkl', 'rb')
#loupanlist=['保利春天花语','保利中央峰景','天府欧城','源上湾国际社区2期','蓝光观岭国际社区9期','武海中华名城','成都后花园国宾红叶','千禧河畔国际社区B区','凯德卓锦万黛','春天国际']
loupanlist = pickle.load(datafile)
datafile.close()

#loupanlist = []

for i in range(1,332):
    get_page(i)

datafile = open('d:\\loupanlist.pkl', 'wb')
pickle.dump(loupanlist, datafile)
datafile.close()


