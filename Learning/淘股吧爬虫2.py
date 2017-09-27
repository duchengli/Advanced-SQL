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

    page_url = 'https://www.taoguba.com.cn/index?pageNo=%d&blockID=0&flag=1' % page_number
    retry_time = 20

    for i in range(retry_time):
        try:
            r = requests.get(url=page_url)
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
                create_date = result.find('li', class_='pcdj03').text.strip()  # 最后回帖时间
                reply_date = result.find('li', class_='pcdj06').text.strip()  # 发帖时间
                count = result.find('li', class_='pcdj04').text.strip()  # 回帖浏览
                tmp_list = [title,author,create_date,reply_date,count,link]
                print(tmp_list)
                writer.writerow(tmp_list)
        except Exception:
            print(u'有问题')

csvfile = open('d:\\taoguba.CSV', 'w', newline='')
writer = csv.writer(csvfile)
writer.writerow([u'title', u'author', u'create_date',u'reply_date', u'count', u'link'])

for i in range(1, 20349):
    print('第%d页' % i)
    get_page(i)
    time.sleep(random.randint(5, 15))

csvfile.close()
