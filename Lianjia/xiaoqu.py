# -*- coding: utf-8 -*-
import urllib.request
import random
from bs4 import BeautifulSoup
import time
import csv

ck={'Cookie':'all-lj=0a26bbdedef5bd9e71c728e50ba283a3; lianjia_uuid=fe53c238-0ebd-4e4a-b442-858988aae3b4; lianjia_ssid=c0c5b78c-f3a6-48ac-8c0f-798836a7cb06; _ga=GA1.2.1328057788.1471959847; CNZZDATA1253492306=1662681935-1471957055-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471957055; _smt_uid=57bc5326.33a30384; CNZZDATA1254525948=797369229-1471955657-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471955657; CNZZDATA1255633284=1688411013-1471956256-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471956256; CNZZDATA1255604082=1834544274-1471958980-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471958980; CNZZDATA1256793290=1743366477-1471956471-null%7C1471956471; miyue_hide=%20index%20%20index%20%20index%20%20index%20; select_city=110000; lianjia_token=2.0068d6f9ba11cbe982797bd08b00855b61'}
#User Agents for random choose
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},{'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},{'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},{'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},{'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},{'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}]
regions={'jinjiang':36,'qingyang':51,'wuhou':59,'gaoxin7':20,'chenghua':30,'jinniu':56,'tianfuxinqu':10}
csvfile=open('d:\\xq.csv','w',newline='')
writer=csv.writer(csvfile)
writer.writerow([u'小区名称',u'大区域',u'小区域',u'成交统计',u'出租统计',u'建造时间',u'小区均价',u'在售二手房'])
xiaoqukey={}
for rg in regions:  
	for page_number in range(1,regions.get(rg)+5):
		ck.update(hds[random.randint(0,len(hds)-1)])        
		req = urllib.request.Request(u"http://cd.lianjia.com/xiaoqu/"+rg+'/pg'+str(page_number)+'/',headers=ck)	
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
		soup = BeautifulSoup(source_code,'lxml')
		xiaoqu_list=soup.findAll('li',{'class':'clear'})
		for xq in xiaoqu_list:
			col1=xq.find('div',{'class':'title'}).text
			col2=xq.find('a',{'class':'district'}).text
			col3=xq.find('a',{'class':'bizcircle'}).text
			col4=xq.find('div',{'class':'houseInfo'}).text.split('|')[0]
			col5=xq.find('div',{'class':'houseInfo'}).text.split('|')[1]
			col6=xq.find('div',{'class':'positionInfo'}).text.split()[3]
			col7=xq.find('div',{'class':'totalPrice'}).text.split('/')[0]
			col8=xq.find('div',{'class':'sellCount'}).find('span').text
			if col1+'-'+col2+'-'+col3 in xiaoqukey:
				print('Duplicate item found!'+col1+'-'+col2+'-'+col3)
			else:
				xiaoqukey.setdefault(col1+'-'+col2+'-'+col3,'inserted')              
				query=[col1,col2,col3,col4,col5,col6,col7,col8]
				writer.writerow(query)
		time.sleep(10)        
    #logfile.close()
csvfile.close()