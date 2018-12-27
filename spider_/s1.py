import socket
if __name__ == '__main__':
    #网络接口  套接字
    client=socket.socket()
    try:
        # 链接服务器
        #http协议：80
        #https协议：443
        client.connect(('www.meinv.hk',80))
        print('连接')
        #发送请求   请求头中Connection：keep-alive长链接   close 短连接
        #第一是头部分，第二是body部分—post请求
        #两个部分之间存在一个空行（代表头header结束）
        client.send('GET / HTTP/1.1\r\nHost:www.meinv.hk\r\n\r\n'.encode())
        response=client.recv(102400)  #接受数据（字节数）
        print(response.decode())

    except Exception as e:
       print('连接失败')