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

regions={'jinjiang':{'chuanshi':8,'dongguangxiaoqu':6,'dongdalu':5,'donghu':17,'hongxinglu':7,'hejiangting':24,'jiuyanqiao':23,'jingjusi':5,'liulichang':14,'lianhua2':8,'langudi':8,'panchenggang':11,'sanshengxiang':23,'shuinianhe':7,'shahebao':11,'sanguangtang':8,'yanshikou':23,'zhuojincheng':19},'qingyang':{'babaojie':18,'beisen':23,'caoshijie':17,'caotang':8,'funanxinqu':18,'guanghuapaoxiao':19,'huanhuaxi':5,'jinsha':14,'kuanzhaixiangzi':5,'renmingongyuan':14,'taishenglu':12,'waiguanghua':31,'wanjiawan':14,'waijinsha':14,'xidan1':7,'xinancaida':17,'youpindao':7},'wuhou':{'cuqiao':9,'caojinlijiao':22,'chuanyin':12,'guangfuqiao':6,'gaoshengqiao':13,'huaxi':23,'hangkonglu':12,'hongpailou':28,'huochenanzhan':10,'longwan':9,'lidu':21,'shuangnan':31,'tongzilin':23,'wuhouci':3,'wuhoulijiao':18,'waishuangnan':28,'wudahuayuan':31,'xinshuangnan':13,'yiguanmiao':12,'yulin':8,'zongbei':16},'gaoxin7':{'chengnanyijia':17,'dayuan':39,'dongyuan2':6,'fangcao':14,'jinrongcheng':27,'shenxianshu':20,'shiyiyiyuan':16,'tianfuchangcheng':13,'xinbei':11,'xinhuizhan':37,'zijing':12,'zhonghe':14},'chenghua':{'balixiaoqu':18,'chengyulijiao':16,'dongkezhan':5,'dongwuyuan':19,'dongjiaojiyi':14,'jianshelu':13,'ligongda':4,'longtansi':2,'lijiatuo':10,'mengzhuiwan':20,'smguangchang':11,'simaqiao':24,'wanxiangcheng1':29,'wannianchang':23,'xinhuagongyuan':8},'jinniu':{'chadianzi':16,'fuqinxiaoqu':9,'gaojiazhuang':14,'guobin':15,'huapaifang':20,'huaqiaocheng3':14,'huazhaobi':12,'jiulidi':10,'jinniuwanda':19,'jinfu':15,'maanlu':12,'shirenxiaoqu':5,'shuhanlu':10,'shawanhuizhan':16,'tonghuimen':9,'wukuaishi':30,'xinanjiaoda':12,'yipintianxia':11,'yingmenkou':16},'tianfuxinqu':{'guangdou':5,'huayang':44,'haiyanggongyuan':18,'lushan':20,'nanhu':42,'sihe':10,'yuanda':6,'yajule':5,'zhongde':9}}

def getesfinfo(esflinks):
	ck={'Cookie':'all-lj=0a26bbdedef5bd9e71c728e50ba283a3; lianjia_uuid=fe53c238-0ebd-4e4a-b442-858988aae3b4; lianjia_ssid=c0c5b78c-f3a6-48ac-8c0f-798836a7cb06; _ga=GA1.2.1328057788.1471959847; CNZZDATA1253492306=1662681935-1471957055-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471957055; _smt_uid=57bc5326.33a30384; CNZZDATA1254525948=797369229-1471955657-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471955657; CNZZDATA1255633284=1688411013-1471956256-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471956256; CNZZDATA1255604082=1834544274-1471958980-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471958980; CNZZDATA1256793290=1743366477-1471956471-null%7C1471956471; miyue_hide=%20index%20%20index%20%20index%20%20index%20; select_city=110000; lianjia_token=2.0068d6f9ba11cbe982797bd08b00855b61'}
	hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},{'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},{'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},{'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},{'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},{'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}]
	
	
	ck.update(hds[random.randint(0,len(hds)-1)])
	req=urllib.request.Request(esflinks,headers=ck)
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
	ershoufang_list=soup.findAll('div',{'class':'info clear'})
	for esf in ershoufang_list:
		col1=esf.find('div',{'class':'title'}).find('a').text#房屋描述
		col2=esf.find('div',{'class':'houseInfo'}).find('a').text#小区名字
		col3=esf.find('div',{'class':'houseInfo'}).text.split('|')[1]#户型
		col4=esf.find('div',{'class':'houseInfo'}).text.split('|')[2]#面积
		col5=esf.find('div',{'class':'houseInfo'}).text.split('|')[3]#朝向
		col6=rg2
		col7=esf.find('div',{'class':'positionInfo'}).find('span').text#楼层
		col8=esf.find('div',{'class':'totalPrice'}).find('span').text#总价
		col9=esf.find('div',{'class':'unitPrice'}).find('span').text#单价
		col10=esf.find('div',{'class':'followInfo'}).text.split('/')[0]#看房人数
		col11=rg1
		col12=rg2
		#col13=esflinks
		if col1+'-'+col2 in esfkeys:
			print('发现重复记录'+col1+'-'+col2)
		else:
			esfkeys.setdefault(col1+'-'+col2,'inserted')
			query=[col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12]
			try:
				writer.writerow(query)
			except:
				print('编码错误无法插入!')
	time.sleep(10)
		
csvfile=open('d:\\esf.csv','w+',newline='',encoding='utf-8')
writer=csv.writer(csvfile)
writer.writerow([u'房屋描述',u'小区名称',u'户型',u'面积',u'朝向',u'小区域',u'楼层',u'总价',u'单价',u'看房人数',u'大区域',u'小区域2'])
esfkeys={}
errorlinks={}
for rg1 in regions:	
	for rg2 in regions.get(rg1):
		for page_number in range(1,regions.get(rg1).get(rg2)+10):
			getesfinfo('http://cd.lianjia.com/ershoufang/'+rg2+'/pg'+str(page_number)+'/')
csvfile.close()


