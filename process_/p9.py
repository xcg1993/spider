from multiprocessing import Array, Process, Value
import os
import time


def f(n, a):
    print('子进程', os.getpid())
    n.value = 20.5  # Value的赋值
    for i in range(len(a)):
        a[i] += 10
        print('子进程', os.getpid(), a[i])
        time.sleep(1)


if __name__ == '__main__':
    num = Value('f', 0.1)
    arr = Array('i', range(10))
    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()
    print('主进程', os.getpid())
    print(num.value)  # 读取值
    print(arr[::-1])