#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Duchengli'

import requests
from bs4 import BeautifulSoup
import lxml
import csv

def get_page(pagenumber):
    page_url = 'http://esf.cdfgj.gov.cn/search?page=%d' %pagenumber

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
        results = soup.find_all('div', class_='pan-item clearfix')
        for result in results:
            try:
                #解析房屋名称
                title = result.h2.a.text.strip()
                #解析房屋属性
                tmp1 = list(map(lambda x:x.string.strip() ,result.find('p',class_='p_hx').children))
                tmp2 = [x for x in tmp1 if x != '']
                #解析发布渠道
                tmp3 = list(map(lambda x: x.string.strip(), result.find('p', class_='p_gx').children))
                tmp4 = [x for x in tmp3 if x != '']
                #解析小区名称
                tmp5 = result.find('p',class_='p_hx').next_sibling.next_sibling.text.strip()
                #解析总价
                tmp6 = result.find('strong', class_='total-price').text.strip()
                #解析单价
                tmp7 = result.find('strong', class_='h-price').text.strip()
                query = [title, tmp2[0], tmp2[1], tmp2[2], tmp2[3], tmp4, tmp5, tmp6, tmp7]
                writer.writerow(query)

            except:
                print(title+'-'+'有问题')

csvfile=open('d:\\touming.csv','w+',newline='')
writer=csv.writer(csvfile)
#esfkeys={}
for i in range(1,100):
    get_page(i)
csvfile.close()


