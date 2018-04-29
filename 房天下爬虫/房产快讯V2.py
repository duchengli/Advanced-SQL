#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Duchengli'

import requests
from bs4 import BeautifulSoup
import lxml
import os
import time
import datetime

#读取房产快讯数据存档数据
load_data = []
with open('房产快讯数据存档.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        load_data.append(line[:-1])
#此时load_data已经有数据了

def get_date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    if len(day) == 1:
        return year + '-' + month + '-' + '0' + day
    else:
        return year + '-' + month + '-' + day

def get_fckx(page_number):
    time.sleep(1)
#   date = '2018-4-29'#手动输入日期
    date = get_date()
#    page_url = 'http://news.cd.fang.com/gdxw/2018-4-29/%d.html' % page_number
    page_url = 'http://news.cd.fang.com/gdxw/%s/%d.html' %(date,page_number)
    print(page_url)

    retry_time = 10
    for i in range(retry_time):
        try:
            r = requests.get(url=page_url)
            break
        except:
            if i < retry_time - 1:
                continue
            else:
                break

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        results = soup.find_all('div',class_='infoBox-item clearfix')
        for result in results:
            try:
                title = result.h3.a.text.strip()
                link = result.h3.a.get('href')
                if link in load_data:
                    pass
                else:
                    print([title, link])
                    load_data.append(link)
            except:
                pass

for i in range(1, 51):
#    print('正在抓取第%d页' %i)
    get_fckx(i)

#将改变后的load_data写回原来的文档,因为此时load_data不仅包括了新数据还包括了原来的数据，所用不能用a方法，只能用w方法
fobj=open("房产快讯数据存档.txt",'w',encoding='utf-8')
fobj.writelines(str(items)+'\n' for items in load_data)
fobj.close()

#_________________________________________________________________
#以下是第一次创建记录文件的时候才用，正常情况下不使用，除非记录文件出问题了
# fobj=open("房产快讯数据存档.txt",'a+',encoding='utf-8')
# fobj.writelines(str(items)+'\n' for items in load_data)
# fobj.close()