import random
import string
from threading import Thread,current_thread,Lock


'''
线程类的写法：继承Thread，重写run（）函数
'''
#扩展：多继承的情况下，调用super（）会根据MRO编排的顺序依次调用指定的方法
class StackThread(Thread):
    def __init__(self):
        super().__init__()#调用父类的线程的初始化函数

    def run(self):
        opt=random.randint(0,1)
        print(self.name,stack,'压入' if opt else '弹出')
        #判断是否取消操作
        if len(stack)==0 and opt==0:
            print(self.name,'本次操作取消')
            return
        with lock:
            if opt:
                stack.insert(0,random.choice(string.ascii_uppercase))
            else:
                print(self.name,stack.pop())

            print(self.name,stack)




if __name__ == '__main__':
    mt=current_thread()#当前主线程对象
    stack=[]#随机间隔时间，向stack压入或者弹出
    print(mt)
    lock=Lock()
    threads=[StackThread() for _ in range(100)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(mt.name,'over')