'''
项目:电子词典
模块:socket pymysql 
'''
import socket
import pymysql
import os 
import sys 

# 搭建网络
def main():
    ADDRESS = ('0.0.0.0',8888)
    # 创建数据库连接
    db = pymysql.connect('localhost','root','123456',
                          'dict',charset='utf8')
    # 创建TCP套接字
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置端口复用
    server.setsockopt(socket.SOL_SOCKET,
                      socket.SO_REUSEADDR,1)
    server.bind(ADDRESS)
    server.listen(10)
    print("等待客户端连接......")
    while True:
        try:
            client,addr = server.accept()
            print('客户端',addr,'连接过来了')
        except KeyboardInterrupt:
            sys.exit('服务器关闭')
        except Exception as e:
            print(e)
            continue
        
        # 创建进程,子进程和客户端交互，父进程等待其他客户端连接
        pid = os.fork()
        # 子进程负责和客户端交互
        if pid == 0:
            doRequest(client,db)
            sys.exit('客户端退出')
        # 父进程继续上去等待下一个客户端连接
        else:
            continue

# 处理客户端请求函数
def doRequest(client,db):
    while True:
        message = client.recv(1024).decode()
        msgList = message.split(' ')
        # msgList: ['R','用户名','密码']
        # 一级子界面退出功能
        if msgList[0] == 'E':
            sys.exit(0)
        elif msgList[0] == 'R':
            # 处理注册函数
            doRegister(client,db,msgList[1],msgList[2])

        elif msgList[0] == 'L':
            # 处理登录函数
            doLogin(client,db,msgList[1],msgList[2])

        elif msgList[0] == 'Q':
            doQuery(client,db,msgList[1],msgList[2])

        elif msgList[0] == 'H':
            dohistory(client,db,msgList[1])

def dohistory(client,db,username):
    cursor = db.cursor()
    sel = 'select * from history where username=%s'
    cursor.execute(sel,[username])
    result = cursor.fetchall()
    if not result:
        client.send('Fail'.encode())
    else:
        client.send(b'OK')
        import time
        time.sleep(0.1)
        for r in result:
            message = '%s %s %s' % (r[1],r[2],r[3])
            client.send(message.encode())
            time.sleep(0.1)
        client.send(b"##")
        time.sleep(0.1)


def doQuery(client,db,username,word):
    cursor = db.cursor()
    sel = 'select interpret from words where word=%s'
    cursor.execute(sel,[word])
    result = cursor.fetchall()
    if not result:
        client.send(b"Fail")
    else:
        client.send(result[0][0].encode())
        doinsert_History(db,username,word)

def doinsert_History(db,username,word):
    cursor = db.cursor()
    ins = 'insert into history(username,word,time) \
    values(%s,%s,%s)'
    import time
    Time = time.ctime()
    try:
        cursor.execute(ins,[username,word,Time])
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

# 处理注册函数
def doRegister(client,db,username,password):
    # 判断user表中是否有此用户
    cursor = db.cursor()
    sel = 'select password from user where username=%s'
    # 根据要注册的用户名判断查询结果是否为空
    cursor.execute(sel,[username])
    # r结果为元组(用户不存在,空元组,否则为非空元组)
    r = cursor.fetchall()
    if r:
        client.send('EXISTS'.encode())
        return
    else:
        # 用户不存在,可以注册
        ins = 'insert into user(username,password) \
               values (%s,%s)'
        try:
            cursor.execute(ins,[username,password])
            db.commit()
            client.send('OK'.encode())
        except Exception as e:
            db.rollback()
            client.send('FAIL'.encode())

    
# 处理登录函数
def doLogin(client,db,username,password):
    sel = 'select password from user where username=%s'
    cursor = db.cursor()
    cursor.execute(sel,[username])
    r = cursor.fetchall()
    # 如果没有查到结果，表示用户名输入错误
    if not r:
        client.send('NAMEERROR'.encode())
    # ((203804380abcd323d),)
    elif r[0][0] == password:
        client.send('OK'.encode())
    else:
        client.send('PWDERROR'.encode())


if __name__ == '__main__':
    main()













