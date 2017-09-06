#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Duchengli'

import requests
from bs4 import BeautifulSoup
import lxml

def get_page(pagenumber):
    page_url = 'http://esf.cdfgj.gov.cn/search?page=%d' %pagenumber
    r = requests.get(url = page_url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,'lxml')
        results = soup.find_all('div', class_='pan-item clearfix')
        for result in results:
            #解析房屋名称
            title = result.h2.a.text.strip()
            #解析房屋属性
            tmp1 = list(map(lambda x:x.string.strip() ,result.find('p',class_='p_hx').children))
            tmp2 = [x for x in tmp1 if x != '']
            #解析发布渠道
            tmp3 = list(map(lambda x: x.string.strip(), result.find('p', class_='p_gx').children))
            tmp4 = [x for x in tmp3 if x != '']
            print(title)
            print(tmp2)
            print(tmp4[0])
            print(tmp4[2])
            print('--------------------------------------------------------------------------------')
            #解析小区名称


get_page(1)