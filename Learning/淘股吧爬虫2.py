#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Duchengli'

import requests
from bs4 import BeautifulSoup
import lxml
import csv
import time
import random


def get_page(page_number):

    cookies = {}
    raw_cookies='bdshare_firstime=1504517693631; UM_distinctid=15e4c3e20f0449-05e2995747fa85-40544130-1fa400-15e4c3e20f145b; CNZZDATA1574657=cnzz_eid%3D1553734631-1504512598-null%26ntime%3D1506645663; JSESSIONID=ce0108cb-d05a-4848-aa97-b4606f56d9ac; tgbuser=1694795; tgbpwd=2A1FE2398FBsld6cznj6vyhdjl'

    for line in raw_cookies.split(';'):
        key,value = line.split('=',1)
        cookies[key] = value

    page_url = 'https://www.taoguba.com.cn/index?pageNo=%d&blockID=0&flag=1' % page_number
    retry_time = 20

    for i in range(retry_time):
        try:
            r = requests.get(url=page_url, cookies=cookies)
            break
        except Exception:
            if i < retry_time - 1:
                continue
            else:
                print('多次尝试仍然失败!')

    if r.status_code == 200:
        try:
            soup = BeautifulSoup(r.text, 'lxml')
            results = soup.find('div', class_='p_list').find_all('ul')
            for result in results:
                title = result.find('li', class_='pcdj02').a.text.strip()  # 标题
                link = 'https://www.taoguba.com.cn/' + result.find('li', class_='pcdj02').a.get('href')
                author = result.find('li', class_='pcdj08').a.text.strip()  # 作者
                create_date = result.find('li', class_='pcdj06').text.strip()  # 发帖时间
                reply_date = result.find('li', class_='pcdj03').text.strip()  # 最后回复时间
                count = result.find('li', class_='pcdj04').text.strip()  # 回帖浏览
                tmp_list = [title,author,create_date,reply_date,count,link]
                print(tmp_list)
                writer.writerow(tmp_list)
        except(TypeError, KeyError) as e:
            pass

csvfile = open('d:\\taoguba20170928(4).CSV', 'w', newline='', encoding='utf-8')
writer = csv.writer(csvfile)
writer.writerow([u'title', u'author', u'create_date',u'reply_date', u'count', u'link'])

for i in range(14736, 20350):
    print('第%d页' % i)
    get_page(i)
    #time.sleep(random.randint(1,5))

csvfile.close()
