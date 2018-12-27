from multiprocessing import Process
a=100
def func():
    global a
    a += 100    #修改全局变量
    print('子进程 a=',a,id(a))
if __name__=='__main__':

    p1=Process(target=func)
    #p1.is_alive()#是否存活   False
    p1.start()
    p1.is_alive()#True
    #p1.terminate()#中断执行
    p1.join()
    print(p1.pid)
    print('父进程',a,id(a))
