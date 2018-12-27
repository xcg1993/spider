from threading import  Thread,local,current_thread
def t1():
    var.v=789   #本地变量
    print(var.v)

if __name__ == '__main__':
    var=local()
    var.v=123
    t=Thread(target=t1)
    t.start()
    t.join()
    print(current_thread().name,var.v)