"""
爬取西刺网站
"""
from http.cookiejar import CookieJar
from urllib.request import urlopen, HTTPCookieProcessor, build_opener, Request
import re
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url='https://www.xicidaili.com/nn/'
opener=build_opener(HTTPCookieProcessor(CookieJar()))

def get():
    resp=opener.open(Request('https://www.xicidaili.com/nn/'))
    html=resp.read().decode()
    print(html)
    # if resp.code==200:
    #     html=resp.readlines()
    #     print(html)
    with open('xc.html','wb') as f:
        f.write(html)


def parse():
    with open('xc.html') as f:    #默认：rt
        html=f.read()         #文本数据
    re.findall(r'(\d+?\.\d+?\.\d+?\.\d+?)\s+?.*?(\d{2,5})',html,re.M)



if __name__ == '__main__':
    get()