# -*- coding: utf-8 -*-
__author__ = 'duchengli'
import urllib
import requests
import re
import json

headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}

def getTopics():
	session=requests.Session()	
	url='https://www.zhihu.com/topics'
	req=session.get(url,headers=headers)
	pattern=re.compile('<li.*?data-id="(.*?)"><a.*?>(.*?)</a></li>',re.S)
	results=re.findall(pattern,req.text)
	return results

def getSubTopic():
	url='https://www.zhihu.com/node/TopicsPlazzaListV2'
	params={'method':'next','params':'{"topic_id":833,"offset":0,"hash_id":"d28e1067630ce1840d3a3fe25bd6a0ad"}'}
	requests.post(url,params)
	print(requests.get(url,params))
	#request=urllib.request.Request(url,params,headers=headers)
	#response=urllib.request.urlopen(request)
	#print(response.read().decode('utf-8'))
	#print(s)
	#s
	#json_str = json.loads(response.read().decode('utf-8'))
            # 将获取到的数组转换成字符串
			#print(json_str)
	
getSubTopic()
'''
print(getTopics())
'''