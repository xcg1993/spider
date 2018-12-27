import os
import time
from multiprocessing import Process

names = []  # 全局变量

def addNames():
    global names  # 子进程与主进程是是并发执行的，不能共享全局变量(主进程变量)，只是复制一份
    names.clear()  # 只会影响子进程的变量，不会影响主进程的变量
    names.append('Disen at '+str(os.getpid()))

    time.sleep(2)
    print('子进程', os.getpid(), names)


if __name__ == '__main__':
    names.append('Jack')
    names.append('Lucy')

    p = Process(target=addNames)
    p.start()

    names.append('Cici')
    print('主进程', os.getpid(), names)