# -*- coding: utf-8 -*-
__author__ = 'duchengli'
import urllib
import random
import urllib.request
import re
import json

ck={'Cookie':'all-lj=0a26bbdedef5bd9e71c728e50ba283a3; lianjia_uuid=fe53c238-0ebd-4e4a-b442-858988aae3b4; lianjia_ssid=c0c5b78c-f3a6-48ac-8c0f-798836a7cb06; _ga=GA1.2.1328057788.1471959847; CNZZDATA1253492306=1662681935-1471957055-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471957055; _smt_uid=57bc5326.33a30384; CNZZDATA1254525948=797369229-1471955657-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471955657; CNZZDATA1255633284=1688411013-1471956256-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471956256; CNZZDATA1255604082=1834544274-1471958980-http%253A%252F%252Fbzclk.baidu.com%252F%7C1471958980; CNZZDATA1256793290=1743366477-1471956471-null%7C1471956471; miyue_hide=%20index%20%20index%20%20index%20%20index%20; select_city=110000; lianjia_token=2.0068d6f9ba11cbe982797bd08b00855b61'}

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},{'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},{'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},{'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},{'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},{'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}]

def getTopics():
	zhihuTopics = []
	url = 'https://www.zhihu.com/topics'
	ck.update(hds[random.randint(0,len(hds)-1)])
	req=urllib.request.Request(url,headers=ck)	
	source_code=urllib.request.urlopen(req,timeout=100).read().decode('utf-8')
	pattern = re.compile('<li.*?data-id="(.*?)"><a.*?>(.*?)</a></li>',re.S)
	results = re.findall(pattern,source_code)
	print(results)
	for n1 in results:
		print(n1[0],n1[1])
		#topic = Topic(n1[0],n1[1])
		#zhihuTopics.append(topic)
	#return zhihuTopics

defgetSubTopic(topic):
    url = 'https://www.zhihu.com/node/TopicsPlazzaListV2'
    isGet = True;
    offset = -20;
    contents = []
    while isGet:
        offset = offset + 20
        values = {'method': 'next', 'params': '{"topic_id":'+topic.id+',"offset":'+str(offset)+',"hash_id":""}'}
        try:
            data = urllib.parse.urlencode(values)(values)
            request = urllib.request.Request(url,data,headers)
            response = urllib.request.urlopen(request)
            json_str = json.loads(response.read().decode('utf-8'))
            # 将获取到的数组转换成字符串
            topicMsg = '.'.join(json_str['msg'])
            pattern = re.compile('<strong>(.*?)</strong>.*?<p>(.*?)</p>',re.S)
            results = re.findall(pattern,topicMsg)
            if len(results) ==0:
                isGet =False
            for n in results:
                content = Content(n[0],n[1])
                contents.append(content)
                print n[0],'->'+n[1]
        excepturllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"错误原因",e
    file = open(topic.name+'.txt','w')
    wiriteLog(contents,file)
    return contents