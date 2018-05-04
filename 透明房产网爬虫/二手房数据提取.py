#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'Duchengli'
# 透明房产网二手房爬虫
# mj参数规定了面积在100-200平方内的房源

import requests
from bs4 import BeautifulSoup
import lxml
import time
import random
import re
import math
import csv
import pickle

datafile = open('esflist.pkl', 'rb')
esf = pickle.load(datafile)
datafile.close()

for k,v in esf.items():
    if '龙湖三千' in v[0]:
        print(k,v)