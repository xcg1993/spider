"""
使用urllib.request实现简单的请求
请求网页
保存照片：
请求照片并保存
"""
import hashlib
from http.client import HTTPResponse
from urllib import request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
def baidu(path):
    #hettp://是HTTP协议的schema
    #https://是HTTP+SSL协议的schema
    #redis://是redis连接的schema
    #ftp：//是FTP协议的schema
    #www.baidu.com  是HOST
    url='http://www.baidu.com'+path
    resp:HTTPResponse=request.urlopen(url)     #返回一个response对象
    #判断请求是否成功
    if resp.code==200:
        print(resp.url,'成功')
        print(resp.status)
        print(resp.headers)
        #read(),readline(),readlines()
        #print(resp.read())
        mine_type=resp.info().get('Content-Type')
        if mine_type.endswith('html'):
            ext_name='.html'
        elif mine_type.endswith('jpeg'):
            ext_name='.jpg'
        with open('baidu-'+path[1:]+ext_name,'wb') as f:
            f.write(resp.read())
    else:
        print('失败',resp.code)

def csdn(path):
    url='https://www.csdn.net'+path
    filename=path[1:]
    if filename=='':
        filename='index.html'
    else:
        filename=filename+'.html'
    request.urlretrieve(url,'csdn-'+filename)
    print('下载csdn',path,'网页成功')


def save_img(url,filename):
    try:
        request.urlretrieve(url,filename)
        print('成功')
    except:
        print('失败')


def md5(url):
    m=hashlib.md5()
    m.update(url.encode())
    return m.hexdigest()


if __name__ == '__main__':
    baidu('/')
    # csdn('/')
    url='https://p1.ssl.qhimgs1.com/bdr/1843__/t01087c2c730bf3f191.jpg'
    filename=md5(url)+'.'+url.split('.')[-1]
    #save_img(url,filename)