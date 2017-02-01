import urllib.parse as up  
import re 
import urllib 
from http.cookiejar import CookieJar  

'''
def getTopics():
	zhihuTopics=[]
	url='https://www.zhihu.com/topics'
	req=urllib.request.Request(url)	
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
'''
def xsrf():  
	url = 'http://www.zhihu.com'  
	zhihu = urllib.request.urlopen(url).read().decode('utf-8')
	pattern = re.compile(r'name="_xsrf" value="(.*?)"/>')  
	match = pattern.findall(zhihu)  
	xsrf = match[0]  
	print(xsrf)
	return xsrf  

'''
def post_data():  
	data = dict()  
	data['_xsrf'] = xsrf  
	data['email'] = 'duchengli@hotmail.com'  
	data['password'] = 'dl820113'  
	data['rememberme'] = 'y'     
	post_data = up.urlencode(data).encode('utf-8') # 编译post数据  
	return post_data  
         
hdr={'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.8','Connection':'keep-alive','Content-Length':'95','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Host':'www.zhihu.com','Origin':'http://www.zhihu.com','RA-Sid':'DEADFC42-20150104-093648-9e5c2d-88ba9a','Referer':'http://www.zhihu.com/','User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','X-Requested-With':'XMLHttpRequest'}  
  
#cookie上创建一个opener  
def build_openner():  
	cookie = CookieJar()  
	cookie_handler = ur.HTTPCookieProcessor(cookie)  
	opener = ur.build_opener(cookie_handler)  
	return opener  


xsrf = xsrf()  
post_data = post_data()  
opener = build_openner()  
ur.install_opener(opener) # 安装opener  
  
def main():  
	url = 'http://www.zhihu.com/login'  
	req = ur.Request(url, post_data, hdr)  
	response = opener.open(req)  
	page = response.read()  
	#print(page)  
	# 测试成功与否  
	testurl = 'http://www.zhihu.com/settings/account'  
	req = ur.urlopen(testurl)  
	print(req.read().decode('utf-8'))  
      
#main()
'''
xsrf()