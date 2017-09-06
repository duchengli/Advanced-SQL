#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Duchengli'

import requests
from bs4 import BeautifulSoup
import lxml

r = requests.get(url = 'http://esf.cdfgj.gov.cn/search?page=1')

if r.status_code == 200:
    soup = BeautifulSoup(r.text,'lxml')
    result = soup.find_all('div', class_='pan-item clearfix')

    print(result[0].h2.a.text.strip())
    tmp1 = list(map(lambda x:x.string.strip() ,result[0].find('p',class_='p_hx').children))
    #print(list(tmp))
    print(type(tmp1))