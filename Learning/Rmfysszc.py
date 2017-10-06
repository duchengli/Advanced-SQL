# -*- coding: utf-8 -*-
import urllib.request
import random
import lxml
from lxml import etree
from bs4 import BeautifulSoup
import time
from urllib.error import URLError
import socket
import csv 
socket.setdefaulttimeout(100)  

def getpages(link):
	headers=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},{'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},{'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},{'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},{'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},{'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}]
	
	req=urllib.request.Request(link,headers=headers[random.randint(0,len(headers)-1)])
	retry_time=20
	for i in range(retry_time):  
		try:
			source_code=urllib.request.urlopen(req,timeout=100).read().decode('utf-8')
			break
		except:
			if i<retry_time-1:
				time.sleep(10) 
				continue
			else:
				print('多次尝试仍然失败!')
	
	soup=BeautifulSoup(source_code,'lxml')
	trs=soup.find('div',{'class':'objlist'}).find('table').findAll('tr')
	for tr in trs:
		tmplist=[]
		for td in tr.findAll('td'):
			try:
				tmplist.append(td.text.replace('\r','').replace('\n','').replace(' ',''))
				tmplist.append(td.find('a').attrs['href'])
			except:
				print('空行')
		#print(tmplist)
		if tmplist!=[]: 
			if tmplist in listkeys or tmplist[0].strip()=='项目名称':
				print('发现重复记录',tmplist)
			else:
				listkeys.append(tmplist)
				try:
					writer.writerow(tmplist)
				except:
					print('编码错误无法插入!')
	time.sleep(10)
		
csvfile=open('d:\\rmfysszc.csv','w+',newline='',encoding='utf-8')
writer=csv.writer(csvfile)
writer.writerow([u'项目名称',u'法院',u'类别',u'所在地',u'成交结果',u'起拍价',u'发布日期'])
listkeys=[]
for page_number in range(1,176):
	getpages('http://www1.rmfysszc.gov.cn/projects.shtml?s=q&dh=3&cc=510100&c=510000&tt=111&fid=%2c%2c&gpstate=1&page='+str(page_number))
csvfile.close()


