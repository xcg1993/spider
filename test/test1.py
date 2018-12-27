"""
1.  请求百度翻译接口数据，并将翻译结果中的解释信息保存到csv文件中。
要求： 基于socket实现HTTP的网络请求
"""


post_url = 'https://fanyi.baidu.com/sug'
import socket
if __name__ == '__main__':
    #网络接口  套接字
    client=socket.socket()
    try:
        client.connect(('fanyi.baidu.com',443))
        print('连接成功')
        #发送请求   请求头中Connection：keep-alive长链接   close 短连接
        #第一是头部分，第二是body部分—post请求
        #两个部分之间存在一个空行（代表头header结束）
        client.send('POST /sug HTTP/1.1\r\nHost:fanyi.baidu.com\r\n\r\nConnection:keep-alive\r\n\r\n'.encode())
        buffers = []
        while True:
            try:
                respone1 = client.recv(1024)  # 接收数据(字节数)
                buffers.append(respone1.decode())
                text: str = respone1.decode()
                if text.find('</html>') > 0:
                    break
                respone1 = None
            except:
                print('error')

        html = ''.join(buffers)
        print(html)


    except Exception as e:
       print('连接失败')