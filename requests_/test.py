import requests

url='http://www.jokeji.cn/user/c.asp?'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
data={
    'u':'disenQF',
    'p':'disen8888',
    't':'big'

}
s=requests.session()
r=s.get(url=url,data=data,headers=headers)
r.encoding='gbk'
print(r.text)