import re
import time
import uuid
from multiprocessing import Process,Queue
import os
from process_.p4 import IMG_DIR
from requests import request
def spider_img(url,queue:Queue):#爬虫网页下载图片
    print('开始爬取：',url)
    resp=request('get',url)
    html=resp.text
    images_a=re.findall(r'<a href="(http://www.meinv.hk/\?p=(\d+?))" >',html)
    images_url=set(images_a)
    while True:
        print('开始爬取：', url)
        resp = request('get', url)
        html = resp.text

        name = re.findall(r'<h1 class="title">(.*?)</h1>', html)[0]
        #获取所有照片的地址
        images_div=re.findall(r'<div class="post-image">(.*?)</div>',html)[0]
        images=re.findall(r'src="(.*?)"',images_div)
        for img_url in images:
            resp=request('get',img_url)
            queue.put((name,img_url,resp.content))
            print('下载%s完成'%img_url)
            time.sleep(1)
        for i in images_a:
            url=i[0]
            images_a.pop(0)
            break
        if images_a==[]:
            break




def pipeline(queue:Queue):      #保存图片
    while True:
        try:
            name,url,bytes=queue.get(timeout=30)
#30秒拿不到数据，则会抛出异常
            dir_=os.path.join(IMG_DIR,name)
            if not os.path.exists(dir_):
                os.mkdir(dir_)

            with open(os.path.join(dir_,uuid.uuid4().hex+'.jpg'),'wb') as f:
                f.write(bytes)
            print('保存照片',url)
        except:
            break
if __name__ == '__main__':
    q=Queue(maxsize=10)  #varchar(20) 20表示字符长度，不是字节
    start_url='http://www.meinv.hk/?p=2707'
    spider=Process(target=spider_img,
                   args=(start_url,q))
    pipeline_=Process(target=pipeline,args=(q,))
    spider.start()
    pipeline_.start()
    spider.join()
    pipeline_.join()
    print('over')   #爬虫报告