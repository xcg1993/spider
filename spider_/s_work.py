import json
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen, Request

url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'Connection':'keep-alive'
}
def search_kfc(city_name,pageSize):
    data={
        'cname':city_name,
        'pageSize':pageSize,
    }
    try:
        resp=urlopen(Request(url,urlencode(data).encode(),headers))
    except HTTPError as e:
        #e.url错误网址   e.code  错误代码   e.msg   详细说明
        print(e.url,e.code,e.msg)
    json_text=resp.read().decode()
    dict=json.loads(json_text)
    print(json_text)
    print(dict)
if __name__ == '__main__':
    search_kfc('咸阳',30)