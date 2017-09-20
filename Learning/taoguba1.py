#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Duchengli'

import requests
from bs4 import BeautifulSoup
import lxml
import csv

def get_page(pagenumber):
    page_url = 'https://www.taoguba.com.cn/default?pageNo=%d#9527' %pagenumber

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
        results = soup.find_all('div', class_='p_listop')
        for result in results:
            try:
                print(result.h2.a.text.strip())


            except:
                print('有问题')

for i in range(1,128):
    get_page(i)
    time.sleep(10)