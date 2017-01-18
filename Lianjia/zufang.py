# -*- coding: utf-8 -*-
import urllib.request
import random
import lxml
from bs4 import BeautifulSoup
import time
from urllib.error import URLError
import socket
import csv 
socket.setdefaulttimeout(100)  

regions={'wuhou':{'cuqiao':8,'caojinlijiao':6,'chuanyin':15,'guangfuqiao':7,'gaoshengqiao':11,'huaxi':15,'hangkonglu':9,'hongpailou':18,'huochenanzhan':8,'longwan':6,'lidu':22,'shuangnan':30,'tongzilin':22,'wuhouci':3,'wuhoulijiao':9,'waishuangnan':26,'wudahuayuan':41,'xinshuangnan':10,'yiguanmiao':8,'yulin':11,'zongbei':25}}

def getzfinfo(zflinks):
	ck={'Cookie':'all-lj=0a26bbdedef5bd9e71c728e50ba283a3; lianjia_uuid=fe53c238-0ebd-4e4a-b442-858988aae3b4; lianjia_ssid=c0c5b78c-f3a6-48ac-8c0f-798836a7cb06; _ga=GA1.2.1328057788.1471959847; CNZZDATA1253492306=1662681935-1471957055-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471957055; _smt_uid=57bc5326.33a30384; CNZZDATA1254525948=797369229-1471955657-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471955657; CNZZDATA1255633284=1688411013-1471956256-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471956256; CNZZDATA1255604082=1834544274-1471958980-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471958980; CNZZDATA1256793290=1743366477-1471956471-null%7C1471956471; miyue_hide=%20index%20%20index%20%20index%20%20index%20; select_city=110000; lianjia_token=2.0068d6f9ba11cbe982797bd08b00855b61'}
	hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},{'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},{'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},{'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},{'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},{'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}]
	
	
	ck.update(hds[random.randint(0,len(hds)-1)])
	req=urllib.request.Request(zflinks,headers=ck)
	retry_time=20
	for i in range(retry_time):  
		try:
			source_code=urllib.request.urlopen(req,timeout=100).read().decode('utf-8')
			break
		except:
			if i<retry_time-1:
				continue
			else:
				print('多次尝试仍然失败!')

	soup=BeautifulSoup(source_code,'lxml')
	zf_list=soup.findAll('div',{'class':'info-panel'})
	for zf in zf_list:
		col1=zf.find('h2').find('a').text#房屋描述
		col2=zf.find('div',{'class':'where'}).find('span',{'class':'region'}).text#小区名字
		col3=zf.find('div',{'class':'where'}).find('span',{'class':'zone'}).text#户型
		col4=zf.find('div',{'class':'where'}).find('span',{'class':'meters'}).text#面积
		col5=zf.find('div',{'class':'other'}).find('div',{'class':'con'}).find('a').text#小区域
		col6=zf.find('div',{'class':'price'}).find('span',{'class':'num'}).text#租金
		col7=zf.find('div',{'class':'price-pre'}).text#更新时间
		col8=zf.find('div',{'class':'square'}).find('span',{'class':'num'}).text#看房人数
		col9=rg1
		col10=rg2
		#col13=zflinks
		if col1+'-'+col10 in zfkeys:
			print('发现重复记录'+col1+'-'+col10)
		else:
			zfkeys.setdefault(col1+'-'+col10,'inserted')
			query=[col1,col2,col3,col4,col5,col6,col7,col8]
			try:
				writer.writerow(query)
			except:
				print('编码错误无法插入!')
	time.sleep(10)
		
csvfile=open('d:\\zf.csv','w+',newline='',encoding='utf-8')
writer=csv.writer(csvfile)
writer.writerow([u'房屋描述',u'小区名称',u'户型',u'面积',u'小区域',u'租金',u'更新时间',u'看房人数'])
zfkeys={}
errorlinks={}
for rg1 in regions:	
	for rg2 in regions.get(rg1):
		for page_number in range(1,regions.get(rg1).get(rg2)+10):
			getzfinfo('http://cd.lianjia.com/zufang/'+rg2+'/pg'+str(page_number)+'/')
csvfile.close()


