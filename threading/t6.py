from threading import Thread, current_thread, Lock


def add():
    with lock:#加锁
        list.append(2)
        print(list)

        # lock.release()#释放锁

def sub():
    if lock.acquire():
        list.pop(2)
        print(list)
        lock.release()
if __name__ == '__main__':
    lock=Lock()
    list=[3,5,9]
    t1=Thread(target=add)
    t2=Thread(target=sub)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('_____')

