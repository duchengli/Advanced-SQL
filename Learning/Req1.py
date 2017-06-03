import requests
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return 'Error'

if __name__ == '__main__':
    url = 'https://item.jd.com/2967929.html'
    print(getHTMLText(url))

# import requests
#
# kv = {'key1': 'value1', 'key2': 'value2'}
# r = requests.request('GET', 'http://python123.io/ws', params=kv)
# print(r.url)

