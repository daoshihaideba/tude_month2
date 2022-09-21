"""
tcp 套接字客户端
"""
from socket import *

# 访问服务器的地址
ADDR = ("127.0.0.1",8888)

# 创建tcp套接字
tcp_socket = socket()

# 连接服务器
tcp_socket.connect(ADDR)

# 发送接收内容
while True:
    msg = input(">>")
    tcp_socket.send(msg.encode())
    if msg == '##':
        break # 表示要退出
    data = tcp_socket.recv(1024)
    print("Server:",data.decode())

# 关闭套接字
tcp_socket.close()
