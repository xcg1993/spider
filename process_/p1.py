import time
from multiprocessing import Process
import os
def find_py(path):
    #当前id？
    #父进程id ——>ppid
    print("当前进程id",os.getpid(),
          '当前父进程id',os.getppid())
    print('开始查找',path)   #真正开发或者生产环境下，必须使用logging日志，不能用print
    time.sleep(5)
    #判断path的目录是否存在
    if not os.path.exists(path):
        raise FileNotFoundError('文件未找到',path)

    files =list(filter(lambda filename: filename.endswith('.py'),os.listdir(path)))
    print(files)


if __name__=="__main__":     #程序入口，类似于c/java 的main 函数
    #find_py()                   保持格式，暂时空内容
    print("当前进程id",os.getpid(),
          '当前父进程id',os.getppid())
    #1.创建进程
    p1=Process(target=find_py,kwargs={'path':'D:\pycharm\python-1805\Django\TPP'})
    #2.启动
    p1.start()
    #3.当前进程（父进程）要等待子进程结束
    p1.join(timeout=5)
    print('所有任务执行完成')
