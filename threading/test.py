from threading import Thread, Lock
import time

# 声明全局变量
money = 1000

def add(n, l):
    for i in range(10):
        print(n, '开始{} 存款...'.format(i))
        l.acquire()
        try:
            global money
            if money < 5000:
                sm = 1000
                money += sm
                print(n, '线程存了', sm, '剩余：', money)
            time.sleep(0.5)
        except:
            pass
        finally:
            l.release()


def sub(n, l):

    for i in range(10):
        print(n, '开始{}次取款...'.format(i))
        l.acquire()
        try:
            global money
            if money >= 500:
                print(n, '-取钱之前-', money)
                sm = 1000
                money -= sm
                print(n, '线程取了{} 之后 剩余:'.format(sm), money)
            time.sleep(0.5)
        except:
            pass
        finally:
            l.release()


if __name__ == '__main__':
    lock = Lock()  # 创建锁对象

    t1 = Thread(target=add, args=(1, lock))
    t2 = Thread(target=sub, args=(2, lock))
    t3 = Thread(target=sub, args=(3, lock))

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
