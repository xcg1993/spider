import os
import time
import uuid
from multiprocessing import Process, Pipe
import urllib
from requests import request

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR=os.path.join(BASE_DIR,'images')


def downloader(conn):
    while True:
        url=conn.recv()
        if url=='0':
            break
        print('下载中',url)
        resp=request('get',url)
        if resp.status_code==200:
            content_type=resp.headers.get('Content-Type')
            extName='.jpg' if content_type.startswith('image/jpeg') else '.png' if content_type.startswith('image/png') else '.gif'
            filename=uuid.uuid4().hex+extName
            with open(os.path.join(IMG_DIR,filename),'wb') as f:
                f.write(resp.content)





if __name__ == '__main__':
    #1.创建管道Pipe
    conn1,conn2=Pipe(duplex=False)#False表示半双工
    p=Process(target=downloader,args=(conn1,))
    p.start()
    #两个事件：
    #1）进入上下文：调用对象的__enter__函数
    #2）退出上下文：调用对象的__exit__ 方法
    with open('urls.txt') as f:
        for line in f: #每次调用f的__next__方法
            conn2.send(line)
            time.sleep(1)

    conn2.send('0')
    p.join()#等待子进程完成任务
    print('--over--')