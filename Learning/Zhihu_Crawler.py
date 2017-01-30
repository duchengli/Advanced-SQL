# -*- coding: utf-8 -*-
__author__ = 'duchengli'
import urllib
import random
import urllib.request
import re
import json
import requests
import ConfigParser

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
		print('未能获取数据')

		


def create_session():
    cf=ConfigParser.ConfigParser()
    cf.read('config.ini')
    cookies=cf.items('cookies')
    cookies=dict(cookies)
    from pprint import pprint
    pprint(cookies)
    email=cf.get('info','email')
    password=cf.get('info','password')

    session=requests.session()
    login_data= {'email': email, 'password': password}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
        'Host': 'www.zhihu.com',
        'Referer': 'http://www.zhihu.com/'
    }
    r = session.post('http://www.zhihu.com/login/email', data=login_data, headers=header)
    if r.json()['r'] == 1:
        print 'Login Failed, reason is:',
        for m in r.json()['data']:
            print r.json()['data'][m]
        print 'So we use cookies to login in...'
        has_cookies = False
        for key in cookies:
            if key != '__name__' and cookies[key] != '':
                has_cookies = True
                break
        if has_cookies is False:
            raise ValueError('请填写config.ini文件中的cookies项.')
        else:
            # r = requests.get('http://www.zhihu.com/login/email', cookies=cookies) # 实现验证码登陆
            r = session.get('http://www.zhihu.com/login/email', cookies=cookies) # 实现验证码登陆

    with open('login.html', 'w') as fp:
        fp.write(r.content)

    return session, cookies


if __name__ == '__main__':
    requests_session, requests_cookies = create_session()

    # url = 'http://www.zhihu.com/login/email'
    url = 'http://www.zhihu.com/topic/19552832'
    # content = requests_session.get(url).content # 未登陆
    # content = requests.get(url, cookies=requests_cookies).content # 已登陆
    content = requests_session.get(url, cookies=requests_cookies).content # 已登陆
    with open('url.html', 'w') as fp:
        fp.write(content)

