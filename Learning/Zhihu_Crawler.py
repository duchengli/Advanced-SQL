# -*- coding: utf-8 -*-
__author__ = 'duchengli'
import urllib
import random
import urllib.request
import re
import json

ck={'Cookie':'q_c1=682e0963d2364cf9923d89f16556d835|1483087248000|1474607524000; d_c0="AHCAbPVwlQqPTpljSnFi-LwJwv1Mjk3jIK4=|1474607524"; _za=cfe4b82c-5980-4982-8ffb-69283db42e9d; __utma=155987696.199938811.1485053109.1485053109.1485055035.2; __utmz=155987696.1485053109.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _zap=a15f5070-c330-47bd-9966-8e8d786e9b4f; l_cap_id="N2VhMzRmYjE1OGYxNGIyZGE0ZDVmYzU3MzdmYjQzNWY=|1483436311|bd9562715e3c22d3a7219bfe09393238ebdb57f5"; cap_id="MDBjMjZhNjk3ZGZjNDdlMmJhZmIyNDc0MjI5MDY2ODE=|1483436311|c82fb9f148c7e7dcc37e6e15e28a540faf26a20a"; r_cap_id="MTRlZGRhMDU2NTRjNGUzOWI5YzA5NmNlZGE3ZDRhZjQ=|1483436316|77c135ecc1ea4aa80a81eac36279d56fe630b355"; login="ZjVjYWQwYmQwODAxNGVmYmI0MjVmY2QxZjlkZWYzYjY=|1483436320|a87020e4a5bd8cc2a7722cc6b4a9c0501886af49"; z_c0=Mi4wQUFEQVRrUTdBQUFBY0lCczlYQ1ZDaGNBQUFCaEFsVk5JUDZTV0FEVjYyajl4a0VYMEdXYkF5Y3R5UV9VWktVZUhR|1485053180|3749455743a53566c42832d238a56bfa96e011e6; _xsrf=3c5a15d777a92df3b2be5c7fe49113ad; aliyungf_tc=AQAAALHw0Tbe4A4AshxHfXSaQd7LlMV8; __utmc=155987696; __utmv=155987696.100-1|2=registration_date=20141022=1^3=entry_date=20141022=1; __utmb=155987696.0.10.1485055035'}

hds={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}

def getTopics():
	zhihuTopics=[]
	url='https://www.zhihu.com/topics'
	ck.update(hds)
	req=urllib.request.Request(url,headers=ck)	
	source_code=urllib.request.urlopen(req,timeout=100).read().decode('utf-8')
	pattern=re.compile('<li.*?data-id="(.*?)"><a.*?>(.*?)</a></li>',re.S)
	results=re.findall(pattern,source_code)
	return zhihuTopics

def getSubTopic():
	url='https://www.zhihu.com/node/TopicsPlazzaListV2'
	contents=[]
	#values={'method':'next','params':'{"topic_id":'+topic.id+',"offset":0,"hash_id":""}'}
	values={'method':'next','params':'{"topic_id":'+'833'+',"offset":0,"hash_id":""}'}
	try:
		data=urllib.parse.urlencode(values)
		request=urllib.request.Request(url,data,headers=ck)
		response=urllib.request.urlopen(request)
		print(response.read().decode('utf-8'))
		print(data)
		#json_str = json.loads(response.read().decode('utf-8'))
            # 将获取到的数组转换成字符串
			#print(json_str)
	except:
		print('Error')
	
getSubTopic()

