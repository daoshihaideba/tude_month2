"""
Name   : Levi
Date   : 2022-03-30
Email  : lvze@tedu.cn
Env    : Python3.6

udp套接字和进程的综合代码训练
"""
from socket import *
from multiprocessing import Process

# 服务端地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 存储用户信息  {name: address}
user = {}


# 处理进入
def do_login(sock, name, addr):
    if name in user or "管理" in name:
        sock.sendto(b'FAIL', addr)
    else:
        sock.sendto(b'OK', addr)
        # 告知其他人
        msg = "欢迎 %s 加入群聊" % name
        for key, value in user.items():
            sock.sendto(msg.encode(), value)
        user[name] = addr  # 增加用户
    # print(user)  # 测试


# 处理聊天
def do_chat(sock, name, content):
    msg = "%s : %s" % (name, content)
    for key, value in user.items():
        # 不要发送给他本人
        if key != name:
            sock.sendto(msg.encode(), value)


# 处理退出
def do_quit(sock, name):
    # 防止服务器异常退出后重启，user为空，此时用户再请求退出
    if name in user:
        del user[name]  # 删除用户
    # 通知其他人
    msg = "%s 退出了群聊" % name
    for key, value in user.items():
        sock.sendto(msg.encode(), value)

# 子进程函数
def do_request(sock):
    # 循环接收客户端请求   总分 ： 总体接收请求 分情况讨论
    while True:
        request, addr = sock.recvfrom(1024)
        tmp = request.decode().split(' ', 2)  # 解析请求
        if tmp[0] == "LOGIN":
            # tmp --> [LOGIN,name]
            do_login(sock, tmp[1], addr)
        elif tmp[0] == "CHAT":
            # tmp --> [CHAT,name,content]
            do_chat(sock, tmp[1], tmp[2])
        elif tmp[0] == "QUIT":
            # tmp --> [QUIT,name]
            do_quit(sock, tmp[1])


# 搭建循环网路模型
def main():
    # udp套接字
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)
    # 子进程处理客户端请求
    p = Process(target=do_request,args=(sock,), daemon=True)
    p.start()
    # 循环的随时发送管理员信息
    while True:
        content = input("管理员消息:")
        if not content:
            break
        msg = "CHAT 管理员消息 " + content
        sock.sendto(msg.encode(),ADDR) # 父进程发送到子进程
    sock.close()

if __name__ == '__main__':
    main()
