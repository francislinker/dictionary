from socket import *
from threading import Thread
import sys

#处理客户端的线程函数
def handler(client):
    while 1:
        msg = client.recv(1024)
        if not msg:
            break
        print(msg.decode())
        client.send('服务器收到'.encode())

address = ('0.0.0.0',8888)
server = socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
server.bind(address)
server.listen(10)

print('正在等待客户端连接...')
while True:
    try:
        client,addr = server.accept()
    except KeyboardInterrupt:
        sys.exit('服务器已断开！')
    except Exception as e:
        print(e)
        continue

    #客户端已经连接，创建线程
    t = Thread(target=handler(),args=(client,),)
    t.start()
    t.setDaemon(True)