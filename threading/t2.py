'''
每次分配的cpu时间
'''



import time
from threading import Thread,current_thread


def add(money):
    global  my_money
    print('余额',my_money)
    my_money+=money
    # time.sleep(1)
    print('存入后余额', my_money)


def sub(money):
    global  my_money
    print('余额',my_money)
    my_money-=money
    # time.sleep(3)
    print('取钱后余额', my_money)




if __name__ == '__main__':
    #MainThread  主线程
    print(current_thread().name,'运行ok')
    my_money = 80000000
    add_t=Thread(target=add,args=(1000,))
    sub_t = Thread(target=sub, args=(1000,))
    add_t.start()
    sub_t.start()
    add_t.join()
    sub_t.join()
    print('over')