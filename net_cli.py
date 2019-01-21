import socket
import sys

client=socket.socket()
if len(sys.argv)!=3:
    
    sys.exit('请在命令行里以主机地址和端口结束~')

host=sys.argv[1]
port=int(sys.argv[2])#argv列表里的都是字符串

client.connect((host,port))
while True:
    msg=input('请输入：')
    client.send(msg.encode())
    if not msg:
        break
    data=client.recv(1024)
    print('服务器返回结果：',data.decode())

client.close()

    



