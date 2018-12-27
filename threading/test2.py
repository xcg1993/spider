# coding=utf8
import threading
import time
from random import randint

data = threading.local()  # 使用线程本地变量


def addNum(i):
    data.v = i  # 每个线程中的本地变量data.v 都是唯一的
    for i in range(5):
        data.v += randint(10, 200)
        print(threading.current_thread().name, data.v)
        time.sleep(1)
    print(threading.current_thread().name,'最终的数：',  data.v)


if __name__ == '__main__':
    print("start Threads")
    try:
        for i in range(6):
            t = threading.Thread(target=addNum, args=(i,))
            t.start()

    except Exception as e:
        print("stop Threads")