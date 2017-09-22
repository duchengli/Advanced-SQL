#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Duchengli'

import  requests
from bs4 import BeautifulSoup
import  lxml
import  csv
import time

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

                print('https://www.taoguba.com.cn/'+ result.h2.a.get('href'))

                print('\n')


            except:
                print('有问题')

for i in range(1,31):
    print('第%d页' %i)
    print('\n')
    print('----------------------------------------------------------------------------------------------------')
    print('\n')
    get_page(i)

    #time.sleep(10)