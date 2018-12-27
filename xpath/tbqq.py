import csv
from http.client import HTTPResponse
from queue import Queue
from threading import Thread
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from lxml import etree

url='http://www.tbqq.net/forum.php?mod=forumdisplay&fid=2&sortid=2&sortid=2&'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'Connection':'keep-alive'
}
def upload(url,num):
    data={
        'page':num
    }
    resp=urlopen(Request(url,urlencode(data).encode(),headers))
    if resp.code==200:
        print('下载成功')
        parse(resp)
    else:
        print('失败')

def parse(resp:HTTPResponse):
    try:
        content_type=resp.headers.get('Content-Type')
        charset=content_type.split(';')[-1]
        if charset:
            encoding=charset.split('=')[-1]
        html=resp.read().decode(encoding=encoding)
    except Exception as e:
        print(e)

    et=etree.HTML(html)   #Element对象
    all_lies=et.xpath('//li[starts-with(@class, "deanactions")]')
    for all_li in all_lies:
        photo='http://www.tbqq.net/'+all_li.xpath('.//img/@src')[0]
        name=all_li.xpath('.//div[@class="deanmadouname"]/a/text()')[0]
        detail='http://www.tbqq.net/'+all_li.xpath('./a/@href')[0]
        job=all_li.xpath('.//div[@class="deanmadouzhiye"]/span/text()')[0]
        height,weight=all_li.xpath('.//div[@class="deanmdl"]/span/text()')
        renqi=all_li.xpath('.//div[@class="deanmdr"]')[0]
        address=all_li.xpath('.//div[@class="deanmadouinfos"]/div[last()]/text()')[0]
        print(photo,name,job,detail)
        info={
            'photo':photo,
            'name':name,
            'detail':detail,
            'job':job,
            'height':height,
            'weight':weight,
            'renqi':renqi,
            'address':address
        }
        item_pipeline(**info)

def item_pipeline(**data):
    with open('mjx.csv','a')as f:
        writer=csv.DictWriter(f,fieldnames=data.keys())
        writer.writerow(data)
        print('写入成功')



if __name__ == '__main__':
    upload(url, 1)
    # task_queue=Queue()
    # spider_thread=Thread(target=upload,args=(task_queue,))
    # spider_thread.start()
    # spider_thread.join()