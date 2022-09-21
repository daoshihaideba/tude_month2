"""
tcp 套接字客户端
"""
from socket import *

# 访问服务器的地址
ADDR = ("127.0.0.1",8888)

# 发送接收内容
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket = socket()
    tcp_socket.connect(ADDR)
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("Server:",data.decode())
    tcp_socket.close()
