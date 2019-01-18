import socket
import os
import sys
import string

def main():
    if len(sys.argv)!=3:
        print('参数错误！')
        return
    address = ((sys.argv[1],int(sys.argv[2])))
    client = socket.socket()
    try:
        client.connect(address)
    except Exception as e:
        print(e)
        return
    
    #客户端连接成功，进入一级界面

    while 1:
        prompt = '''
        **************一级界面************
        ----1.注册   2.登录   3.退出---
        *********************************
        请选择（1/2/3）：
        '''

        cmd = input(prompt)
        if cmd.isdigit() and cmd in ['1','2','3']:
            if cmd == '1':
                deRegister(client)
            elif cmd == '2':
                doLogin(client)
            else:
                doExit()
        else:
            print('你输错了，请按照格式输入喔！')

def deRegister(client):
    while 1:
        allchars = string.punctuation + string.whitespace
        username = input("\033[31m]请输入注册用户名：\033[0m")
        for u in username:
            if u in allchars:
                print('用户名不能有特殊字符~~~')
                break

        password1 = input('请输入密码：')
        password2 = input('请重新输入密码：')


def doLogin(client):
    pass

def doExit():
    pass

if __name__ == "__main__":
    
    main()