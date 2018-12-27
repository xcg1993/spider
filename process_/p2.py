'''
1000个4位随机验证码（字母，数字组成）
每间隔2秒读取一次验证码（统计验证码的数量）
'''
import re
import time
from multiprocessing import Process,current_process
import os
import string
import random
def random_verify_code(total_cnt=1000,length=4,file_path=None):
    if file_path is not None:
        random_range = string.ascii_uppercase + string.digits
        l = list(random_range)
        for _ in range(total_cnt):

            random.shuffle(l)#打乱顺序
            verify_code=set()
            index=0
            while len(verify_code)<length:
                verify_code.add(l[index])
                index+=1
            verify_code=''.join(verify_code)
            with open(file_path,'a') as f:
                f.write(verify_code+'\n')
            time.sleep(0.5)
  #current_process()获取当前的进程对象
    print(current_process().name,current_process().pid)


def count_verify_code(delta=2,file_path=None):
    time.sleep(1)
    if file_path is not None:
    #统计指定文件的代码的行数  wc
        last_line=0
        while True:
            r=os.popen('find /V "" /C %s'%file_path)
            lines=r.read()
            lines=int(re.findall(r'\d+',lines)[0])
            if lines==last_line:
                break

            print(lines,end='')   #读取命令结果
            last_line=lines
            time.sleep(delta)

if __name__ == '__main__':
    p1_param={
        'total_cnt': 1000,
        'file_path':'verify_code.txt'

    }
    p2_param = {

        'file_path': 'verify_code.txt'

    }
    p1=Process(target=random_verify_code,kwargs=p1_param)
    p2=Process(target=count_verify_code,kwargs=p2_param)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('over')