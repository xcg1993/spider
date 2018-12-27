import requests
url='http://127.0.0.1:5000/update/1'
#json参数，请求会发送json数据到服务器
resp=requests.request('PUT',url,json={'name':'xcg','age':24})
if resp.status_code==200:
    print(resp.headers.get('content-type'))
    print(resp.text)