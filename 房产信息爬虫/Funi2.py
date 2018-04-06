#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'Duchengli'
# 透明房产网二手房爬虫

import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import time
import random

def get_page(page_number):
    page_url = 'http://esf.cdfgj.gov.cn/search?page=%d' %page_number

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
        soup = BeautifulSoup(r.text,'lxml')
        results = soup.find_all('div', class_='pan-item clearfix')
        for result in results:
            try:
#                title = result.h2.a.text.strip()#解析房屋名称
                tmp1 = list(map(lambda x:x.string.strip() ,result.find('p',class_='p_hx').children))#解析房屋属性
                tmp2 = [x for x in tmp1 if x != '']#第二次解析房屋属性

                tmp3 = list(map(lambda x: x.string.strip(), result.find('p', class_='p_gx').children))
                tmp4 = [x for x in tmp3 if x != '']#解析发布渠道

                tmp5 = result.find('p',class_='p_hx').next_sibling.next_sibling.text.strip()#解析小区名称
                tmp6 = tmp5.split(' ')[0]
                tmp7 = tmp5.split(' ')[1][1:].replace('[','').replace(']','')
                if tmp7.find('区')!= -1:
                    tmp8 = tmp7[:tmp7.find('区')+1]
                elif tmp7.find('县')!= -1:
                    tmp8 = tmp7[:tmp7.find('县')+1]
                elif tmp7.find('市')!= -1:
                    tmp8 = tmp7[:tmp7.find('市')+1]

                tmp9 = result.find('strong', class_='total-price').text.strip()#解析总价
                tmp10 = result.find('strong', class_='h-price').text.strip()#解析单价

                query = [tmp8, tmp7, tmp6, tmp2[0].replace('平米',''), tmp2[1], tmp2[2], tmp2[3].replace('年建造',''), tmp9.replace('万',''), tmp10.replace('元/平',''),tmp4[2][:11]]
                esflist.append(query)
            except:
                print(str(page_number)+'-'+'有问题数据')
    print('%s 页已经处理完毕' %page_number)
    time.sleep(random.randint(0,2))

esflist=[]
for i in range(1,5989):
    get_page(i)
df = pd.DataFrame(esflist)
df.columns = ['区县','地址','小区','面积','户型','楼层','修建时间','总价','单价','更新时间']
df.to_csv('二手房列表.csv', index = False, encoding = "gbk")