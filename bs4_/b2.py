"""
https://www.gushiwen.org/gushi/sanbai.aspx
基于beatifulsoup爬取古诗文
"""
import re
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup, Tag
from requests import HTTPError
from bs4_.utils import decode_html
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
user_agent= 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
url='https://www.gushiwen.org/gushi/sanbai.aspx'
headers={
    'User-Agent':user_agent
}
def download(url):
    try:
        resp=urlopen(Request(url,headers=headers))
        if resp.code==200:
            print(f'request {url} ok')  #format格式字符串
            parse(resp)
        else:
            print(f'request {url} fail;{resp.code}')    #20x
    except HTTPError as e:
        print(e)
def parse(resp):
    content_type = resp.headers.get('content-type')
    if content_type.startswith('text/html'):
        html=decode_html(resp.read(),content_type)
        bs=BeautifulSoup(html,'lxml')
        #查询所有a标签
        as_=bs.find_all('a')
        for a_ in as_:
            # print(a_.text,a_.attrs.get('href'))
            href=a_.get('href')  #同a_.attrs.get(href)
            if re.match(r'https://so.gushiwen.org/shiwenv_\w+?.aspx',href):
                print(a_.getText(),href)
    elif content_type.startswith('image/'):
        pass
    else:#非网页或图片，最大可能是json数据
        pass
def item_pipeline(**data):
    print(data)
def start_spider():
    pass
if __name__ == '__main__':
    download(url)