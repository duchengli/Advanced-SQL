import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

# 获取链接列表
# def get_url_list(start,end):
# 	url_list=[]
# 	while(start<=end):
# 		url = 'https://www.airbnbchina.cn/s/%E6%88%90%E9%83%BD--%E5%9B%9B%E5%B7%9D%E7%9C%81--%E4%B8%AD%E5%9B%BD?guests=1&adults=1&children=0&infants=0&checkin=2017-03-22&checkout=2017-03-23&ss_id=fv5xtw1n&source=bb&cdn_cn=1&page='+str(start)
# 		url += '&allow_override%5B%5D=&ne_lat=30.700951735091245&ne_lng=104.20669555664062&sw_lat=30.52376985943266&sw_lng=103.95675659179688&zoom=12&search_by_map=true&s_tag=3eLfCN0H'
# 		url_list.append(url)
# 		start+=1
# 	return url_list


# def save_json_data():
# #	url_list =get_url_list(1,17)
# 	url_list =get_url_list(1,1)
# 	count=0
# 	for url in url_list:
# 		req=urllib.request.Request(url,headers=ck)
# 		retry_time=20
# 		for i in range(retry_time):
# 			try:
# 				data=urllib.request.urlopen(req,timeout=100).read()
# 				break
# 			except:
# 				if i<retry_time-1:
# 					continue
# 				else:
# 					print('多次尝试仍然失败!')
# #		data=source_code.read()
# #		print(source_code)
# 		print(data)
# 		#json_data = data[16:]
#
#
# 		dict = demjson.decode(json_data)
# 		list_data = dict['data']
# #		print(len(list_data))
# 		for i in range(len(list_data)):
# 			if len(list_data[i].split(','))==16:
# 				tmp_list=[]
# #				print(len(list_data[i].split(',')))
# 				for j in range(12):
# 					tmp_list.append(list_data[i].split(',')[j])
# 				writer.writerow(tmp_list)

# req = urllib.request.Request('http://www.baidu.com/')
# response = urllib.request.urlopen(req)
# the_page = response.read()
# soup = BeautifulSoup(the_page,'lxml')
#
# print(soup.prettify())

values = {'username': 'duchengli@hotmail.com', 'password': 'dl820113'}
data = urllib.parse.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib.request.Request(url,data)
response = urllib.request.urlopen(request)
print(response.read())
