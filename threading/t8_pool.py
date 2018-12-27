import time
from threading import Thread, current_thread
from queue import Queue
class WorkManager():
    def __init__(self,max_threads=2):
        self.max_threads=max_threads
        self.task_queue=Queue()     #队列对象
        self.thread_pool=[]        #线程数组

    def apply_async(self,task,*args):
        """
        发布任务
        :param task:任务函数
        :param args:函数的参数
        :return:
        """
        self.task_queue.put((task,args))

    def close(self):
        """
        停止发布任务，开始运行线程池中的线程
        :return:
        """
        if self.task_queue.qsize()<self.max_threads:
            self.max_threads=self.task_queue.qsize
        for _ in range(self.max_threads):
            self.thread_pool.append(Work(self.task_queue))

    def wait_all_complete(self):
        """
        等待所有线程池中的线程完成任务
        :return:
        """
        for thread in self.thread_pool:
            if thread.isAlive():thread.join()


class Work(Thread):
    def __init__(self,q):
        super().__init__()
        self.q=q        #q即为Queue任务队列
        self.start() #启动

    def run(self):
        while True:
            try:
                task,args=self.q.get(block=False)
                #执行任务
                task(*args)
                self.q.task_done()#任务完成信号
            except:
                break

def do_task(*args):
    print(current_thread().name,'开始执行任务')
    time.sleep(1)
    print(current_thread().name,'任务完成')
if __name__ == '__main__':
    #创建线程池对象
    pool_manager=WorkManager(max_threads=10)
    #发布任务
    for token in range(1000):
        pool_manager.apply_async(do_task,'http://meinv.hk/?p=',token)

    pool_manager.close()#启动线程池中的线程
    pool_manager.wait_all_complete()