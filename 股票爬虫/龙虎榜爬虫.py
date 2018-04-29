#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'Duchengli'

import requests
import json
#import numpy as np



#读取同花顺的自选股数据
def THS():
    f = open('THS.txt')
    lines = f.readlines()
    for line in lines:
        if len(line.strip()) != 0 and not line.startswith('代码'):
#           print([line.split('\t')[0],line.split('\t')[1]])
            THS_list.append([line.split('\t')[0],line.split('\t')[1]])

#读取最近3个月东方财富网龙虎榜数据
def LHB():
    url = 'http://data.eastmoney.com/DataCenter_V3/stock2016/StockStatistic/pagesize=5000,page=1,sortRule=-1,sortType=,startDate=2018-01-27,endDate=2018-04-27,gpfw=0,js=var%20data_tab_3.html?rt=25414064'
    req = requests.get(url=url,timeout=5)
    content = req.text
    dict1 = json.loads(content[content.find('=')+1:])
    for item in dict1['data']:
        LHB_list.append(dict(item)['SName'])

#同时满足龙虎榜和自选股的股票
def filter():
    for item in THS_list:
        if item[1] in LHB_list:
            Final_list.append(item[0])

THS_list = []
LHB_list = []
Final_list = []

THS()
LHB()
filter()

# print('同花顺自选股一共有%d条' %len(THS_list))
# print('龙虎榜一共有%d条' %len(LHB_list))
# print('同时上榜的股票一共有%d条' %len(Final_list))
# #
# # print(THS_list)
# # print(LHB_list)
#
# # for item in Final_list:
# #     print(item[2:])

