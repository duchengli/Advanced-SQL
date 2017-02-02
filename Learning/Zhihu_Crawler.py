# -*- coding: utf-8 -*-

import http.cookiejar
import urllib
import requests
import re
import time
import os.path
from PIL import Image

agent='Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers={'Host':'www.zhihu.com','Referer':'https://www.zhihu.com/','User-Agent':agent}
session=requests.session()
session.cookies=http.cookiejar.CookieJar()

def isLogin():
	url='https://www.zhihu.com/settings/profile'
	login_code=session.get(url,headers=headers,allow_redirects=False).status_code
	if login_code == 200:
		return True
	else:
		return False

def login(secret,account):
	if re.match(r"^1\d{10}$",account):
		print('使用手机号登录\n')
		post_url='https://www.zhihu.com/login/phone_num'
		postdata={
			#'_xsrf': get_xsrf(),
			'password': secret,
			'remember_me': 'true', 
			'phone_num': account,
		}
	else:
		if "@" in account:
			print('使用邮箱登录\n')
		else:
			print("你的账号输入有问题，请重新登录")
			return 0
		post_url='https://www.zhihu.com/login/email'
		postdata={
			#'_xsrf': get_xsrf(),
			'password': secret,
			'remember_me': 'true',
			'email': account,
		}
	try:
		# 不需要验证码直接登录成功
		login_page=session.post(post_url,data=postdata,headers=headers)
		login_code=login_page.text
		print(login_page.status_code)
		print(login_code)
	except:
		# 需要输入验证码后才能登录成功
		postdata['captcha']=get_captcha()
		login_page=session.post(post_url,data=postdata,headers=headers)
		login_code=eval(login_page.text)
		print(login_code['msg'])
	#print(session.cookies)
	
if __name__ == '__main__':
	if isLogin():
		print('您已经登录')
	else:
		account=input('请输入你的用户名\n>')
		secret=input('请输入你的密码\n>')
		login(secret,account)
		login_code=session.get('https://www.zhihu.com/settings/profile',headers=headers,allow_redirects=False)
		print(login_code.text)
		