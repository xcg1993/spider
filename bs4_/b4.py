import random
import re
import time
from queue import Queue
from threading import Thread, current_thread
from urllib.request import Request,urlopen,ProxyHandler,build_opener
from bs4 import BeautifulSoup, Tag
from requests import HTTPError
from bs4_.utils import decode_html
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

user_agent= 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'

headers={
    'User-Agent':user_agent
}
# opener=build_opener(ProxyHandler(proxies={'https':'119.101.113.11:9999'}))


def download(url,callback):
    try:
        resp=urlopen(Request(url,headers=headers))
        if resp.code==200:
            print('ok')
            callback(resp)
    except HTTPError as e:
        print(e)

def parse(resp):
    html=decode_html(resp.read(),resp.headers.get('content-type'))
    soup=BeautifulSoup(html,'lxml')
    conts=soup.select('div[class=cont]')#list
    print(type(conts))
    for cont in conts:
        as_=cont.select('a')
        if len(as_)==2:
            content_tag,author_title_tag=tuple(as_)
            item_pipeline(content=content_tag.text,author_title=author_title_tag.text)
            #请求下页数据
    more=soup.select('.amore')    #list
    if more:
        next_page_url='https://so.gushiwen.org'+more[0].get('href')
        time.sleep(random.uniform(2,6))
        download(next_page_url,parse)
    else:
        print('没有下一页')
def item_pipeline(**data):
    print(data['content'],data['author_title'])

if __name__ == '__main__':
    # url = 'https://so.gushiwen.org/mingju/'
    download('https://so.gushiwen.org/mingju/',parse)
