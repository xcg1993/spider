'''
每次分配的cpu时间
通过lock锁解决一致性问题
'''



import time
from threading import Thread, current_thread, Lock


def add(money):
    global  my_money
    with lock:
        print('余额',my_money)
        my_money+=money
        # 10/0
        time.sleep(2)
        print('存入后余额', my_money)



def sub(money):
    global  my_money
    #进入上下文：调用lock.acquire() 加锁
    #退出上下文，调用lock.release()释放锁
    with lock:
        print('余额',my_money)
        #如果其他线程修改my_money,则要等到lock释放锁
        my_money-=money
        time.sleep(3)
        print('取钱后余额', my_money)




if __name__ == '__main__':
    #MainThread  主线程
    print(current_thread().name,'运行ok')
    my_money = 80000000
    lock=Lock()
    add_t=Thread(target=add,args=(1000,))
    sub_t = Thread(target=sub, args=(1000,))
    add_t.start()
    sub_t.start()
    add_t.join()
    sub_t.join()
    print('over')