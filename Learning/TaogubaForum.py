#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Duchengli'
# 淘股吧帖子爬虫
# 2018-03-25生成

import requests
from bs4 import BeautifulSoup
import lxml
import os

def get_text(link):
    retry_time = 20
    for i in range(retry_time):
        try:
            r = requests.get(url=link)
            break
        except:
            if i < retry_time - 1:
                continue
            else:
                print('无法获取网页原始数据')

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        results = soup.find_all('div', class_='p_coten')
        for result in results:
#            print(result.text)
            content_lists.append(result.text)

def get_href(page_number):
    page_url = 'https://www.taoguba.com.cn/index?pageNo=%d&blockID=1&flag=1&pageNum=20754' % page_number
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

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        results = soup.find_all('li', class_='pcdj02')
        for result in results:
            try:
                link = 'https://www.taoguba.com.cn/'+result.a.get('href')
                post_lists.append(link)
            except:
                pass

post_lists = []
content_lists = []

#第一步是爬取帖子的超链接，构建post_links超链接列表
for i in range(1, 10):
    get_href(i)
print('一共爬取了%d条帖子' %len(post_lists))

#第二部是爬取所有帖子的明细数据，构建content_lists帖子列表
for post_list in post_lists:
    print(post_list)
    get_text(post_list)

fobj=open("content.txt",'w',encoding='utf-8')
fobj.writelines(('%s%s'%(str(items),os.linesep) for items in content_lists))
fobj.close()