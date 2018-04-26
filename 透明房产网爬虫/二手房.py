#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'Duchengli'
# 透明房产网二手房爬虫
# mj参数规定了面积在100-200平方内的房源

import requests
from bs4 import BeautifulSoup
import lxml
import time
import random
import re
import math

#根据第一页上的信息条数获取翻页次数
def count_page(qy):
    page_url = 'http://esf.cdfgj.gov.cn/search?page=1&qy=%d&mj=100,200' %qy
    retry_time = 20
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
        soup = BeautifulSoup(r.text,'lxml')
        result = soup.find('div', class_='pan-tab clearfix').dt
        total_count = int(re.sub("\D", "",result.text))
        total_page = math.ceil(total_count/10)
        return total_page

#获取页面信息
def get_page(page_number,qy):
    page_url = 'http://esf.cdfgj.gov.cn/search?page=%d&qy=%d&mj=100,200' %(page_number,qy)
    retry_time = 10
    for i in range(retry_time):
        try:
            r = requests.get(url=page_url)
            break
        except:
            if i < retry_time - 1:
                continue
            else:
                err_list.append(page_number)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,'lxml')
        results = soup.find_all('div', class_='pan-item clearfix')
        for result in results:
            try:
                if result.find('div', class_='yhy').text == '已核验':#只爬取已经核验的房源
                    id = result.find('div', class_='ynum').text.strip()#解析核验号作为唯一标志项
                    link = 'http://esf.cdfgj.gov.cn'+result.h2.a.get('href')#解析房源连接
                    total_price = int(result.find('strong', class_='total-price').text.strip().replace('万',''))#解析总价
                    xqm = result.find('p',class_='p_hx').next_sibling.next_sibling.text.strip().split(' ')[0]#解析小区名称
#                    print(xqm,id,total_price,link)
#                    esf[id]=total_price
                    esf_list.append((id,xqm,total_price,link))
            except:
                pass
    print('%s 页已经处理完毕' %page_number)
    time.sleep(3)

esf_list = []
esf_dict = {}
err_page = []

for i in range(1,count_page(510105)+1):
#for i in range(1,5):
    get_page(i,510105)
# print(esf)
# print(err_page)

for i in sorted(esf_list, key=lambda  x:x[2], reverse=True):
    print(i)