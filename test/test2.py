import csv
import time
import uuid
from http.client import HTTPResponse
from queue import Queue
from threading import Thread
from urllib.request import urlopen, Request
from lxml import etree
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}

def spider_all(q, all_url):  # 1.加载每一页网页连接，将所有网页连接加入到队列中
    q.put(all_url)
    for page in range(2, 3):
        url = 'https://www.qiushibaike.com/imgrank/page/%d/' % page
        time.sleep(5)
        q.put(url)

def upload(task_queue, img_queue):  # 2.下载全部页数据
    while True:
        try:
            url = task_queue.get(timeout=30)  # 从队列中拿出每一页所有数据
            resp = urlopen(Request(url, headers=headers))
            if resp.code == 200:
                print('下载成功')
                parse(resp, img_queue)
            else:
                print('失败')
        except:
            break

def parse(resp: HTTPResponse, img_queue):  # 3.解析数据
    try:
        content_type = resp.headers.get('Content-Type')
        charset = content_type.split(';')[-1]
        if charset:
            encoding = charset.split('=')[-1]
            html = resp.read().decode(encoding=encoding)
    except Exception as e:
        print(e)
        return
    et = etree.HTML(html)  # Element对象
    all_divs_ = et.xpath('//div[starts-with(@class, "article block")]')
    qb_info = {}
    for all_div_ in all_divs_:
        qb_info['photo_url'] = 'https:' + all_div_.xpath('.//div[starts-with(@class, "thumb")]//img/@src')[0]
        print(qb_info)
        item_pipeline(img_queue, **qb_info)

def item_pipeline(img_queue, **data):
    with open('qbtext.csv', 'a') as f:  # 从队列中拿出来写入文件
        writer = csv.DictWriter(f, fieldnames=data.keys())
        writer.writerow(data)
    img_queue.put(data['photo_url'])  # 将照片加入队列

def save_img(img_queue):  # 保存图片
    while True:
        try:
            url = img_queue.get(timeout=60)  # 从列中拿出照片连接
        except:
            break
        resp = urlopen(Request(url, headers=headers))
        content_type = resp.headers.get('Content-Type')
        name = str(uuid.uuid4())
        if content_type.startswith('image/jpeg'):
            name += '.jpg'
        elif content_type.startswith('image/png'):
            name += '.png'
        else:
            name += '.gif'

        with open('imges/%s' % name, 'wb') as f:
            f.write(resp.read())
        print('图片保存成功')

if __name__ == '__main__':
    task_queue = Queue()  # 所有网页连接
    img_queue = Queue()  # 保存照片队列
    spider_thread = Thread(target=spider_all, args=(task_queue, 'https://www.qiushibaike.com/imgrank/page/1/'))
    spider_thread.start()
    link_thread = Thread(target=upload, args=(task_queue, img_queue))
    link_thread.start()
    img_thread = Thread(target=save_img, args=(img_queue,))
    img_thread.start()
    spider_thread.join()
    link_thread.join()
    img_thread.join()
    print('全部完成')
