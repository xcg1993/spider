import os
from threading import Thread,current_thread

def list_img(path):
    print(current_thread().name,'搜索中')
    if os.path.exists(path):
        for filename in os.listdir(path):
            full_file_path=os.path.join(path,filename)
            if os.path.isdir(full_file_path):
                list_img(full_file_path)
            else:
                print(full_file_path)

if __name__ == '__main__':
    t=Thread(target=list_img,args=('../process_',))
    t.start()
    t.join()
    print('over')