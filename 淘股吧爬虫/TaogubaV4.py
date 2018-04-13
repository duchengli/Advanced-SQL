#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Duchengli'
# 淘股吧帖子爬虫V3
# 可以根据发布时间生成不同的文档
# 2018-03-29第三次创建

import requests
from bs4 import BeautifulSoup
import lxml
import os

#get_post_lists用于获取帖子列表，包括标题，发帖时间和帖子链接
def get_post_lists(page_number):
    page_url = 'https://www.taoguba.com.cn/index?pageNo=%d&blockID=1&flag=1' % page_number
    retry_time = 5
    for i in range(retry_time):
        try:
            r = requests.get(page_url,timeout=5)
            break
        except:
            if i < retry_time - 1:
                continue
            else:
                break

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        results = soup.find_all('li', class_='pcdj02')
        if results:
            for result in results:
                try:
                    post_title = result.a.text
                    post_date = result.parent.find('li',class_ = 'pcdj06').text
                    post_link = 'https://www.taoguba.com.cn/' + result.a.get('href')
                    # 获取存储回帖/浏览/加油券三项数据
                    post_reply = int(result.parent.find('li', class_='pcdj04').text.split('/')[0])
                    post_view = int(result.parent.find('li', class_='pcdj04').text.split('/')[1])

                    likes = result.parent.find_all('li', class_='pcdj05')
                    tmp_str = ''
                    for like in likes:
                        tmp_str = tmp_str + '/' + like.text
                    post_like = int(tmp_str.split('/')[3])

                    if post_reply > 0 and post_like > 0:  # 判断是否是热帖
                        print(post_title, post_date, post_link, post_view, post_reply, post_like)
                        post_lists.append((post_title,post_date,post_link))
                except:
                    pass

#save_post_texts以日期为文件名保存当日帖子的内容，参数post是一个元组，标题，发帖时间和帖子链接
def save_post_texts(post):
    file_name = os.getcwd() + '\\' + post[1] + '.txt'
    retry_time = 5
    for i in range(retry_time):
        try:
            r = requests.get(url=post[2], timeout=5)
            break
        except:
            if i < retry_time - 1:
                continue
            else:
                print('爬取 %s 时发生错误，已经保存到错误列表，稍后将重新爬取' %post[2])
                err_lists.append(post[2])
                break

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        result = soup.find('div', class_='p_coten')
        if result:
            try:
                f = open(file_name,'a+',encoding='utf-8')
                f.write(result.text)
                f.close()
            except FileNotFoundError:
                f = open(file_name, 'w+', encoding='utf-8')
                f.write(result.text)
                f.close()

os.chdir(r'd:\Spider')
post_lists = []
err_lists = []
j = 1

for i in range(1,10):
#    print('正在分析第%d页' % i)
    get_post_lists(i)
print('解析完毕，一共有%d条帖子需要爬取' %len(post_lists))

for post in post_lists:
#    print('正在爬取第%d条帖子' %j)
    save_post_texts(post)
    j = j + 1
print('爬取完毕，一共爬取了%d条帖子，成功%d条，失败%d条' %(len(post_lists),len(post_lists)-len(err_lists),len(err_lists)))