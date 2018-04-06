#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Duchengli'

import requests
from bs4 import BeautifulSoup
import lxml


def get_fcq(page_number):
    page_url = 'http://news.cd.fang.com/more/201312398/%d.html' %page_number
    retry_time = 20
    for i in range(retry_time):
        try:
            r = requests.get(url=page_url)
            break
        except:
            if i < retry_time - 1:
                continue
            else:
                print('无法获取网页原始数据')
                break

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        results = soup.find_all('div',class_='infoBox-item clearfix')
        for result in results:
            try:
                title = result.h3.a.text.strip()
                link = result.h3.a.get('href')
                newslists.append([title,link])
#                print([title,link])
            except:
                print('有问题')


newslists=[]
# 爬取新闻列表
for i in range(1, 251):
    print('正在抓取第%d页' %i)
    get_fcq(i)
    
newssets=set(newslists)
print('一共抓取了%d条新闻' %len(newssets))
for k in range(0,len(newssets)):
    print(newssets[k])
#    print('\n')
