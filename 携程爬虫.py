import requests
import json

class Ctrip:
    def __init__(self):
        pass
    def get_json(self):
        url = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=CTU&ACity1=BJS,PEK&SearchType=S&DDate1=2018-04-27&IsNearAirportRecommond=0&LogToken=f83e379fa7fa4332af34ed89c4480d8c&rk=5.7435591444686365230934&CK=CF8C3B8B266060678869DAF67A5C464A&r=0.1773557575497505756410'
        headers = {'Host': "flights.ctrip.com",
                   'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
                   'Referer': "http://flights.ctrip.com/booking/ctu-bjs,pek-day-1.html?ddate1=2018-04-27"}
        req = requests.get(url=url,timeout=5,headers=headers)
        content = req.text
        dict_content = json.loads(content, encoding='UTF-8')
        for k,v in dict_content.items():
            print(str(k)+":"+str(v))

ctrip = Ctrip()
ctrip.get_json()


