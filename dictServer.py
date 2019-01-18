'''
项目：电子词典
模块：socket pymysql
'''
# import socket
# import pymysql
# import os
# import sys

# def main():
#     address = ('0.0.0.0',8888)
#     #创建数据库连接对象
#     db = pymysql.connect('localhost','root','123456','dict',charset='utf8')
#     #创建TCP套接字
#     server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#     server.bind(address)
#     server.listen(10)
#     print('等待客户端连接...')
#     while True:
#         try:
#             client,addr = server.accept()
#             print('客户端',addr,'已连接..')
#         except KeyboardInterrupt:
#             sys.exit('服务器已经关闭，客户端无法连接...')
#         except Exception as e:
#             print(e)
#             continue

#         pid = os.fork()#每来一个客户端创建一个子进程

#         if pid == 0:
#             doRequest(client)
#             sys.exit('客户端退出')#事情做完就退出子进程
        
#         else:
#             continue
    
# def doRequest(client):
#     while True:
#         message=client.recv(1024)
#         print(message.decode())
#         client.send('服务端收到'.encode())

        


# if __name__ == "__main__":
#     main()