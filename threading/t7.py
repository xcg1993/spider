import time
from threading import Thread, Lock, Condition, current_thread
from queue import Queue
class ConcurrentQueue():#自定义同步线程队列
    def __init__(self,max_size=10):
        self.max_size=max_size  #满仓量
        #常用函数：acquire(),release(),wait(),notify()
        self.condition=Condition(Lock())#条件变量
        self.q=Queue()#仓库

    def get(self):
        with self.condition:
            while self.q.empty():
                print('销售',current_thread().name)
                self.condition.wait(timeout=10)
            #仓库不为空时
            obj=self.q.get()#获取消息数据
            self.condition.notify()#通知生产线程
        return obj
    def put(self,obj):
        with self.condition:
            #仓库满时，无法生产
            while self.q.qsize()>=self.max_size:
                print('生产',current_thread().name,'仓库已满')
                self.condition.wait()#等待
            #仓库不满时
            self.q.put(obj)
            self.condition.notify()#通知等待的消费者线程
def producer(q,start,end):
    for _ in range(start,end):
        obj='黄金-%d'% _
        print('生产者',current_thread().name,obj)
        q.put(obj)
        time.sleep(0.1)
def consumer(q):
    for _ in range(15):
        obj=q.get()
        print('消费者：',current_thread().name,obj)
        time.sleep(0.2)

def start_thread(threads):
    for t in threads:
        t.start()

def wait_all(threads):
    for t in threads:
        t.join()

if __name__ == '__main__':
    q=ConcurrentQueue(2)

    seq=((10,20)),(30,40),(50,60)
    ps=[Thread(target=producer,args=(q,*seq[_])) for _ in range(3)]

    cs = [Thread(target=consumer, args=(q,)) for _ in range(3)]
    start_thread(ps+cs)
    wait_all(ps+cs)
    print('over')
