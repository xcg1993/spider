from threading import Thread
from urllib.parse import urlencode
from urllib.request import HTTPHandler, build_opener, Request

url='http://tieba.baidu.com/f?'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',

}
params={
    'kw':'python3',
    'ie':'utf8',
    'pn':150 #0 50 100 150
}
#1  声明HTTP处理器
handler=HTTPHandler()
#2.构造opener打开器（浏览器）
opener=build_opener(handler)
def search_tieba(keyword,page_num=0,filename=None):
    params['kw']=keyword
    params['pn'] = page_num
    #3.实例化请求对象
    req=Request(url,data=urlencode(params).encode(),headers=headers)
    #4.发送请求
    resp=opener.open(req)
    with open(filename,'wb') as f:
        f.write(resp.read())
        print('over')
if __name__ == '__main__':
    keys=[('英雄联盟','t1.html'),('绝地求生','t2.html'),('王者荣耀','t3.html')]
    sts=[Thread(target=search_tieba,kwargs={'keyword':k,'filename':filename}) for k,filename in keys]
    for i in sts:
        i.start()
    for i in sts:
        i.join()
    print('over')