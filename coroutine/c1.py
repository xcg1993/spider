import random
import time


def fib(n):
    a,b=0,1
    index=1
    print(n)
    while index<=n:
        #delay从外部传入的延迟时间
        delay=yield b  #返回第index的数
        time.sleep(delay)
        a,b=b,a+b
        index+=1

if __name__ == '__main__':
    # for n in fib(10):
    #     print(n)
    f=fib(10)
    n=next(f)
    print(n)
    print('我隔了两天')
    # time.sleep(1)
    while True:
        try:
            n=f.send(random.uniform(0.5,1.5))#先向fib发送数据，再从fib内获取数据
            print('获取数据',n)
        except:
            break
