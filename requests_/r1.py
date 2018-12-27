import requests
url='https://www.zhipin.com/common/data/city.json'
resp=requests.get(url)
if resp.status_code==200:
    content_type=resp.headers.get('Content-Type')
    if content_type.startswith('application/json'):
        city_json=resp.json()  #自动使用resp.encoding进行解码
        city_list=city_json.get('data').get('cityList')
        for city in city_list:
            print(city.get('code'),city.get('name'))