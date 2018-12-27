"""
城市
https://www.zhipin.com/common/data/city.json

职位
https://www.zhipin.com/job_detail/?ka=header-job

搜索接口：
    https://www.zhipin.com/job_detail/?query=python&scity=101110100

下一页：
    https://www.zhipin.com/job_detail/?query=python&scity=101110100&page=2



"""
import json
import random
import time
from http import cookiejar
from queue import Queue
from threading import Thread
from urllib.request import Request, urlopen, build_opener, HTTPCookieProcessor,ProxyHandler
from http.cookiejar import CookieJar

from bs4 import BeautifulSoup

from bs4_.utils import decode_html
import ssl

from ua_ip_pool import get_ip, get_ua

ssl._create_default_https_context=ssl._create_unverified_context
url1 = 'https://www.zhipin.com/common/data/city.json'
# url2='https://www.zhipin.com/c101010100/?page={}'
headers={
    'User-Agent':get_ua()
}
opener=build_opener(ProxyHandler(proxies={'http':get_ip()}))
def download(url,callback):
    try:
        # print(11111)
        # url,callback=queue.get(timeout=30)
        # print(222)
        resp=opener.open(Request(url,headers=headers))
        # print(988898)
        if resp.code==200:
            print('*****ok,开始爬取******')
            callback(resp)
    except Exception as e:
        print(e)

def parse_city(resp):
    content_type=resp.headers.get('content-type')
    if content_type.startswith('application/json'):
        city_data=json.loads(resp.read())
        # print(1111)
        for city_list in city_data['data']['cityList']:
            # print(city_list)
            city_detail={}
            for city_name in city_list['subLevelModelList']:
                city_detail['code']=city_name['code']
                city_detail['name']=city_name['name']
                item_pipeline(**city_detail)


def parse_job(resp):
    html=decode_html(resp.read(),resp.headers.get('content-type'))
    soup=BeautifulSoup(html,'lxml')
    job_=soup.select('div[class=job-title]')   #list
    # job_name={}
    for job_name in job_:
        # job_name['name']=job_name.text
        # item_pipeline(**job_name)
        print(job_name.text)
# def start_spider(q):
#
#     q.put((url1,parse_city))   #必须为元祖
#     download_threads=Thread(target=download,args=(q,))
#     download_threads.start()

def item_pipeline(**data):
    print(data['code'],data['name'])
if __name__ == '__main__':

    # queue=Queue()
    # start_spider(queue)
    # download('https://www.zhipin.com/common/data/city.json',parse_city)
    # download(url1,parse_city)
    url2 = 'https://www.zhipin.com/c101010100/?page={}'
    for num in range(1,100):
        download(url2.format(num), parse_job)
        time.sleep(random.uniform(3,6))
    print('over')
