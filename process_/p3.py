import time
from multiprocessing import Process, Pipe


def downloader(conn):
    while True:
        url=conn.recv()
        if url=='0':
            break
        print('下载中',url)
if __name__ == '__main__':
    #1.创建管道Pipe
    conn1,conn2=Pipe(duplex=False)#False表示半双工
    p=Process(target=downloader,args=(conn1,))
    p.start()

    for url in ('http://www.baidu.com',
                'http://www.hao123.com',
                'http://www.bilibili.com'):
        conn2.send(url)#发送下载任务
        time.sleep(1)
    conn2.send('0')
    p.join()#等待子进程完成任务
    print('--over--')