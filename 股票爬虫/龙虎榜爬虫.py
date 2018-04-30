#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'Duchengli'

import requests
import json

#读取最近3个月东方财富网龙虎榜数据
def LHB():
    url = 'http://data.eastmoney.com/DataCenter_V3/stock2016/StockStatistic/pagesize=5000,page=1,sortRule=-1,sortType=,startDate=2018-04-27,endDate=2018-04-27,gpfw=0,js=var%20data_tab_3.html?rt=25414064'
    req = requests.get(url=url,timeout=5)
    content = req.text
    dict1 = json.loads(content[content.find('=')+1:])
    for item in dict1['data']:
        #print(dict(item)['SName'])
        #LHB_list.append(dict(item)['SName'])
        for k,v in item.items():
            print(k + ':' + v)
LHB()


