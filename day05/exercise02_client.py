"""
聊天机器人客户端
"""
from socket import *

# 访问服务器的地址
ADDR = ("127.0.0.1",8888)

# 具体功能
def control(q):
    tcp_socket = socket()
    tcp_socket.connect(ADDR)
    tcp_socket.send(q.encode())  # 发送问题
    data = tcp_socket.recv(1024) # 接受回答
    tcp_socket.close()
    return data.decode()

# 与用户交互
def view():
    # 发送接收内容
    while True:
        q = input("我:")
        if not q:
            break
        res = control(q)
        print("小美:", res)

view()
