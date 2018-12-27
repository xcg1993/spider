import csv
from queue import Queue
from threading import Thread
from urllib.request import Request, urlopen

from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
def spider_single(page):

    try:
        if page==1:
            url = 'http://sc.chinaz.com/tupian/shuaigetupian.html'
        else:
            url='http://sc.chinaz.com/tupian/shuaigetupian_%d.html'% page
        resp=urlopen(Request(url,headers=headers))
        if resp.code==200:
            parse(resp)
    except:
        print('页码有误')
        return
    # else:
    #     print('页码有误')
    #     return
def parse(resp):
    try:
        # content_type=resp.headers.get('Content-Type')
        # mime_type,charset=tuple(content_type.split(';'))
        # if charset:
        #     html=resp.read().decode(encoding=charset)
        # else:
        #     html=resp.read().decode(encoding='gbk')
        html = resp.read().decode(encoding='UTF-8')

    except Exception as e:
        print('失败',e)
        return

    et=etree.HTML(html)     #Element对象
    all_divs=et.xpath('//div[starts-with(@class,"box")]')
    shuaige = {}

    for all_div in all_divs:
        img=all_div.xpath('.//a/img')
        if img:
            shuaige['photo_name'] = img[0].xpath('./@alt')[0]
            shuaige['src_url']=img[0].xpath('./@src2')[0]
            print(shuaige['photo_name'],shuaige['src_url'])

            save_img(**shuaige)


def save_img(**data):
    url=data['src_url']
    name=data['photo_name']
    resp=urlopen(Request(url,headers=headers))
    content_type=resp.headers.get('Content-Type')

    if content_type.startswith('image/jpeg'):
        name += '.jpg'
    elif content_type.startswith('image/png'):
        name += '.png'
    else:
        name += '.gif'

    with open('shuaige/%s'%name,'wb') as f:
        f.write(resp.read())

if __name__ == '__main__':
    # stack_queue=Queue()

    img_queue=Queue()
    spider_all_thread=Thread(target=spider_single,args=(2,))
    spider_all_thread.start()
    spider_all_thread.join()