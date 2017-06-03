import urllib.request
import random
import csv

ck={'Cookie':'erf_eligible=82; p1_hcopy3=control_places; ftv=1487553708569; __ssid=2b34dca2-a8d2-4cf6-8b16-5385bbf75ac3; _user_attributes=%7B%22curr%22%3A%22CNY%22%2C%22guest_exchange%22%3A6.8644%2C%22device_profiling_session_id%22%3A%221487560184--d6fb05601419430ed457b2f4%22%2C%22giftcard_profiling_session_id%22%3A%221487560184--9fa0f0758b2631eefc37d379%22%2C%22reservation_profiling_session_id%22%3A%221487560184--5ca5a9d99f1fa790bea59141%22%7D; p3_sticky_friendly_booking=control; i18n_google_nmt=treatment; _ga=GA1.2.1595560062.1487553707; _csrf_token=V4%24.airbnbchina.cn%24XuBpQ-dTqN0%24F-TG72JnAuqqogzfEE74mCHW0UkHhbocvH9rpKrZdQw%3D; flags=268439552; _airbed_session_id=3b9012edaa572b93ad6d6784c2127bd7; EPISODES=s=1487560426174&r=https%3A%2F%2Fwww.airbnbchina.cn%2Frooms%2F15248199%3Fcheckin%3D2017-03-22%26checkout%3D2017-03-23%26guests%3D1%26adults%3D1%26children%3D0%26infants%3D0%26s%3D3eLfCN0H; bev=1487553692_HbBNl%2FsqkGKpL7WF'}


# 获取链接列表
def get_url_list(start,end):
	url_list=[]
	while(start<=end):
		url = 'https://www.airbnbchina.cn/s/%E6%88%90%E9%83%BD--%E5%9B%9B%E5%B7%9D%E7%9C%81--%E4%B8%AD%E5%9B%BD?guests=1&adults=1&children=0&infants=0&checkin=2017-03-22&checkout=2017-03-23&ss_id=fv5xtw1n&source=bb&cdn_cn=1&page='+str(start)
		url += '&allow_override%5B%5D=&ne_lat=30.700951735091245&ne_lng=104.20669555664062&sw_lat=30.52376985943266&sw_lng=103.95675659179688&zoom=12&search_by_map=true&s_tag=3eLfCN0H'
		url_list.append(url)
		start+=1
	return url_list


def save_json_data():
#	url_list =get_url_list(1,17)
	url_list =get_url_list(1,1)
	count=0
	for url in url_list:
		req=urllib.request.Request(url,headers=ck)
		retry_time=20
		for i in range(retry_time):
			try:
				data=urllib.request.urlopen(req,timeout=100).read()
				break
			except:
				if i<retry_time-1:
					continue
				else:
					print('多次尝试仍然失败!')
#		data=source_code.read()
#		print(source_code)
		print(data)
		#json_data = data[16:]
		

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

save_json_data()  				
				
'''
csvfile=open('d:\\eastmoney.csv','w',newline='')
writer=csv.writer(csvfile)
writer.writerow([u'代码',u'股票简称',u'股东人数',u'较上期变化',u'人均流通股',u'前十大流通股东持股数量',u'前十大流通股东占流通股比例',u'前十大股东持股数量','前十大股东占总股本比例','机构持股数量','机构持股占流通A股本比例','筹码集中度'])				


'''