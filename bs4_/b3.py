"""
https://www.gushiwen.org/gushi/sanbai.aspx
基于beatifulsoup爬取古诗文
"""
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
url='https://www.gushiwen.org/gushi/sanbai.aspx'
headers={
    'User-Agent':user_agent
}
opener=build_opener(ProxyHandler(proxies={'http':'119.39.238.127:9999'}))
def download(queue):
    while True:
        try:
            #从队列中拿出url和callback回调函数
            url,callback=queue.get(timeout=30)
            resp=urlopen(Request(url,headers=headers))
            if resp.code==200:
                print(f'request {url} ok')  #format格式字符串
                callback(resp,queue)     #回调函数
            else:
                print(f'request {url} fail;{resp.code}')    #20x
            time.sleep(random.uniform(1,5))
        except HTTPError as e:
            print(e)
        except Exception as e:
            break
    print(current_thread().name,'over')
def parse(resp,q):
    content_type = resp.headers.get('content-type')
    if content_type.startswith('text/html'):
        html=decode_html(resp.read(),content_type)
        bs=BeautifulSoup(html,'lxml')   #Tag对象
        #查询所有a标签
        as_=bs.find_all('a')
        for a_ in as_:   #a_是Tag标签
            # print(a_.text,a_.attrs.get('href'))
            href=a_.get('href')  #同a_.attrs.get(href)
            if re.match(r'https://so.gushiwen.org/shiwenv_\w+?.aspx',href):
                print(a_.getText(),href)
                q.put((href,parse_book))
    elif content_type.startswith('image/'):
        pass
    else:#非网页或图片，最大可能是json数据
        pass


def parse_book(resp,q):
    print(resp.url,'开始解析')         #第二层网页的解析
    html=decode_html(resp.read(),resp.headers.get('content-type'))
    bs=BeautifulSoup(html,'lxml')
    h1:Tag=bs.find('h1')
    if h1:
        title=h1.text
    p:Tag=bs.find('p',class_='source')
    if p:
        source=p.text
    div:Tag=bs.find('div',class_='contson')
    if div:
        content=div.text
    item_pipeline(**{
        'title':title,
        'source':source,
        'content':content
    })

def item_pipeline(**data):
    print(data)
def start_spider(q):
    q.put((url,parse))    #第一个任务    入口
    download_threads=[Thread(target=download,args=(q,)) for _ in range(2)]
    for t in download_threads:
        t.start()
    for t in download_threads:
        t.join()
    print('完成')
if __name__ == '__main__':
    queue=Queue()
    start_spider(queue)