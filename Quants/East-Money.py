import urllib.request
import demjson
import random
import csv

# 获取页数
def get_pages_count():
	url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=GG&sty=GDRS&st=6&sr=-1&p=1'
	url += '&ps=50&js=var%20wPPmivFX={pages:(pc),data:[(x)]}&mkt=1&fd=2016-9-30&rt=49437052'
	wp = urllib.request.urlopen(url)
	data = wp.read().decode('utf8')
	start_pos = data.index('=')
	json_data = data[start_pos + 1:]
	dict = demjson.decode(json_data)
	pages =dict['pages']
	return pages

# 获取链接列表
def get_url_list(start,end):
	url_list=[]
	while(start<=end):
		url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=GG&sty=GDRS&st=6&sr=-1&p=%d' %start
		url += '&ps=50&js=var%20wPPmivFX={pages:(pc),data:[(x)]}&mkt=1&fd=2016-9-30&rt=49437052'
		url_list.append(url)
		start+=1
	return url_list

ck={'Cookie':'all-lj=0a26bbdedef5bd9e71c728e50ba283a3; lianjia_uuid=fe53c238-0ebd-4e4a-b442-858988aae3b4; lianjia_ssid=c0c5b78c-f3a6-48ac-8c0f-798836a7cb06; _ga=GA1.2.1328057788.1471959847; CNZZDATA1253492306=1662681935-1471957055-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471957055; _smt_uid=57bc5326.33a30384; CNZZDATA1254525948=797369229-1471955657-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471955657; CNZZDATA1255633284=1688411013-1471956256-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471956256; CNZZDATA1255604082=1834544274-1471958980-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471958980; CNZZDATA1256793290=1743366477-1471956471-null%7C1471956471; miyue_hide=%20index%20%20index%20%20index%20%20index%20; select_city=110000; lianjia_token=2.0068d6f9ba11cbe982797bd08b00855b61'}
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},{'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},{'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},{'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},{'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},{'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}]


def save_json_data():
	pages =get_pages_count()
	url_list =get_url_list(1,pages)
#	url_list =get_url_list(1,1)
	count=0
	for url in url_list:
		ck.update(hds[random.randint(0,len(hds)-1)])
		req=urllib.request.Request(url,headers=ck)
		retry_time=20
		for i in range(retry_time):
			try:
				data=urllib.request.urlopen(req,timeout=100).read().decode('utf-8')
				break
			except:
				if i<retry_time-1:
					continue
				else:
					print('多次尝试仍然失败!')
#		data=source_code.read()
#		print(source_code)
		start_pos = data.index('=')
		json_data = data[start_pos + 1:]
		dict = demjson.decode(json_data)
		list_data = dict['data']
#		print(len(list_data))
		for i in range(len(list_data)):
			if len(list_data[i].split(','))==16:
				tmp_list=[]
#				print(len(list_data[i].split(',')))
				for j in range(12):
					tmp_list.append(list_data[i].split(',')[j])
				writer.writerow(tmp_list)


csvfile=open('d:\\eastmoney.csv','w',newline='')
writer=csv.writer(csvfile)
writer.writerow([u'代码',u'股票简称',u'股东人数',u'较上期变化',u'人均流通股',u'前十大流通股东持股数量',u'前十大流通股东占流通股比例',u'前十大股东持股数量','前十大股东占总股本比例','机构持股数量','机构持股占流通A股本比例','筹码集中度'])				

save_json_data()
   